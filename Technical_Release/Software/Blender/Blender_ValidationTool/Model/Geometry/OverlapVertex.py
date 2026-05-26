# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Geometry/OverlapVertex.py

Check Overlap Vertices - module thuộc tầng Model của hệ thống validation.

Phát hiện các đỉnh trùng vị trí hoặc nằm quá gần nhau theo ngưỡng
MERGE_THRESHOLD. Hai đỉnh có khoảng cách Euclid <= ngưỡng được coi là
overlap, bất kể chúng có nối với nhau bằng cạnh hay không (kiểm theo
toạ độ local).

Thuật toán dùng mathutils.kdtree.KDTree: O((N log N)) thay vì O(N^2) khi
duyệt cặp brute-force.

API:

    check_object(obj) -> list[int] | None
        PURE CHECK - đăng ký trong Config.CHECK_FUNCTIONS["geo_overlapvertex"].
        - list rỗng []         : mesh sạch.
        - list các vert index  : các đỉnh bị overlap.
        - None                 : obj không hợp lệ.

    check_and_highlight(objs) -> dict[str, list[int]] | None
        WORKFLOW UI - dùng khi user click "Run Check".
            1. (Tiền điều kiện) User chọn 1 hoặc nhiều mesh ở Object Mode.
               Controller đã lọc bỏ Light/Camera/...
            2. Tự động chạy 3-7.
            3. Multi-object Edit Mode + Vertex Select + Select All.
            4. Chạy check_object() cho từng obj.
            5. Có lỗi: deselect, select các đỉnh overlap trên các mesh.
            6. Lưu trạng thái View3D rồi bật X-Ray + Viewport Statistics
               (state là per-View3D-space, không phụ thuộc số object).
            7. Khi user Tab về Object Mode (hoặc Refresh) -> trả về trạng
               thái View3D ban đầu qua msgbus.

        Returns
        -------
        dict[str, list[int]] | None
            None / {} / {obj_name: [vert_idx,...]}.

    restore_state()
        Public hook để Controller/Refresh.py gọi cưỡng bức khôi phục
        View3D mà không phụ thuộc msgbus.
"""

import bpy
import bmesh
from mathutils.kdtree import KDTree


# Ngưỡng khoảng cách giữa 2 đỉnh: dưới ngưỡng này coi là overlap.
# 1e-4 ~ 0.1mm khi 1 Blender unit = 1m, hợp lý cho asset game/film.
MERGE_THRESHOLD = 1e-4


# ---------------------------------------------------------------------------
# Core algorithm
# ---------------------------------------------------------------------------
def find_overlap_vertex_indices(bm, threshold=MERGE_THRESHOLD):
    """
    Trả về set[int] các vert index có ít nhất 1 đỉnh khác nằm trong bán
    kính `threshold`. KDTree tự đối xứng: nếu A gần B thì B cũng gần A,
    nên duyệt mỗi đỉnh 1 lần là đủ.
    """
    n = len(bm.verts)
    if n < 2:
        return set()

    tree = KDTree(n)
    for v in bm.verts:
        tree.insert(v.co, v.index)
    tree.balance()

    overlap = set()
    for v in bm.verts:
        # find_range trả về cả chính v (distance 0). Cần ít nhất 1 hit
        # khác index thì mới tính là overlap.
        for _co, idx, _dist in tree.find_range(v.co, threshold):
            if idx != v.index:
                overlap.add(v.index)
                overlap.add(idx)

    return overlap


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Validation entry-point - pure check, không có side-effect.

    Returns
    -------
    list[int] | None
        - List index các vert bị overlap (rỗng nghĩa là sạch).
        - None nếu obj không hợp lệ.
    """
    if obj is None or obj.type != 'MESH' or obj.data is None:
        return None

    me = obj.data
    if len(me.vertices) < 2:
        return []

    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(me)
        owned = False
    else:
        bm = bmesh.new()
        bm.from_mesh(me)
        owned = True

    try:
        bm.verts.ensure_lookup_table()
        return sorted(find_overlap_vertex_indices(bm))
    finally:
        if owned:
            bm.free()


# ===========================================================================
# Workflow: Run check + select overlap verts + X-Ray + Statistics
# ===========================================================================
#
# State management:
#   - Trước khi bật X-Ray/Stats, lưu giá trị cũ của mọi VIEW_3D space.
#   - msgbus subscribe `obj.mode`: khi user Tab (mode != 'EDIT') thì
#     khôi phục lại đúng giá trị đã lưu rồi unsubscribe.
#   - Hàm restore_state() public cho Refresh.py gọi cưỡng bức.

_state_owner = object()      # owner id cho msgbus
_watched_obj_names = []      # list tên object đang track, [] = không track
_saved_view_states = []      # [{'space', 'xray', 'stats'}, ...]


def _snapshot_and_set_view_state():
    """Lưu show_xray + show_stats của mọi View3D space rồi bật cả hai."""
    global _saved_view_states
    _saved_view_states = []

    wm = bpy.context.window_manager
    if wm is None:
        return

    for window in wm.windows:
        for area in window.screen.areas:
            if area.type != 'VIEW_3D':
                continue
            for space in area.spaces:
                if space.type != 'VIEW_3D':
                    continue
                _saved_view_states.append({
                    'space': space,
                    'xray': space.shading.show_xray,
                    'stats': space.overlay.show_stats,
                })
                space.shading.show_xray = True
                space.overlay.show_stats = True


