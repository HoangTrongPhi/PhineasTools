"""
    Hoàng Trọng Phi
    16/6/2025
"""

import maya.cmds as cmds


def cleanHistory():
    currSel = cmds.ls(selection=True)
    for mesh in currSel:
        cmds.delete(mesh, constructionHistory=True)
    return 1

def freezeTransform():
    cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1)
    return 1

def setupMesh():
    cleanHistory()
    freezeTransform()
    return 1
####-------------######
