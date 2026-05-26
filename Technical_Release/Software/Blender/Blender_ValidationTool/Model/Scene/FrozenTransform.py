# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Scene/FrozenTransform.py

Check Frozen Transform - module thuộc tầng Model của hệ thống validation.

Một object được coi là "frozen transform" khi:
    - Location = (0, 0, 0)
    - Rotation = (0, 0, 0)    (mọi rotation_mode)
    - Scale    = (1, 1, 1)

Nếu lệch khỏi identity -> user cần Apply Transform (Ctrl+A) trước khi export.

API:

    check_object(obj) -> list[str] | None
        PURE CHECK - đăng ký trong Config.CHECK_FUNCTIONS["scn_frozen"].
        - list rỗng []         : transform đã frozen (identity).
        - list các string      : các thành phần lệch, vd ["location", "scale"].
        - None                 : obj không hợp lệ.

    check_and_highlight(objs) -> dict[str, list[str]] | None
        WORKFLOW UI - dùng khi user click "Run Check".
            1. (Tiền điều kiện) Controller đã lọc objs chỉ còn MESH hợp lệ.
            2. Chạy check_object() trên từng obj.
            3. Ép Object Mode + deselect all, rồi select đúng các obj chưa
               frozen để user tự Apply Transform.

        Returns
        -------
        dict[str, list[str]] | None
            - None                   : input rỗng / không có obj hợp lệ.
            - {} (dict rỗng)         : tất cả obj đều đã frozen.
            - {obj_name: [comp,...]} : các obj chưa frozen, kèm danh sách
              thành phần lệch.
"""

import bpy


# Float tolerance: Blender lưu transform dưới dạng float32, các phép apply/undo
# có thể để lại noise ~1e-7. 1e-6 đủ chặt để bắt lỗi thật, đủ lỏng cho noise.
EPS = 1e-6


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _is_zero(vec):
    return all(abs(v) <= EPS for v in vec)


def _is_one(vec):
    return all(abs(v - 1.0) <= EPS for v in vec)


def _rotation_is_identity(obj):
    """Kiểm tra rotation = identity với mọi rotation_mode.

    Blender hỗ trợ EULER (XYZ/XZY/...), QUATERNION, AXIS_ANGLE. Mỗi mode lưu
    ở một property khác nhau; ta phải đọc đúng property của mode hiện tại,
    không thể chỉ check rotation_euler.
    """
    mode = obj.rotation_mode
    if mode == 'QUATERNION':
        q = obj.rotation_quaternion
        # Identity quaternion: (w=1, x=0, y=0, z=0). Quaternion (-1,0,0,0)
        # cũng biểu diễn cùng rotation nhưng Blender không tự normalize về
        # +1, nên ta chấp nhận cả hai.
        return (
            abs(abs(q[0]) - 1.0) <= EPS
            and abs(q[1]) <= EPS
            and abs(q[2]) <= EPS
            and abs(q[3]) <= EPS
        )
    if mode == 'AXIS_ANGLE':
        # rotation_axis_angle = (angle, x, y, z). Identity khi angle ~ 0.
        aa = obj.rotation_axis_angle
        return abs(aa[0]) <= EPS
    # EULER modes (XYZ/XZY/YXZ/YZX/ZXY/ZYX)
    return _is_zero(obj.rotation_euler)


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Pure check - không có side-effect.

    Returns
    -------
    list[str] | None
        - List các thành phần transform lệch khỏi identity. Rỗng nghĩa là
          obj đã frozen.
        - None nếu obj không hợp lệ.
    """
    if obj is None:
        return None

    issues = []
    if not _is_zero(obj.location):
        issues.append("location")
    if not _rotation_is_identity(obj):
        issues.append("rotation")
    if not _is_one(obj.scale):
        issues.append("scale")
    return issues


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    Workflow:
        1. Lọc objs xuống còn các obj hợp lệ.
        2. Chạy check_object() từng obj để tìm obj chưa frozen.
        3. Ép Object Mode + deselect all, rồi select đúng các obj đó
           để user tự Apply Transform (Ctrl+A).

    Parameters
    ----------
    objs : list[bpy.types.Object]
        Danh sách object đã được Controller lọc (chỉ MESH có data).

    Returns
    -------
    dict[str, list[str]] | None
        None / {} / {obj_name: ["location","rotation","scale"]}.
    """
    if not objs:
        return None

    # ---- Step 1: lọc candidate ----
    candidates = [o for o in objs if o is not None]
    if not candidates:
        return None

    # ---- Step 2: tìm các obj chưa frozen ----
    issues = {}
    targets = []
    for o in candidates:
        items = check_object(o)
        if items:
            issues[o.name] = items
            targets.append(o)

    # ---- Step 3: chuẩn hóa Mode + selection ----
    # Ép về Object Mode trước khi đụng select_set (Edit Mode khóa
    # selection ở Object level).
    if bpy.context.mode != 'OBJECT':
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            pass

    try:
        bpy.ops.object.select_all(action='DESELECT')
    except RuntimeError:
        pass

    # Sạch hết -> không cần select gì, trả {} để Controller báo OK.
    if not targets:
        return {}

    # ---- Step 4: select các obj chưa frozen để user tự xử lý ----
    try:
        for o in targets:
            o.select_set(True)
        bpy.context.view_layer.objects.active = targets[0]
    except (RuntimeError, ReferenceError):
        return None

    return issues


# ---------------------------------------------------------------------------
# Standalone debug
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _objs = list(bpy.context.selected_objects)
    _result = check_and_highlight(_objs)
    if _result is None:
        print("[FrozenTransform] Không có object hợp lệ trong selection.")
    elif not _result:
        print(f"[FrozenTransform] {len(_objs)} object: tất cả đã frozen.")
    else:
        print(f"[FrozenTransform] {len(_result)} object chưa frozen, "
              f"đã select sẵn - nhấn Ctrl+A để Apply Transform:")
        for name, items in _result.items():
            print(f"  - {name}: {', '.join(items)}")
