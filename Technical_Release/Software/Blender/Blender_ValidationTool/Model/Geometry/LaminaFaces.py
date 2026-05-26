# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Geometry/LaminaFaces.py

Check Lamina Faces - module thuộc tầng Model của hệ thống validation.

Lamina Faces (theo định nghĩa Maya): các face chồng/duplicate lên nhau,
biểu hiện qua việc 2+ face cùng dùng chung một dải cạnh liền nhau trên
chu vi của chúng.

Điều kiện phát hiện:
    Đi dọc chu vi của mỗi face, nếu tồn tại CỬA SỔ TRƯỢT gồm
    MIN_CHAIN_LENGTH cạnh liên tiếp mà tất cả các cạnh trong cửa sổ
    đều được dùng chung bởi ÍT NHẤT MỘT face khác -> đánh dấu cả face
    hiện tại lẫn (các) face kia là Lamina.

    Mặc định MIN_CHAIN_LENGTH = 3 (giống Maya Cleanup > Lamina Faces).

API:

    check_object(obj) -> list[int] | None
        PURE CHECK - đăng ký trong Config.CHECK_FUNCTIONS["geo_lamina"].
        - list rỗng []         : mesh sạch.
        - list các face index  : các face bị lamina.
        - None                 : obj không hợp lệ.

    check_and_highlight(objs) -> dict[str, list[int]] | None
        WORKFLOW UI - dùng khi user click "Run Check".
            1. (Tiền điều kiện) User chọn 1 hoặc nhiều mesh ở Object Mode.
               Các loại object khác đã được lọc bỏ ở tầng Controller.
            2. Tự động chạy 3-6.
            3. Multi-object Edit Mode + Face Select + Select All.
            4. Chạy check_object() cho từng obj.
            5. Select lamina trên các mesh, hide phần còn lại.
            6. Khi user Tab về Object Mode -> reveal all trên mọi mesh
               đã track qua msgbus.

        Returns
        -------
        dict[str, list[int]] | None
            None / {} / {obj_name: [face_idx,...]}.
"""

import bpy
import bmesh


# Số cạnh liên tiếp tối thiểu để coi là Lamina. Giữ = 3 để khớp Maya.
MIN_CHAIN_LENGTH = 3


# ---------------------------------------------------------------------------
# Core algorithm
# ---------------------------------------------------------------------------
def find_lamina_face_indices(bm, min_chain=MIN_CHAIN_LENGTH):
    """
    Tìm tất cả face index là Lamina Faces.

    Thuật toán: với mỗi face, đi dọc chu vi (cyclic) và kiểm tra mọi
    cửa sổ trượt gồm `min_chain` cạnh liên tiếp. Nếu tồn tại 1 face
    khác cùng chia sẻ tất cả các cạnh trong cửa sổ -> cả 2 đều lamina.

    Trả về set[int] các face index.
    """
    lamina = set()

    for face in bm.faces:
        loops = face.loops
        n = len(loops)
        if n < min_chain:
            continue

        # face.edges thông qua loops giữ đúng thứ tự cyclic quanh face.
        ring = [loop.edge for loop in loops]
        f_idx = face.index

        for start in range(n):
            # Lấy giao của (link_faces - {face hiện tại}) trên min_chain cạnh.
            common = None
            for k in range(min_chain):
                edge = ring[(start + k) % n]
                others = {f.index for f in edge.link_faces if f.index != f_idx}
                if not others:
                    common = None
                    break
                common = others if common is None else (common & others)
                if not common:
                    break

            if common:
                lamina.add(f_idx)
                lamina.update(common)

    return lamina


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Validation entry-point - pure check, không có side-effect.

    Returns
    -------
    list[int] | None
        - List index các face bị lamina (rỗng nghĩa là sạch).
        - None nếu obj không hợp lệ.
    """
    if obj is None or obj.type != 'MESH' or obj.data is None:
        return None

    me = obj.data
    if len(me.polygons) == 0:
        return []

    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(me)
        owned = False
    else:
        bm = bmesh.new()
        bm.from_mesh(me)
        owned = True

    try:
        bm.faces.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        return sorted(find_lamina_face_indices(bm))
    finally:
        if owned:
            bm.free()


