"""
    Author: HOANG TRONG PHI
    20/4/2026
"""
import maya.cmds as cmds
import os

def getSelMeshName():
    """
    Trả về tên hiển thị (transform) của mesh đang được select.
    Nếu không có selection hoặc không phải mesh → return None
    """
    selection = cmds.ls(sl=True, shortNames=True)

    if not selection:
        return None

    # Lấy object đầu tiên
    obj = selection[0]

    # Nếu chọn shape → lấy parent transform
    if cmds.nodeType(obj) == "mesh":
        parent = cmds.listRelatives(obj, parent=True, fullPath=False)
        return parent[0] if parent else None

    # Nếu là transform → check có phải mesh không
    shapes = cmds.listRelatives(obj, shapes=True, fullPath=False) or []
    for shape in shapes:
        if cmds.nodeType(shape) == "mesh":
            return obj

    return None


def getSelMeshNames():
    """
    Trả về list tên hiển thị (transform) của tất cả mesh đang được select.
    Nếu không có selection hoặc không phải mesh → return empty list
    """

    result = []
    selection = cmds.ls(sl=True, shortNames=True)

    for obj in selection:
        if cmds.nodeType(obj) == "mesh":
            parent = cmds.listRelatives(obj, parent=True, fullPath=False)
            if parent:
                result.append(parent[0])
        else:
            shapes = cmds.listRelatives(obj, shapes=True, fullPath=False) or []
            for shape in shapes:
                if cmds.nodeType(shape) == "mesh":
                    result.append(obj)
                    break

    return result