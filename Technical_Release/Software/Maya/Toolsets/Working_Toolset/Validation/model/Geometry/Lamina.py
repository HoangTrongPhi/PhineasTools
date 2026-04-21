
"""

    
"""
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Lamina'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print ('Running ' + __name__)
    currSel = cmds.ls(selection=True) or []
    cmds.select(nodes)
    mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","0","0.001","0","0.01","0","1e-05","0","-1","1","0" }')
    laminaFaceList = cmds.ls(selection=True) or []
    if currSel == []:
        cmds.selectMode(object=True)
    cmds.select(currSel)
    return laminaFaceList


def fix(*arg):
    print ('Fixing...')
    return 1


def doc(*arg):
    mess = 'Lamina: cac face co chung edges, face bi trung nhau\n\nHowToFix: Delete nhung face bi trung'
    return mess


def report(*arg):
    return 1