# ===========================================================================
# Workflow: Run check + isolate error faces + auto-reveal on Tab
# ===========================================================================
#
# Watcher (step 6) - giống Concave.py:
#   - msgbus subscribe vào property `mode` của object đang track.
#   - Khi user Tab -> mode đổi -> callback chạy.
#   - Callback reveal all (set hide=False trên mesh data) rồi unsubscribe.

_state_owner = object()
_watched_obj_names = []      # list tên object đang track, [] nếu không track


def _reveal_all(obj):
    """Tương đương bpy.ops.mesh.reveal() nhưng làm được từ Object Mode."""
    me = obj.data
    for p in me.polygons:
        p.hide = False
    for e in me.edges:
        e.hide = False
    for v in me.vertices:
        v.hide = False
    me.update()

    wm = bpy.context.window_manager
    if wm is not None:
        for window in wm.windows:
            for area in window.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()


def _on_mode_change():
    """Reveal khi mọi mesh đã track đều thoát Edit Mode."""
    global _watched_obj_names
    if not _watched_obj_names:
        bpy.msgbus.clear_by_owner(_state_owner)
        return

    valid_objs = []
    any_in_edit = False
    for name in _watched_obj_names:
        obj = bpy.data.objects.get(name)
        if obj is None:
            continue
        valid_objs.append(obj)
        if obj.mode == 'EDIT':
            any_in_edit = True

    if any_in_edit:
        return

    for obj in valid_objs:
        _reveal_all(obj)
    bpy.msgbus.clear_by_owner(_state_owner)
    _watched_obj_names = []


def _watch_mode_change(objs):
    bpy.msgbus.clear_by_owner(_state_owner)
    for obj in objs:
        bpy.msgbus.subscribe_rna(
            key=obj.path_resolve("mode", False),
            owner=_state_owner,
            args=(),
            notify=_on_mode_change,
        )


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    Multi-object 6-step flow:
        1. Controller đã lọc objs chỉ còn mesh hợp lệ.
        2. Tự động chạy 3-6.
        3. Multi-object Edit Mode + Face Select + Select All.
        4. Per-obj: chạy check_object().
        5. Có lỗi: select lamina trên các mesh có issue, hide phần còn lại.
           Sạch: về Object Mode.
        6. Watcher: Tab -> reveal all.

    Returns
    -------
    dict[str, list[int]] | None
    """
    global _watched_obj_names

    if not objs:
        return None

    valid_objs = [
        o for o in objs
        if o is not None and o.type == 'MESH' and o.data is not None
    ]
    if not valid_objs:
        return None

    if bpy.context.mode != 'OBJECT':
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            pass

    try:
        for o in valid_objs:
            o.select_set(True)
        current_active = bpy.context.view_layer.objects.active
        if current_active not in valid_objs:
            bpy.context.view_layer.objects.active = valid_objs[0]
    except (RuntimeError, ReferenceError):
        return None

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='SELECT')

    issues = {}
    for obj in valid_objs:
        result = check_object(obj)
        if result:
            issues[obj.name] = result

    if not issues:
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        return {}

    bpy.ops.mesh.select_all(action='DESELECT')

    selected_any = False
    for obj in valid_objs:
        idx_list = issues.get(obj.name)
        if not idx_list:
            continue
        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()
        n_faces = len(bm.faces)
        for idx in idx_list:
            if 0 <= idx < n_faces:
                bm.faces[idx].select = True
                selected_any = True
        bm.select_flush_mode()
        bmesh.update_edit_mesh(obj.data)

    if not selected_any:
        return issues

    bpy.ops.mesh.hide(unselected=True)

    _watched_obj_names = [o.name for o in valid_objs]
    _watch_mode_change(valid_objs)

    return issues


# ---------------------------------------------------------------------------
# Standalone debug
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _objs = [o for o in bpy.context.selected_objects if o.type == 'MESH']
    _result = check_and_highlight(_objs)
    if _result is None:
        print("[Lamina] Không có mesh hợp lệ trong selection.")
    elif not _result:
        print(f"[Lamina] {len(_objs)} mesh: tất cả sạch.")
    else:
        total = sum(len(v) for v in _result.values())
        print(f"[Lamina] {total} lamina face(s) trên {len(_result)} mesh:")
        for name, idxs in _result.items():
            preview = idxs if len(idxs) <= 20 else idxs[:20] + ['...']
            print(f"  - {name}: {preview}")
        print("[Lamina] Nhấn Tab để reveal lại toàn bộ mesh.")
