"""
    Chức năng:
    - Xác định 2 vertex đầu/cuối của selection (dùng khi selection là 1 dãy cạnh/vertex).
    - Trả về thứ tự cạnh (edge order) và vertex (vertex order) dựa trên selection.
    - Gom các edge liên tiếp thành nhóm (list of list), ví dụ các đoạn edge liên tiếp.
    - Trả về cạnh đối diện với selection hiện tại trên polygon face.
    - Trả về vertex đầu/cuối (theo hướng cạnh) dựa trên world space position.
"""

import maya.cmds as cmds
import re
import math


from selection_utils import SelectionUtils
sels = SelectionUtils.getAllSel()

class EdgeUtils:
    @staticmethod
    def isolateFirstEdge(sel):
        """
        Xác định 2 vertex đầu/cuối của selection (dùng khi selection là 1 dãy cạnh/vertex).
        """
        vertStartandEnd = []
        for s in sel:
            cmds.select(s, r=True)
            vert = cmds.ls(cmds.polyListComponentConversion(s, fe=1, tv=1), fl=1)
            if len(vert) < 2:
                continue
            V1, V2 = vert[0], vert[1]
            edgeV1 = cmds.ls(cmds.polyListComponentConversion(V1, fv=1, te=1), fl=1)
            inter1 = list(set(sel) & set(edgeV1))
            if len(inter1) == 1:
                vertStartandEnd.append(V1)
            edgeV2 = cmds.ls(cmds.polyListComponentConversion(V2, fv=1, te=1), fl=1)
            inter2 = list(set(sel) & set(edgeV2))
            if len(inter2) == 1:
                vertStartandEnd.append(V2)
        return vertStartandEnd


    @staticmethod
    def getOrderedSelection():
        """
        Trả về thứ tự cạnh (edge order) và vertex (vertex order) dựa trên selection.
        """
        sel = SelectionUtils.getAllSel()
        orSel = sel[:]
        allVert = cmds.ls(cmds.polyListComponentConversion(sel, tv=1), fl=1)
        vertStartandEnd = EdgeUtils.isolateFirstEdge(sel)
        if not vertStartandEnd:
            vertStartandEnd = EdgeUtils.isolateFirstEdge(orSel[:-1])
        if not vertStartandEnd:
            return [], []
        vertOrder = [vertStartandEnd[0]]
        edgeOrder = []
        for _ in range(len(sel)):
            edgeV = cmds.ls(cmds.polyListComponentConversion(vertOrder[-1], fv=1, te=1), fl=1)
            inter = list(set(sel) & set(edgeV))
            inter = [i for i in inter if i not in edgeOrder]
            if len(inter) == 1:
                edgeOrder.append(inter[0])
                sel = [x for x in sel if x != inter[0]]
                edgeVerts = cmds.ls(cmds.polyListComponentConversion(inter, fe=1, tv=1), fl=1)
                bl = list(set(edgeVerts) - set(vertOrder))
                if bl:
                    vertOrder.append(bl[0])
        cmds.select(orSel)
        return edgeOrder, vertOrder


    @staticmethod
    def getEdgeGroup():
        """
        Gom các edge liên tiếp thành nhóm (list of list), ví dụ các đoạn edge liên tiếp.
        """
        selEdges = SelectionUtils.getAllSel()
        if not selEdges:
            return []
        trans = selEdges[0].split(".")[0]
        e2vInfos = cmds.polyInfo(selEdges, ev=True)
        e2vDict = {}
        for info in e2vInfos:
            evList = [int(i) for i in re.findall(r'\d+', info)]
            e2vDict[evList[0]] = evList[1:]
        fEdges = []
        while e2vDict:
            startEdge, startVtxs = e2vDict.popitem()
            edgesGrp = [startEdge]
            for vtx in startVtxs:
                curVtx = vtx
                num = 0
                while True:
                    nextEdges = [k for k, v in e2vDict.items() if curVtx in v]
                    if nextEdges:
                        ne = nextEdges[0]
                        if num == 0:
                            edgesGrp.append(ne)
                        else:
                            edgesGrp.insert(0, ne)
                        curVtx = [v for v in e2vDict[ne] if v != curVtx][0]
                        e2vDict.pop(ne)
                    else:
                        break
                    num += 1
            fEdges.append(edgesGrp)
        retEdges = []
        for group in fEdges:
            retEdges.append([f"{trans}.e[{x}]" for x in group])
        return retEdges


    @staticmethod
    def getOppositeEdge():
        """
        Trả về cạnh đối diện với selection hiện tại trên polygon face.
        """
        sel = SelectionUtils.getAllSel()
        V1 = cmds.ls(cmds.polyListComponentConversion(sel, tv=1), fl=1)
        E1 = cmds.ls(cmds.polyListComponentConversion(V1, te=1), fl=1)
        V2 = cmds.ls(cmds.polyListComponentConversion(E1, tv=1), fl=1)
        facelist = cmds.ls(cmds.polyListComponentConversion(sel, tf=1), fl=1)
        innerFace = []
        for f in facelist:
            toVert = cmds.ls(cmds.polyListComponentConversion(f, tv=1), fl=1)
            if len(toVert) == 6:
                innerFace.append(f)
        if len(innerFace) != 1:
            return []
        F1 = cmds.ls(cmds.polyListComponentConversion(innerFace[0], tv=1), fl=1)
        finalVert = list(set(F1) - set(V2))
        oppositeEdge = cmds.ls(cmds.polyListComponentConversion(finalVert, te=1, internal=1), fl=1)
        return oppositeEdge



    @staticmethod
    def getEdgeDirection(edge):
        """
        Trả về vertex đầu/cuối (theo hướng cạnh) dựa trên world space position.
        """
        # Parse edge number
        edgeNumber = int(edge.split("[")[-1].split("]")[0])
        verts = cmds.ls(cmds.polyListComponentConversion(edge, fe=1, tv=1), fl=1)
        if len(verts) != 2:
            return verts
        vpos = [cmds.xform(v, q=True, ws=True, t=True) for v in verts]
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(vpos[0], vpos[1])))

        # Find direction (by splitting or calculating by world position)
        # Ở đây có thể dùng logic: chọn một vertex làm đầu, so sánh vị trí hai điểm
        # Giả sử bạn muốn trả về [đầu, cuối] dựa trên thứ tự tọa độ xyz
        if vpos[0][0] < vpos[1][0]:
            return [verts[0], verts[1]]
        else:
            return [verts[1], verts[0]]