def _restore_view_state():
    """Trả show_xray + show_stats về đúng giá trị đã snapshot."""
    global _saved_view_states
    for entry in _saved_view_states:
        space = entry['space']
        try:
            space.shading.show_xray = entry['xray']
            space.overlay.show_stats = entry['stats']
        except (ReferenceError, AttributeError):
            # space đã bị đóng/đổi loại - bỏ qua, không phá vỡ vòng lặp.
            pass
    _saved_view_states = []

    wm = bpy.context.window_manager
    if wm is not None:
        for window in wm.windows:
            for area in window.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()


def _on_mode_change():
    """Restore View3D khi mọi mesh đã track đều thoát Edit Mode."""
    global _watched_obj_names
    if not _watched_obj_names:
        bpy.msgbus.clear_by_owner(_state_owner)
        return

    any_in_edit = False
    any_alive = False
    for name in _watched_obj_names:
        obj = bpy.data.objects.get(name)
        if obj is None:
            continue
        any_alive = True
        if obj.mode == 'EDIT':
            any_in_edit = True

    if not any_alive:
        # Toàn bộ object đã bị xóa.
        bpy.msgbus.clear_by_owner(_state_owner)
        _watched_obj_names = []
        _saved_view_states.clear()
        return

    if any_in_edit:
        return

    _restore_view_state()
    bpy.msgbus.clear_by_owner(_state_owner)
    _watched_obj_names = []


def _watch_mode_change(objs):
    """Subscribe vào obj.mode của mọi obj để bắt sự kiện Tab."""
    bpy.msgbus.clear_by_owner(_state_owner)
    for obj in objs:
        bpy.msgbus.subscribe_rna(
            key=obj.path_resolve("mode", False),
            owner=_state_owner,
            args=(),
            notify=_on_mode_change,
        )


def restore_state():
    """
    Public hook cho Refresh.py: khôi phục View3D + huỷ subscription kể cả
    khi mode chưa đổi (Refresh có thể đổi mode trước khi gọi, hoặc không).
    An toàn để gọi nhiều lần.

    Refresh được coi là "dọn dẹp cứng": sau khi restore từ snapshot, tắt
    luôn X-Ray ở mọi View3D space (kể cả trước check user đã bật) để mọi
    lần Refresh đều cho ra cùng một trạng thái viewport ổn định.
    """
    global _watched_obj_names
    _restore_view_state()
    bpy.msgbus.clear_by_owner(_state_owner)
    _watched_obj_names = []

    wm = bpy.context.window_manager
    if wm is None:
        return
    for window in wm.windows:
        for area in window.screen.areas:
            if area.type != 'VIEW_3D':
                continue
            for space in area.spaces:
                if space.type != 'VIEW_3D':
                    continue
                try:
                    space.shading.show_xray = False
                except (ReferenceError, AttributeError):
                    pass
            area.tag_redraw()


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    Multi-object 7-step flow:
        1. Controller đã lọc objs chỉ còn mesh hợp lệ.
        2. Tự động thực hiện 3-7.
        3. Multi-object Edit Mode + Vertex Select + Select All.
        4. Per-obj: chạy check_object().
        5. Có lỗi: deselect, select các vert overlap trên các mesh.
           Sạch: về Object Mode, không đổi View3D.
        6. Snapshot rồi bật X-Ray + Viewport Statistics.
        7. Watcher: Tab -> restore_state.

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

    # ---- Step 3: Edit Mode + Vertex Select + Select All ----
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='SELECT')

    # ---- Step 4: chạy check trên từng obj ----
    issues = {}
    for obj in valid_objs:
        result = check_object(obj)
        if result:
            issues[obj.name] = result

    # ---- Step 5: select riêng các vert overlap, hoặc thoát nếu sạch ----
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
        bm.verts.ensure_lookup_table()
        n_verts = len(bm.verts)
        for idx in idx_list:
            if 0 <= idx < n_verts:
                bm.verts[idx].select = True
                selected_any = True
        bm.select_flush_mode()
        bmesh.update_edit_mesh(obj.data)

    if not selected_any:
        return issues

    # ---- Step 6: snapshot rồi bật X-Ray + Statistics ----
    _snapshot_and_set_view_state()

    # ---- Step 7: watch Tab để restore ----
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
        print("[OverlapVertex] Không có mesh hợp lệ trong selection.")
    elif not _result:
        print(f"[OverlapVertex] {len(_objs)} mesh: tất cả sạch.")
    else:
        total = sum(len(v) for v in _result.values())
        print(f"[OverlapVertex] {total} overlap vert(s) trên {len(_result)} mesh:")
        for name, idxs in _result.items():
            preview = idxs if len(idxs) <= 20 else idxs[:20] + ['...']
            print(f"  - {name}: {preview}")
        print("[OverlapVertex] Nhấn Tab hoặc Refresh để khôi phục View3D.")
