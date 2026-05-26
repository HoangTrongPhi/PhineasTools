# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/UV/OverlapUV.py

Check Overlap UV - phát hiện UV Island chồng đè trong UV space.

Ý tưởng:
    Một mesh bị Overlap UV khi tồn tại >= 2 UV Island khác nhau mà vùng
    UV của chúng có diện tích giao > 0. Hai island chỉ tiếp xúc cạnh /
    đỉnh (packed sát) KHÔNG tính là overlap.

API:

    check_object(obj) -> list[int] | None
        PURE CHECK - đăng ký trong Config.CHECK_FUNCTIONS["uv_overlap"].
        - list rỗng []         : mesh sạch.
        - list face index      : các face thuộc các island bị overlap.
        - None                 : obj không hợp lệ.

    check_and_highlight(objs) -> dict[str, list[int]] | None
        WORKFLOW UI - dùng khi user click "Run Check".
            1. Controller đã lọc objs chỉ còn mesh hợp lệ.
            2. Nếu CÓ NHIỀU mesh trong selection:
               - Chạy check pure trên từng obj.
               - Select tất cả các object lỗi (Object Mode).
               - Popup nhắc "chỉ nên check từng object".
            3. Nếu CHỈ 1 mesh trong selection và phát hiện lỗi:
               - Set obj đó làm active + select.
               - Vào Edit Mode (nếu chưa).
               - ADDITIVELY select bad face ở MESH side + ADDITIVELY set
                 UV loop selection trên bad face. Các face / UV shell
                 KHÔNG overlap giữ nguyên trạng thái selection cũ - chỉ
                 thêm bad shells vào, không deselect ai.
               - Chuyển workspace hiện tại sang 'UV Editing'.
               - KHÔNG đổi sync, KHÔNG đổi uv_select_mode.
               - Tương thích Blender < 3.5 (BMLoopUV.select) và Blender
                 >= 3.5 (bool layer ".vs.<uv_name>" / ".es.<uv_name>").

        Returns
        -------
        dict[str, list[int]] | None
            None / {} / {obj_name: [face_idx,...]}.
