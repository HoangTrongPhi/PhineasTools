import maya.cmds as cmds

# =========================
# Nhóm Extension1 - thao tác crease nâng cao
# =========================

def sp_smart_lvl(level=1):
    """
    Set crease level thông minh cho selection.
    """
    sel = cmds.ls(selection=True, flatten=True)
    for edge in sel:
        cmds.setAttr(edge + ".crease", level)

def sp_fast_crease(level=1):
    """
    Thêm crease nhanh cho các cạnh đang chọn.
    """
    sel = cmds.filterExpand(selectionMask=32)  # Chỉ lấy edge
    if not sel:
        cmds.warning("Chưa chọn cạnh nào! Vui lòng chọn edge trước khi dùng lệnh này.")
        return
    for edge in sel:
        try:
            cmds.polyCrease(edge, value=level)
        except Exception as e:
            cmds.warning(f"Lỗi polyCrease ở cạnh {edge}: {e}")

def sp_no_crease():
    """
    Xoá crease trên các cạnh đã chọn.
    """
    sel = cmds.ls(selection=True, flatten=True)
    for edge in sel:
        cmds.polyCrease(edge, value=0)

def sp_smooth_os(level=1):
    """
    Smooth object nhanh (chia lưới).
    """
    sel = cmds.ls(selection=True, long=True)
    for obj in sel:
        cmds.polySmooth(obj, divisions=level)

def smooth_sg(level=1):
    """
    Smooth selection group (chung logic với sp_smooth_os).
    """
    sp_smooth_os(level=level)

def sp_crease_preset(preset='medium'):
    """
    Gán crease preset (thấp, vừa, cao) cho cạnh đã chọn.
    """
    value = 1
    if preset == 'low':
        value = 0.33
    elif preset == 'medium':
        value = 0.66
    elif preset == 'high':
        value = 1
    sel = cmds.ls(selection=True, flatten=True)
    for edge in sel:
        cmds.polyCrease(edge, value=value)

def sp_level(level=1):
    """
    Điều chỉnh crease level trực tiếp.
    """
    sel = cmds.ls(selection=True, flatten=True)
    for edge in sel:
        cmds.setAttr(edge + ".crease", level)

def sp_physical_crease(width=0.05):
    """
    Chuyển crease thành chamfer thực (thực thể hình học).
    """
    sel = cmds.ls(selection=True, flatten=True)
    for edge in sel:
        cmds.polyBevel3(edge, fraction=width, segments=1)

def sp_show_crease_ed():
    """
    Chọn & hiển thị các cạnh có crease (giá trị > 0).
    """
    all_edges = cmds.ls(type='mesh', flatten=True)
    crease_edges = []
    for edge in all_edges:
        val = cmds.getAttr(edge + ".crease")
        if val and val[0] > 0:
            crease_edges.append(edge)
    cmds.select(crease_edges)

