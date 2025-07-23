
"""
    1/11/2024
    Create by HOANG TRONG PHI   @HuangFei
    Done ,testing Maya 2022 -> 2024
"""
#from __future__ import print_function
import maya.cmds as cmds

def getPosition():
    """
    get translate of selection
    """
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        translate = cmds.xform(curSelList[0], query=True, rotatePivot=True, worldSpace=True)
        return translate
    return []

def getRotation():
    """
    get rotation of selection
    """
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        rotation = cmds.xform(curSelList[0], query=True, rotation=True, worldSpace=True)
        return rotation
    return []

def getScale():
    """
    get Scale of selection
    """
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        scales = cmds.xform(curSelList[0], query=True, scale=True, worldSpace=True)
        return scales
    return []

def setPosition(translate):
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        for mesh in curSelList:
            #newTanslate = cmds.move(translate[0], translate[1], translate[2], mesh, rotatePivotRelative=True)
            cmds.setAttr(('{}.translateX').format(mesh), translate[0])
            cmds.setAttr(('{}.translateY').format(mesh), translate[1])
            cmds.setAttr(('{}.translateZ').format(mesh), translate[2])
    return 1

def setRotation(rotation):
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        for mesh in curSelList:
            cmds.setAttr(('{}.rotateX').format(mesh), rotation[0])
            cmds.setAttr(('{}.rotateY').format(mesh), rotation[1])
            cmds.setAttr(('{}.rotateZ').format(mesh), rotation[2])

    return 1


def setScale(scales):
    """
    Set attribute of mesh: scale
    """
    curSelList = cmds.ls(selection=True)
    if len(curSelList) > 0:
        for mesh in curSelList:
            cmds.setAttr(('{}.scaleX').format(mesh), scales[0])
            cmds.setAttr(('{}.scaleY').format(mesh), scales[1])
            cmds.setAttr(('{}.scaleZ').format(mesh), scales[2])

    return 1