"""

import bpy
import bmesh
from mathutils.geometry import (
    intersect_point_tri_2d,
    intersect_line_line_2d,
    tessellate_polygon,
)


# Tolerance cho việc so khớp UV khi build island.
UV_EPS = 1e-6
# Tolerance cho test hình học (AABB + edge crossing).
GEOM_EPS = 1e-7


# ---------------------------------------------------------------------------
# Core: build UV islands theo định nghĩa chuẩn (edge non-seam)
# ---------------------------------------------------------------------------
def _build_uv_islands(bm, uv_layer, eps=UV_EPS):
    """
    Gom face thành các UV Island bằng Union-Find.

    Hai face thuộc cùng 1 island <=> chia sẻ 1 edge VÀ UV ở CẢ HAI đỉnh
    của edge khớp nhau trên cả 2 mặt (edge không phải UV seam). Chỉ
    khớp 1 đỉnh là không đủ - đó là kiểu "chạm 1 điểm", không phải
    cùng island.

    Returns
    -------
    list[set[int]]
        Mỗi phần tử là set face-index của 1 island.
    """
    bm.faces.ensure_lookup_table()
    n_faces = len(bm.faces)
    parent = list(range(n_faces))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    eps_sq = eps * eps

    for edge in bm.edges:
        link_faces = edge.link_faces
        if len(link_faces) < 2:
            continue
        v_a, v_b = edge.verts[0], edge.verts[1]

        # Cache UV ở 2 endpoint cho mỗi face nối với edge này.
        face_uvs = []
        for f in link_faces:
            uv_a = uv_b = None
            for l in f.loops:
                if l.vert == v_a:
                    uv_a = l[uv_layer].uv
                elif l.vert == v_b:
                    uv_b = l[uv_layer].uv
                if uv_a is not None and uv_b is not None:
                    break
            face_uvs.append((f.index, uv_a, uv_b))

        for i in range(len(face_uvs)):
            fi, ai, bi = face_uvs[i]
            if ai is None or bi is None:
                continue
            for j in range(i + 1, len(face_uvs)):
                fj, aj, bj = face_uvs[j]
                if aj is None or bj is None:
                    continue
                if ((ai - aj).length_squared < eps_sq and
                        (bi - bj).length_squared < eps_sq):
                    union(fi, fj)

    islands_map = {}
    for f in bm.faces:
        r = find(f.index)
        islands_map.setdefault(r, set()).add(f.index)

    return list(islands_map.values())


# ---------------------------------------------------------------------------
# Core: tessellate face UV thành tam giác
# ---------------------------------------------------------------------------
def _face_uv_triangles(face, uv_layer):
    """Trả về list các tam giác UV (mỗi tam giác = tuple 3 Vector2D)."""
    uvs = [l[uv_layer].uv.copy() for l in face.loops]
    n = len(uvs)
    if n < 3:
        return []
    if n == 3:
        return [(uvs[0], uvs[1], uvs[2])]
    if n == 4:
        # Fan-triangulation đủ cho quad lồi/lõm điển hình.
        return [(uvs[0], uvs[1], uvs[2]), (uvs[0], uvs[2], uvs[3])]
    tris_idx = tessellate_polygon([uvs])
    return [(uvs[a], uvs[b], uvs[c]) for a, b, c in tris_idx]


# ---------------------------------------------------------------------------
# Core: triangle-triangle overlap 2D (có vùng giao > 0)
# ---------------------------------------------------------------------------
def _triangle_overlap_2d(t1, t2, eps=GEOM_EPS):
    """
    True khi 2 tam giác có diện tích giao > 0. Tiếp xúc cạnh / đỉnh
    KHÔNG coi là overlap (tránh false-positive cho island packed sát).
    """
    a, b, c = t1
    p, q, r = t2

    # AABB rejection (treat touching as separate).
    if (max(a.x, b.x, c.x) <= min(p.x, q.x, r.x) + eps or
            min(a.x, b.x, c.x) >= max(p.x, q.x, r.x) - eps or
            max(a.y, b.y, c.y) <= min(p.y, q.y, r.y) + eps or
            min(a.y, b.y, c.y) >= max(p.y, q.y, r.y) - eps):
        return False

    # Centroid bắt được trường hợp 1 tam giác hoàn toàn nằm trong tam
    # giác kia (vertex test có thể miss nếu mọi đỉnh nằm trên cạnh).
    c1 = (a + b + c) / 3.0
    if intersect_point_tri_2d(c1, p, q, r):
        return True
    c2 = (p + q + r) / 3.0
    if intersect_point_tri_2d(c2, a, b, c):
        return True

    # Đỉnh nằm STRICT bên trong (== 1, không tính trên cạnh = -1).
    for v in (a, b, c):
        if intersect_point_tri_2d(v, p, q, r) == 1:
            return True
    for v in (p, q, r):
        if intersect_point_tri_2d(v, a, b, c) == 1:
            return True

    # Edge crossing thực sự: giao điểm không phải tại endpoint.
    eps_sq = eps * eps
    for e1a, e1b in ((a, b), (b, c), (c, a)):
        for e2a, e2b in ((p, q), (q, r), (r, p)):
            pt = intersect_line_line_2d(e1a, e1b, e2a, e2b)
            if pt is None:
                continue
            touch = False
            for ep in (e1a, e1b, e2a, e2b):
                if (pt - ep).length_squared < eps_sq:
                    touch = True
                    break
            if not touch:
                return True

    return False


# ---------------------------------------------------------------------------
# Public entry-point (pure check)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Pure check, không có side-effect.

    Returns
    -------
    list[int] | None
        - List face index thuộc các UV Island bị overlap (rỗng = sạch).
        - None nếu obj không hợp lệ.
    """
    if obj is None or obj.type != 'MESH' or obj.data is None:
        return None

    me = obj.data
    if not me.uv_layers or len(me.polygons) < 2:
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
        uv_layer = bm.loops.layers.uv.active
        if uv_layer is None:
            return []

        islands = _build_uv_islands(bm, uv_layer)
        if len(islands) < 2:
            return []

        # Tessellate + cache AABB cho từng island.
        island_data = []
        for faces in islands:
            tris = []
            xs, ys = [], []
            for fi in faces:
                f = bm.faces[fi]
                for tri in _face_uv_triangles(f, uv_layer):
                    tris.append(tri)
                    for v in tri:
                        xs.append(v.x)
                        ys.append(v.y)
            if tris:
                island_data.append((faces, tris, (min(xs), min(ys), max(xs), max(ys))))

        # So sánh pairwise với AABB rejection.
        bad_islands = set()
        n = len(island_data)
        for i in range(n):
            faces_i, tris_i, (xi0, yi0, xi1, yi1) = island_data[i]
            for j in range(i + 1, n):
                faces_j, tris_j, (xj0, yj0, xj1, yj1) = island_data[j]
                if (xi1 <= xj0 + GEOM_EPS or xj1 <= xi0 + GEOM_EPS or
                        yi1 <= yj0 + GEOM_EPS or yj1 <= yi0 + GEOM_EPS):
                    continue
                overlap = False
                for ta in tris_i:
                    if overlap:
                        break
                    for tb in tris_j:
                        if _triangle_overlap_2d(ta, tb):
                            overlap = True
                            break
                if overlap:
                    bad_islands.add(i)
                    bad_islands.add(j)

        bad_faces = set()
        for idx in bad_islands:
            bad_faces.update(island_data[idx][0])
        return sorted(bad_faces)
    finally:
        if owned:
            bm.free()


