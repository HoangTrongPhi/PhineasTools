import maya.cmds as cmds

# =========================
# Nhóm thao tác crease & smooth
# =========================

def cp_qsmooth(level=1):
    """
    Smooth mesh nhanh (subdivision).
    """
    sel = cmds.ls(selection=True, long=True)
    for obj in sel:
        cmds.polySmooth(obj, divisions=level)

def cp_shape_shifter(shape_type='sphere'):
    """
    Đổi hình dạng mesh: 'sphere', 'cube', v.v...
    """
    sel = cmds.ls(selection=True, long=True)
    for obj in sel:
        if shape_type == 'sphere':
            cmds.polySphere(obj)
        elif shape_type == 'cube':
            cmds.polyCube(obj)
        # Có thể mở rộng thêm

def cp_goz():
    """
    Gửi mesh sang Zbrush qua GoZ (giả lập).
    """
    # Không có API chuẩn, chỉ placeholder
    pass

def cp_get_goz():
    """
    Nhận mesh từ Zbrush qua GoZ (giả lập).
    """
    # Không có API chuẩn, chỉ placeholder
    pass

