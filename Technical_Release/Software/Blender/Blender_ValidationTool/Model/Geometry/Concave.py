# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Geometry/Concave.py

Check Concave Faces - module thuộc tầng Model của hệ thống validation.

Một polygon là convex khi tất cả các đỉnh đều "rẽ cùng một hướng" khi đi
dọc theo chu vi. Nếu có bất kỳ đỉnh nào "rẽ ngược chiều" thì polygon đó
là concave.

Lưu ý: Tam giác KHÔNG BAO GIỜ concave. Nếu mesh đã bị triangulate
(import từ FBX/GLTF/OBJ, hoặc đã chạy Triangulate modifier) thì hàm
này sẽ không tìm thấy concave face nào. Hãy dissolve về n-gon trước.

Giao tiếp với framework (Config.CHECK_FUNCTIONS["geo_concave"]):

    check_object(obj) -> list[int] | None
        - list rỗng []         : mesh sạch.
        - list các face index  : các face bị concave.
        - None                 : obj không hợp lệ -> framework skip object.

Module này là PURE CHECK:
    - Chỉ đọc bmesh, không sửa mesh.
    - Không select face, không đổi mode, không in log lan man.
    - Việc select/highlight/report do tầng trên (RunSingle/RunAll/UI) lo,
      dựa vào list index mà hàm trả về.
"""

import bpy
import bmesh


# Ngưỡng tương đối: dot/(|e1|*|e2|) ~ sin(angle).
# 1e-6 ~ 0.00006 độ, đủ chặt để bỏ qua mấy điểm gần thẳng hàng do float noise.
EPS = 1e-6


# ---------------------------------------------------------------------------
# Core algorithm
# ---------------------------------------------------------------------------
def is_face_concave(face):
    """
    Kiểm tra một bmesh face có concave không.

    Đi dọc theo chu vi, tại mỗi đỉnh tính cross(edge_vào, edge_ra) rồi
    dot với face.normal để biết "rẽ trái hay phải". Nếu chu vi đổi dấu
    giữa chừng -> concave.
    """
    verts = [v.co for v in face.verts]   # không cần .copy(), chỉ đọc
    n = len(verts)
    if n < 4:
        # Tam giác (hoặc ít hơn) không thể concave.
        return False

    normal = face.normal
    sign = None

    for i in range(n):
        v0 = verts[(i - 1) % n]
        v1 = verts[i]
        v2 = verts[(i + 1) % n]
        edge1 = v1 - v0
        edge2 = v2 - v1
        cross = edge1.cross(edge2)
        dot = cross.dot(normal)

        # Ngưỡng tương đối theo độ dài cạnh -> không phụ thuộc scale mesh.
        denom = edge1.length * edge2.length
        if denom < 1e-12:
            continue  # cạnh suy biến (2 đỉnh trùng nhau)
        if abs(dot) / denom < EPS:
            continue  # 3 điểm gần như thẳng hàng -> bỏ qua

        current_sign = dot > 0
        if sign is None:
            sign = current_sign
        elif sign != current_sign:
            return True

    return False


# ---------------------------------------------------------------------------
# Public entry-point (đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Validation entry-point.

    Parameters
    ----------
    obj : bpy.types.Object | None
        Object cần check.

    Returns
    -------
    list[int] | None
        - List index các face bị concave (rỗng nghĩa là sạch).
        - None nếu obj không hợp lệ (None / không phải mesh / không có data).
    """
    # ---- Validate input ----
    if obj is None or obj.type != 'MESH' or obj.data is None:
        return None

    me = obj.data

    # Mesh không có face -> trivially sạch.
    if len(me.polygons) == 0:
        return []

    # ---- Lấy bmesh: hỗ trợ cả Edit Mode lẫn Object Mode ----
    # - Edit Mode: dùng bmesh sống của Blender (from_edit_mesh).
    # - Object Mode: tạo bmesh tạm, NHỚ free() sau khi xong.
    if obj.mode == 'EDIT':
        bm = bmesh.from_edit_mesh(me)
        owned = False
    else:
        bm = bmesh.new()
        bm.from_mesh(me)
        owned = True

    try:
        bm.faces.ensure_lookup_table()
        return [f.index for f in bm.faces if is_face_concave(f)]
    finally:
        if owned:
            bm.free()


# ---------------------------------------------------------------------------
# Standalone debug: chỉ chạy khi mở trực tiếp trong Text Editor + Run Script.
# KHÔNG chạy khi Blender load addon (lúc đó __name__ != "__main__").
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _obj = bpy.context.active_object
    _result = check_object(_obj)
    if _result is None:
        print("[Concave] Object không hợp lệ.")
    else:
        print(f"[Concave] '{_obj.name}': {len(_result)} concave face(s).")
        if _result:
            preview = _result if len(_result) <= 50 else _result[:50] + ['...']
            print(f"          indices: {preview}")