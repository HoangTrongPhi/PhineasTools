"""
    Chức năng:
    - Chuyển đổi giữa các chế độ chọn (vertex, edge, face, shell) trong Maya.
"""


import maya.cmds as cmds
import maya.mel as mel

class SelectionModes:
    @staticmethod
    def get_transform_of_selection():
        """
        Trả về tên transform object đầu tiên trong selection (nếu có).
        Nếu selection là shape thì trả về cha transform.
        """
        sel = cmds.ls(selection=True, long=True)
        if not sel:
            return ""
        # Nếu là shape thì lấy cha transform, nếu là transform thì lấy luôn
        node = sel[0]
        node_type = cmds.nodeType(node)
        if node_type in ["mesh", "nurbsCurve", "nurbsSurface"]:
            parent = cmds.listRelatives(node, parent=True, fullPath=True)
            if parent:
                return parent[0]
            return ""
        else:
            return node

    @staticmethod
    def vertex_mode():
        """
        Chuyển sang chế độ chọn vertex cho object đang được chọn
        """
        sel = SelectionModes.get_transform_of_selection()
        if not sel:
            return
        mel.eval('resetPolySelectConstraint;')
        mel.eval(f'doMenuComponentSelection("{sel}", "vertex");')

    @staticmethod
    def edge_mode():
        """
        Chuyển sang chế độ chọn edge cho object đang được chọn
        """
        sel = SelectionModes.get_transform_of_selection()
        if not sel:
            return
        mel.eval('resetPolySelectConstraint;')
        mel.eval(f'doMenuComponentSelection("{sel}", "edge");')

    @staticmethod
    def border_mode():
        """
        Chuyển sang chế độ chọn border edge (vùng hở) cho object đang được chọn
        """
        sel = SelectionModes.get_transform_of_selection()
        if not sel:
            return
        SelectionModes.edge_mode()
        mel.eval('polySelectConstraint -m 2 -bo 1;')

    @staticmethod
    def face_mode():
        """
        Chuyển sang chế độ chọn face cho object đang được chọn
        """
        sel = SelectionModes.get_transform_of_selection()
        if not sel:
            return
        mel.eval('resetPolySelectConstraint;')
        mel.eval(f'doMenuComponentSelection("{sel}", "facet");')

    @staticmethod
    def shell_mode():
        """
        Chuyển sang chế độ chọn face shell cho object đang được chọn
        """
        sel = SelectionModes.get_transform_of_selection()
        if not sel:
            return
        SelectionModes.face_mode()
        # Chế độ shell phải dùng polySelectConstraint, cmds không hỗ trợ trực tiếp
        mel.eval('polySelectConstraint -sh 1;')
