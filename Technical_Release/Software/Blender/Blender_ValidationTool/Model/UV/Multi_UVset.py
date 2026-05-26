# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/UV/Multi_UVset.py

"""

import bpy


# Số UV layer tối đa cho phép trên 1 mesh. Vượt quá -> lỗi.
# Mặc định = 1 (yêu cầu phổ biến cho asset game).
UV_MAP_NUM = 1


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Validation entry-point - pure check, không có side-effect.

    Returns
    -------
    list[int] | None
        - List index các UV layer dư (>= UV_MAP_NUM). Rỗng nghĩa là sạch.
        - None nếu obj không hợp lệ.
    """
    if obj is None or obj.type != 'MESH' or obj.data is None:
        return None

    uv_layers = obj.data.uv_layers
    n = len(uv_layers)
    if n <= UV_MAP_NUM:
        return []

    # Trả về index của các UV layer dư để khớp signature list[int]
    # với các check khác. Số phần tử = n - UV_MAP_NUM cũng chính là
    # "số UV thừa" hiển thị trong report.
    return list(range(UV_MAP_NUM, n))


# ===========================================================================
# Workflow: Run check + select offending objects + open DATA properties tab
# ===========================================================================
#
# Khác hẳn các check Geometry: lỗi nằm ở metadata của mesh (uv_layers),
# không phải topology. Không cần Edit Mode, không cần hide, không cần
# msgbus restore. Chỉ cần đưa user đến đúng chỗ để sửa: chọn object lỗi
# + mở Properties Editor ở tab Object Data.


def _switch_properties_to_data():
    """Tìm mọi Properties Editor đang mở và chuyển sang context='DATA'.

    'DATA' là tab Object Data Properties - nơi chứa UV Maps panel cho mesh.
    Set thẳng space.context thay vì gọi bpy.ops vì op cần đúng context
    override, trong khi gán property thì luôn chạy được.
    """
    wm = bpy.context.window_manager
    if wm is None:
        return

    switched_any = False
    for window in wm.windows:
        for area in window.screen.areas:
            if area.type != 'PROPERTIES':
                continue
            for space in area.spaces:
                if space.type != 'PROPERTIES':
                    continue
                try:
                    space.context = 'DATA'
                    switched_any = True
                except (TypeError, AttributeError):
                    # Một số object type (Empty/Light...) không có tab DATA;
                    # nhưng ta đã đảm bảo active là MESH ở trên rồi nên rất
                    # hiếm khi rơi vào nhánh này.
                    pass
            area.tag_redraw()

    return switched_any


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    Multi-object workflow (Object Mode, không vào Edit Mode):
        1. Controller đã lọc objs chỉ còn mesh hợp lệ.
        2. Tự động thực hiện 3-5.
        3. Đảm bảo Object Mode.
        4. Per-obj: chạy check_object().
        5. Có lỗi: deselect all, select riêng các object lỗi, set active
                   = obj lỗi đầu tiên, chuyển Properties Editor -> DATA.
           Sạch: không đổi selection.

    Parameters
    ----------
    objs : list[bpy.types.Object]
        Danh sách mesh đã được Controller lọc (chỉ type=='MESH', data!=None).

    Returns
    -------
    dict[str, list[int]] | None
        None / {} / {obj_name: [uv_layer_idx,...]}.
    """
    if not objs:
        return None

    valid_objs = [
        o for o in objs
        if o is not None and o.type == 'MESH' and o.data is not None
    ]
    if not valid_objs:
        return None

    # Đảm bảo Object Mode trước khi đụng selection.
    if bpy.context.mode != 'OBJECT':
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            pass

    # ---- Step 4: chạy check trên từng obj ----
    issues = {}
    for obj in valid_objs:
        result = check_object(obj)
        if result:
            issues[obj.name] = result

    # ---- Step 5: sạch -> trả về luôn, không đụng selection ----
    if not issues:
        return {}

    # Có lỗi: deselect all rồi chỉ select các obj lỗi.
    try:
        bpy.ops.object.select_all(action='DESELECT')
    except RuntimeError:
        # Fallback nếu op không poll được (ví dụ scene rỗng đặc biệt).
        for o in bpy.context.view_layer.objects:
            o.select_set(False)

    bad_objs = []
    for obj in valid_objs:
        if obj.name in issues:
            try:
                obj.select_set(True)
                bad_objs.append(obj)
            except (RuntimeError, ReferenceError):
                pass

    if bad_objs:
        try:
            bpy.context.view_layer.objects.active = bad_objs[0]
        except (RuntimeError, ReferenceError):
            pass

    # Mở Properties Editor sang tab Object Data để user thấy UV Maps panel.
    _switch_properties_to_data()

    return issues


# ---------------------------------------------------------------------------
# Standalone debug
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _objs = [o for o in bpy.context.selected_objects if o.type == 'MESH']
    _result = check_and_highlight(_objs)
    if _result is None:
        print("[Multi_UVset] Không có mesh hợp lệ trong selection.")
    elif not _result:
        print(f"[Multi_UVset] {len(_objs)} mesh: tất cả <= {UV_MAP_NUM} UV layer.")
    else:
        print(
            f"[Multi_UVset] {len(_result)} mesh có > {UV_MAP_NUM} UV layer:"
        )
        for name, idxs in _result.items():
            print(f"  - {name}: dư {len(idxs)} UV (index {idxs})")
