"""
    Chức năng:
    - Mở rộng vùng chọn face hiện tại.
    - Tạo vùng border giữa hai face và điền các face bên trong.

"""


import maya.cmds as cmds
import maya.mel as mel

# --- Nhóm các hàm tiện ích liên quan selection ---
def get_all_sel():
    """Lấy toàn bộ selection dưới dạng list full path."""
    sel = cmds.ls(selection=True, flatten=True)
    return sel if sel else []

def get_sandt(type_="t"):
    """Lấy tên transform hoặc shape object đang chọn."""
    sel = cmds.ls(selection=True, long=True)
    if not sel:
        return ""
    split = sel[0].split('|')
    if len(split) < 2:
        return split[-1]
    return split[-1] if type_ == "s" else split[-2]

# --- Phần thao tác với mặt (face) ---
class FaceFillTools:
    @staticmethod
    def grow_face():
        """Mở rộng vùng selection face hiện tại thêm một lần."""
        sel = get_all_sel()
        if not sel:
            return
        cmds.ConvertSelectionToContainedEdges()
        cmds.ConvertSelectionToEdges()
        FaceFillTools.grow_ring()  # Phụ thuộc vào grow_ring
        cmds.ConvertSelectionToFaces()

    @staticmethod
    def grow_ring():
        """Mở rộng selection theo edge ring."""
        cmds.polySelectConstraint(m=2, t=0x8000, w=1)
        mel.eval('PolySelectTraverse 2')  # sang edge ring
        cmds.polySelectConstraint(disable=True)

    @staticmethod
    def face_border_sel():
        """Chọn border giữa 2 faces, đánh dấu vùng fill."""
        chkFace = cmds.filterExpand(sm=34, ex=True)
        if chkFace is None:
            return

        # Yêu cầu đúng 2 face được chọn
        sel = get_all_sel()
        if len(sel) != 2:
            return

        trans = get_sandt("t")
        s1faces = [sel[0]]
        s2faces = [sel[1]]
        cmds.progressWindow(title='Face Fill...', progress=0, max=100, status='Processing...')
        interFaces = []

        for i in range(100):
            cmds.progressWindow(edit=True, progress=i, status='Calculating...')
            cmds.select(s1faces)
            FaceFillTools.grow_face()
            s1faces = get_all_sel()
            cmds.select(s2faces)
            FaceFillTools.grow_face()
            s2faces = get_all_sel()
            interFaces = list(set(s1faces) & set(s2faces))
            if len(interFaces) == 2:
                break
        cmds.progressWindow(endProgress=1)

        # Xử lý tạo border
        faceBorder = []
        for i in range(2):
            mel.eval('polySelectSp -loop {} {};'.format(sel[i], interFaces[0]))
            faceBorder += get_all_sel()
            mel.eval('polySelectSp -loop {} {};'.format(sel[i], interFaces[1]))
            faceBorder += get_all_sel()
        faceBorder = list(set(faceBorder))

        cmds.select(clear=True)
        # Lấy vertex của từng face
        s1verts = cmds.ls(cmds.polyListComponentConversion(sel[0], ff=1, tv=1), fl=1)
        s2verts = cmds.ls(cmds.polyListComponentConversion(sel[1], ff=1, tv=1), fl=1)
        if not s1verts or not s2verts:
            return
        sv1 = int(s1verts[0].split('[')[-1][:-1])  # index đầu tiên của face 1
        sv2 = int(s2verts[0].split('[')[-1][:-1])  # index đầu tiên của face 2

        # Tìm đường đi ngắn nhất giữa hai vertex trên cùng một mesh
        shortEdge = cmds.polySelect(trans, shortestEdgePath=(sv1, sv2))
        shortVert = cmds.ls(cmds.polyListComponentConversion(get_all_sel(), fe=1, tv=1), fl=1)

        combinedVerts = cmds.ls(cmds.polyListComponentConversion(faceBorder, ff=1, tv=1), fl=1)
        vertBool = list(set(shortVert) - set(combinedVerts))

        # Chuyển vertex nội bộ sang face
        internalFace = cmds.ls(cmds.polyListComponentConversion(vertBool, fv=1, tf=1), fl=1)
        borderBool = list(set(internalFace) - set(faceBorder))
        cmds.select(borderBool)
        if not borderBool:
            cmds.select(faceBorder)
            return

        # Duyệt lấy các face bên trong border
        for _ in range(len(faceBorder) // 4):
            mel.eval('PolySelectTraverse 1;')
            borderInter = list(set(get_all_sel()) & set(faceBorder))
            borderSubs = list(set(get_all_sel()) - set(faceBorder))
            cmds.select(borderSubs)
            if len(borderInter) == len(faceBorder):
                finalFaces = list(set(borderSubs) | set(faceBorder))
                cmds.select(finalFaces)
                break


