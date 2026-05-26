# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Scene/History.py
Workflow:
    1. Nhận list object do user chọn.
    2. Lọc bỏ các type không liên quan đến mesh pipeline:
       Camera, Light, Armature (Skeleton), Empty, Speaker, Lattice, ...
       Chỉ giữ lại các type convert-able: MESH/CURVE/SURFACE/META/FONT.
    3. Tìm các object còn history (có modifier hoặc chưa phải MESH).
    4. Ép Object Mode, deselect all, rồi select đúng những object đó
       để user tự xử lý (apply modifier / Convert To Mesh).
API:
    check_object(obj) -> list[str] | None
        PURE CHECK - đăng ký trong Config.CHECK_FUNCTIONS["scn_history"].
        - list rỗng []         : MESH sạch, không modifier.
        - list các string      : các "history item" (tên modifier hoặc
                                 marker "<type:CURVE>") đang tồn tại.
        - None                 : obj không hợp lệ hoặc type bị bỏ qua
                                 (Camera/Light/Armature/...).

    check_and_highlight(objs) -> dict[str, list[str]] | None
        WORKFLOW UI - dùng khi user click "Run Check".
        Returns
        -------
        dict[str, list[str]] | None
            - None                   : input rỗng / không có obj hợp lệ.
            - {} (dict rỗng)         : tất cả candidate đã sạch sẵn.
            - {obj_name: [items,...]}: các obj còn history; đã được
              select sẵn trong viewport, kèm danh sách item cần xử lý
              (modifier name hoặc "<type:XXX>").
"""

import bpy


# ---------------------------------------------------------------------------
# Type filter
# ---------------------------------------------------------------------------
# Các type có thể convert sang MESH thông qua bpy.ops.object.convert(target='MESH').
# Object type khác (CAMERA / LIGHT / ARMATURE / EMPTY / ...) bị bỏ qua hoàn toàn.
CONVERTIBLE_TYPES = {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Pure check - không có side-effect.
    Returns
    -------
    list[str] | None
        - List các "history item" đang tồn tại (rỗng nghĩa là sạch).
          Mỗi item là tên modifier, hoặc marker "<type:XXX>" nếu obj
          chưa phải là MESH.
        - None nếu obj không hợp lệ / type bị bỏ qua.
    """
    if obj is None or obj.data is None:
        return None
    if obj.type not in CONVERTIBLE_TYPES:
        # Camera, Light, Armature (Skeleton), Empty, Speaker, Lattice, ...
        return None

    items = []
    if obj.type != 'MESH':
        items.append(f"<type:{obj.type}>")
    # obj.modifiers tồn tại trên mọi Object có data; với CURVE/SURFACE/...
    # cũng có thể chứa modifiers - liệt kê hết.
    for mod in obj.modifiers:
        items.append(mod.name)
    return items

# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    Workflow:
        1. Lọc objs xuống còn các type convert-able (Camera/Light/Armature
           bị bỏ qua).
        2. Chạy check_object() từng obj để tìm các obj còn history.
        3. Ép Object Mode + deselect all, rồi select đúng các obj còn
           history để user tự xử lý.
    Parameters
    ----------
    objs : list[bpy.types.Object]
        Danh sách object user đã chọn. Có thể lẫn Camera/Light/Armature,
        hàm sẽ tự bỏ qua.

    Returns
    -------
    dict[str, list[str]] | None
        None / {} / {obj_name: [items,...]}.
    """
    if not objs:
        return None

    # ---- Step 1: lọc candidate ----
    candidates = [
        o for o in objs
        if o is not None
        and o.type in CONVERTIBLE_TYPES
        and o.data is not None
    ]
    if not candidates:
        return None

    # ---- Step 2: tìm các obj còn history ----
    issues = {}
    targets = []
    for o in candidates:
        items = check_object(o)
        if items:
            issues[o.name] = items
            targets.append(o)

    # ---- Step 3: chuẩn hóa Mode + selection ----
    # Ép về Object Mode trước khi đụng vào select_set (Edit Mode đôi khi
    # khóa selection ở Object level).
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

    # ---- Step 4: select các obj còn history để user tự xử lý ----
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
        print("[History] Không có object hợp lệ trong selection.")
    elif not _result:
        print(f"[History] {len(_objs)} object: tất cả đã sạch.")
    else:
        total = sum(len(v) for v in _result.values())
        print(f"[History] {len(_result)} object còn history "
              f"({total} item), đã select sẵn để user xử lý:")
        for name, items in _result.items():
            preview = items if len(items) <= 20 else items[:20] + ['...']
            print(f"  - {name}: {preview}")
