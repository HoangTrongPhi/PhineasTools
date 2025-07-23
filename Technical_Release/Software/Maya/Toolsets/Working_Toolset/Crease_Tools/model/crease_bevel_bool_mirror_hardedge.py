import maya.cmds as cmds

# =========================
# Nhóm thao tác với crease/bevel/bool/mirror/hard edge
# =========================

def cp_hbevel(bevel_width=0.1, bevel_segments=1):
    """
    Bevel các cạnh cứng đã chọn.
    """
    sel_edges = cmds.ls(selection=True, flatten=True)
    if not sel_edges:
        cmds.warning("Chọn các cạnh để bevel.")
        return
    # Bevel edges
    cmds.polyBevel3(sel_edges, fraction=bevel_width, segments=bevel_segments)

def cp_hedge_sel():
    """
    Chọn các cạnh cứng (hard edges) trong selection.
    """
    sel_objs = cmds.ls(selection=True, long=True)
    for obj in sel_objs:
        edges = cmds.polyListComponentConversion(obj, toEdge=True)
        hard_edges = []
        for edge in edges:
            if cmds.polySoftEdge(edge, query=True, angle=True)[0] == 0.0:
                hard_edges.append(edge)
        if hard_edges:
            cmds.select(hard_edges, add=True)

def cp_hard_display():
    """
    Hiển thị rõ hard edge trong viewport (không thực sự đổi màu).
    """
    cmds.displayColor("hardEdge", 17, dormant=True)

def cp_panel_bool():
    """
    Boolean giữa 2 đối tượng (Difference)
    """
    sel = cmds.ls(selection=True)
    if len(sel) < 2:
        cmds.warning("Chọn ít nhất 2 mesh để Boolean.")
        return
    cmds.polyCBoolOp(sel[0], sel[1], op=2, ch=1)  # op=2: difference

def cp_display_bool():
    """
    Hiển thị trạng thái boolean hoặc bật/tắt bool history (giả lập).
    """
    # Không có API chuẩn cho trạng thái này - placeholder
    pass

def cp_keep_bool():
    """
    Duy trì boolean khi tách object (giữ lại history).
    """
    # Đảm bảo boolean vẫn còn khi detach/separate - placeholder
    pass

def cp_instance_bool():
    """
    Tạo instance mesh với boolean (giữ lại quan hệ).
    """
    sel = cmds.ls(selection=True)
    if len(sel) < 2:
        cmds.warning("Chọn ít nhất 2 mesh để Instance Boolean.")
        return
    result = cmds.instance(sel[0])
    cmds.polyCBoolOp(result[0], sel[1], op=2, ch=1)  # op=2: difference

def cp_bak_that_nod(obj):
    """
    Bake (lưu) node history thành mesh tĩnh.
    """
    dup = cmds.duplicate(obj, name=obj + "_baked")[0]
    cmds.delete(dup, constructionHistory=True)
    return dup

def cp_nod_baker():
    """
    Tìm toàn bộ mesh và bake node.
    """
    meshes = cmds.ls(type='mesh', long=True)
    for mesh in meshes:
        trans = cmds.listRelatives(mesh, parent=True, fullPath=True)
        if trans:
            cp_bak_that_nod(trans[0])

def cp_mirror(axis='x'):
    """
    Mirror mesh qua trục (x/y/z).
    """
    sel = cmds.ls(selection=True, long=True)
    if not sel:
        cmds.warning("Chọn đối tượng để Mirror.")
        return
    for obj in sel:
        if axis == 'x':
            scale = [-1, 1, 1]
        elif axis == 'y':
            scale = [1, -1, 1]
        else:
            scale = [1, 1, -1]
        dup = cmds.duplicate(obj)[0]
        cmds.setAttr(dup + ".scale", *scale, type="double3")

def cp_mesh_slicer(plane='yz'):
    """
    Slice (cắt) mesh qua mặt phẳng (xy/yz/xz).
    """
    sel = cmds.ls(selection=True, long=True)
    if not sel:
        cmds.warning("Chọn đối tượng để slice.")
        return
    for obj in sel:
        cmds.polyCut(obj, cutPlane=plane)

