# -*- coding: utf-8 -*-
"""
    Chức năng:
    - Lấy tên Transform hoặc Shape object đang chọn.
    - Lấy danh sách object/component hiện đang được chọn (full path).
    - Chọn các vertex trong phạm vi bán kính (dùng soft selection).
    - Tìm vertex gần nhất với selection đầu tiên, trong phạm vi threshold (world space).
    - Tách số nguyên nằm trong dấu ngoặc vuông của chuỗi.
    - Hiển thị thông báo (console), mô phỏng chức năng inViewMessage trong Maya.
    - Các hàm này sử dụng Maya API để truy xuất thông tin selection và thực hiện các thao tác trên vertex.
"""

import maya.cmds as cmds
import maya.api.OpenMaya as om
import math
from functools import reduce

class SelectionUtils:
    @staticmethod
    def getSandT(type="t"):
        """
        Lấy tên Transform hoặc Shape object đang chọn.
        type='t' trả về transform, type='s' trả về shape
        """
        outVal = ""
        try:
            selection = om.MGlobal.getActiveSelectionList()
            for i in range(selection.length()):
                dagPath = selection.getDagPath(i)
                dagName = dagPath.fullPathName()
                if len(dagName.split("|")) > 2:
                    if type == "s":
                        outVal = dagName.split("|")[-1]
                    elif type == "t":
                        outVal = dagName.split("|")[-2]
                else:
                    outVal = dagName.split("|")[-1]
        except Exception:
            pass
        return outVal


    @staticmethod
    def getAllSel():
        """
        Trả về danh sách object/component hiện đang được chọn (full path)
        """
        sel = om.MGlobal.getActiveSelectionList()
        names = []
        for i in range(sel.length()):
            names.append(sel.getSelectionStrings(i)[0])
        # cmds.ls đảm bảo trả về dạng list string đúng format component
        return cmds.ls(names, fl=1)


    @staticmethod
    def RadiusSelect(radius):
        """
        Chọn các vertex trong phạm vi bán kính (dùng soft selection).
        """
        cmds.softSelect(sse=1, ssd=radius * 100)
        softSelection = om.MRichSelection()
        om.MGlobal.getRichSelection(softSelection)
        selection = softSelection.getSelection()
        vertsList = []
        for i in range(selection.length()):
            dagPath, component = selection.getComponent(i)
            if component.hasFn(om.MFn.kMeshVertComponent):
                fnComp = om.MFnSingleIndexedComponent(component)
                for j in range(fnComp.elementCount):
                    vertsList.append('%s.vtx[%d]' % (dagPath.fullPathName(), fnComp.element(j)))
        cmds.softSelect(sse=0)
        return vertsList

    @staticmethod
    def getClosestVert(threshold):
        """
        Tìm vertex gần nhất với selection đầu tiên, trong phạm vi threshold (world space).
        """
        sel = SelectionUtils.getAllSel()
        if not sel:
            return ""
        cmds.select(SelectionUtils.RadiusSelect(threshold))
        allVerts = SelectionUtils.getAllSel()
        if sel[0] in allVerts:
            allVerts.remove(sel[0])

        V1 = cmds.xform(sel[0], q=True, ws=True, t=True)
        distlist = {}
        for V in allVerts:
            V2 = cmds.xform(V, q=True, ws=True, t=True)
            # Tính khoảng cách Euclid
            distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(V1, V2)))
            if distance < threshold:
                distlist[V] = distance

        if not distlist:
            return ""
        closestVert = min(distlist, key=distlist.get)
        return closestVert