# ===========================================================================
# Workflow: highlight bad UV islands
# ===========================================================================

def _set_uv_shell_selection(bm, uv_layer, bad_face_set):
    """
    ADD UV selection vào các loop thuộc bad_face_set. KHÔNG đụng loop
    của các face khác (kể cả set về False) - các UV shell không overlap
    được giữ nguyên trạng thái selection trước đó.

    Tương thích cả 2 API:
    - Blender < 3.5: BMLoopUV có .select / .select_edge.
    - Blender >= 3.5: UV selection lưu dưới dạng bool layer trên loops.
      Tên layer theo convention ".vs.<uv_name>" (vertex) và ".es.<uv_name>"
      (edge). Layer được tự tạo nếu chưa có.
    """
    if uv_layer is None or not bm.faces or not bad_face_set:
        return False

    bm.faces.ensure_lookup_table()
    n_faces = len(bm.faces)

    # Probe API cũ.
    use_old_api = False
    try:
        _ = bm.faces[0].loops[0][uv_layer].select
        use_old_api = True
    except AttributeError:
        use_old_api = False

    if use_old_api:
        for fi in bad_face_set:
            if fi < 0 or fi >= n_faces:
                continue
            for l in bm.faces[fi].loops:
                lu = l[uv_layer]
                lu.select = True
                try:
                    lu.select_edge = True
                except AttributeError:
                    pass
        return True

    # API mới (Blender 3.5+): bool layers.
    uv_name = uv_layer.name
    sel_vert = bm.loops.layers.bool.get(f".vs.{uv_name}")
    if sel_vert is None:
        try:
            sel_vert = bm.loops.layers.bool.new(f".vs.{uv_name}")
        except (ValueError, RuntimeError):
            return False

    sel_edge = bm.loops.layers.bool.get(f".es.{uv_name}")
    if sel_edge is None:
        try:
            sel_edge = bm.loops.layers.bool.new(f".es.{uv_name}")
        except (ValueError, RuntimeError):
            sel_edge = None

    for fi in bad_face_set:
        if fi < 0 or fi >= n_faces:
            continue
        for l in bm.faces[fi].loops:
            l[sel_vert] = True
            if sel_edge is not None:
                l[sel_edge] = True

    return True


