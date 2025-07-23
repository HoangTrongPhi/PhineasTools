"""
   Chức năng:
    - Nối các edge loop đã chọn, hỗ trợ weld nếu cần
    - Cắt và nối các edge loop với nhau
    - Kết nối các edge với vertex
    - Biến edge loop thành đường thẳng
    - Làm phẳng các vertex theo mặt phẳng view
    - Chuyển đổi edge loop thành hình tròn hoặc đường cong
    - Chuyển đổi vertex thành đường cong hoặc hình tròn

"""




import maya.cmds as cmds
import maya.api.OpenMaya as om
import math


# Lấy danh sách selection hiện tại (object hoặc component)
def get_all_sel():
    sel = cmds.ls(sl=True, fl=True)
    return sel or []

# Kiểm tra và lấy edges đang chọn
def get_selected_edges():
    return cmds.filterExpand(sm=32, ex=True)

# Kiểm tra và lấy vertex đang chọn
def get_selected_vertices():
    return cmds.filterExpand(sm=31, ex=True)




#-------- Thao tác trên Edge Loop/Vertex --------
# Load edge loop vào biến HighEdges (trả về list hoặc None)
def load_edge_loop():
    edges = get_selected_edges()
    if not edges:
        cmds.warning("Only Edges/Edge Loops Supported")
        return None
    # Cập nhật UI nếu cần (ví dụ: cmds.textField ...)
    return edges

# Load một vertex vào slot (trả về tên vertex)
def load_vertex():
    vtx = get_selected_vertices()
    if not vtx or len(vtx) != 1:
        cmds.warning("Load Single Vertex in the slot.")
        return None
    return vtx[0]




# --------- Nhóm kết nối (Connect/Cut/Bridge...) -----
# Nối các edge loop đã chọn, hỗ trợ weld nếu cần
def cut_and_stitch(high_edges, low_edges, threshold=0.01, weld=True):
    # high_edges: list edge nguồn, low_edges: list edge đích
    if not high_edges or not low_edges:
        cmds.warning("Thiếu edge để nối.")
        return
    # Chỉ minh hoạ, chi tiết thao tác (dựa vào vector, tính toán vị trí, weld...) cần viết thêm
    for src, dst in zip(high_edges, low_edges):
        cmds.select([src, dst])
        try:
            cmds.polyConnectComponents()
        except:
            cmds.warning("Lỗi nối edge: {} - {}".format(src, dst))
    if weld:
        all_verts = cmds.ls(cmds.polyListComponentConversion(high_edges + low_edges, tv=True), fl=True)
        cmds.polyMergeVertex(all_verts, d=threshold)
    cmds.select(clear=True)

# Nối giữa 2 selection edge (bridge)
def dist_connect(sel):
    if len(sel) != 2:
        cmds.warning("Chọn đúng 2 edge.")
        return
    cmds.select(sel)
    try:
        cmds.polyConnectComponents()
    except:
        cmds.warning("Lỗi bridge edge.")


# Kết nối nhiều edge với vertex
def connect_to_vertex(vertex, edges):
    for edge in edges:
        cmds.select([vertex, edge])
        try:
            cmds.polyConnectComponents()
        except:
            cmds.warning(f"Lỗi nối {vertex} - {edge}")

# Biến edge loop thành đường thẳng
def straight_loop(edge_group):
    for edges in edge_group:
        verts = cmds.ls(cmds.polyListComponentConversion(edges, fe=True, tv=True), fl=True)
        if len(verts) < 2:
            continue
        # Tính vị trí đầu-cuối
        pos0 = cmds.pointPosition(verts[0], w=True)
        pos1 = cmds.pointPosition(verts[-1], w=True)
        for i, v in enumerate(verts[1:-1], 1):
            t = float(i) / (len(verts) - 1)
            interp = [pos0[j] + t * (pos1[j] - pos0[j]) for j in range(3)]
            cmds.xform(v, ws=True, t=interp)

# Làm phẳng các vertex theo mặt phẳng view
def view_planar(sel):
    if len(sel) < 2: return
    positions = [cmds.pointPosition(v, w=True) for v in sel]
    center = [sum(vals) / len(vals) for vals in zip(*positions)]
    # Đơn giản, di chuyển các điểm về trung tâm view trên mặt phẳng
    for v in sel:
        pos = cmds.pointPosition(v, w=True)
        planar_pos = list(pos)
        planar_pos[2] = center[2]  # làm phẳng theo trục Z
        cmds.xform(v, ws=True, t=planar_pos)





# --------chuyển đổi Loop/Vertex thành đường tròn, đường cong --------------
# Chuyển loop thành hình tròn (circle)
def circle(edge_group):
    for edges in edge_group:
        verts = cmds.ls(cmds.polyListComponentConversion(edges, fe=True, tv=True), fl=True)
        n = len(verts)
        if n < 3:
            continue
        positions = [cmds.pointPosition(v, w=True) for v in verts]
        center = [sum(vals)/n for vals in zip(*positions)]
        # Tính bán kính trung bình
        avg_radius = sum(math.dist(p, center) for p in positions) / n
        for i, v in enumerate(verts):
            angle = 2 * math.pi * i / n
            new_pos = [
                center[0] + avg_radius * math.cos(angle),
                center[1] + avg_radius * math.sin(angle),
                center[2]
            ]
            cmds.xform(v, ws=True, t=new_pos)