def _popup(message, title="Overlap UV", icon='INFO'):
    """popup_menu 1 dòng, non-blocking. Bỏ qua nếu context không hỗ trợ."""
    def draw(self, context):
        self.layout.label(text=message)
    try:
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)
    except (RuntimeError, AttributeError):
        pass


def _switch_to_uv_editing_workspace():
    """Đổi workspace hiện tại sang 'UV Editing' nếu tồn tại."""
    ws = bpy.data.workspaces.get('UV Editing')
    if ws is None:
        return False
    win = bpy.context.window
    if win is None:
        return False
    try:
        win.workspace = ws
        return True
    except (TypeError, AttributeError):
        return False


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs):
    """
    - Multi-object: select tất cả object lỗi + popup "chỉ nên check từng object".
    - Single object: Edit Mode + UV Editing workspace + select UV Island lỗi.

    Returns
    -------
    dict[str, list[int]] | None
    """
    if not objs:
        return None

    valid_objs = [
        o for o in objs
        if o is not None and o.type == 'MESH' and o.data is not None
    ]
    if not valid_objs:
        return None

    # Đảm bảo Object Mode để filter / set selection.
    if bpy.context.mode != 'OBJECT':
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            pass

    # Chạy check trên từng obj.
    issues = {}
    for obj in valid_objs:
        result = check_object(obj)
        if result:
            issues[obj.name] = result

    if not issues:
        return {}

    # ===== MULTI-OBJECT =====
    if len(valid_objs) > 1:
        try:
            bpy.ops.object.select_all(action='DESELECT')
        except RuntimeError:
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

        _popup(
            f"{len(bad_objs)} object có Overlap UV. Chỉ nên check từng object.",
            title="Overlap UV",
            icon='ERROR',
        )
        return issues

    # ===== SINGLE OBJECT =====
    obj = valid_objs[0]

    # Active obj phải là obj này để vào Edit Mode trên nó.
    try:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
    except (RuntimeError, ReferenceError):
        return issues

    # Edit Mode bắt buộc để UV selection nhìn thấy + manipulate.
    if obj.mode != 'EDIT':
        try:
            bpy.ops.object.mode_set(mode='EDIT')
        except RuntimeError:
            return issues

    bad_set = set(issues[obj.name])
    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()
    n_faces = len(bm.faces)
    uv_layer = bm.loops.layers.uv.active

    # ADDITIVELY select bad faces ở MESH side. KHÔNG deselect các face
    # khác - selection cũ của user được giữ nguyên. Việc select bad
    # face ở mesh đảm bảo UV editor hiển thị UV của chúng kể cả khi
    # sync OFF (sync OFF chỉ show UV của face đang select trong mesh).
    for fi in bad_set:
        if 0 <= fi < n_faces:
            bm.faces[fi].select = True
    bm.select_flush_mode()

    # ADDITIVELY set UV loop selection - chỉ đánh dấu trên loop của bad
    # face, UV shell khác giữ nguyên (sync OFF cần cái này, sync ON tự
    # sync từ mesh face select ở trên).
    _set_uv_shell_selection(bm, uv_layer, bad_set)

    bmesh.update_edit_mesh(obj.data)

    # Đổi workspace sang 'UV Editing' để user thấy ngay UV bị overlap.
    _switch_to_uv_editing_workspace()

    return issues


# ---------------------------------------------------------------------------
# Standalone debug
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _objs = [o for o in bpy.context.selected_objects if o.type == 'MESH']
    _result = check_and_highlight(_objs)
    if _result is None:
        print("[OverlapUV] Không có mesh hợp lệ trong selection.")
    elif not _result:
        print(f"[OverlapUV] {len(_objs)} mesh: tất cả sạch.")
    else:
        total = sum(len(v) for v in _result.values())
        print(f"[OverlapUV] {total} overlap face(s) trên {len(_result)} mesh:")
        for name, idxs in _result.items():
            preview = idxs if len(idxs) <= 20 else idxs[:20] + ['...']
            print(f"  - {name}: {preview}")
