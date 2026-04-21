
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Zero Face'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print ('Running ' + __name__)
    currSel = cmds.ls(selection=True) or []
    cmds.select(nodes)
    mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","1","1e-05","0","0.01","0","1e-05","0","-1","0","0" }')
    zeroAreaFaces = cmds.ls(selection=True) or []
    if currSel == []:
        cmds.selectMode(object=True)
    cmds.select(currSel)
    return zeroAreaFaces


def fix(*arg):
    print ('Fixing...')
    return 1


def doc(*arg):
    mess = 'Zero Face: Cac face co dien tich qua nho\n\nHowToFix: weld diem, hoac collapse edge lai'
    return mess


def report(*arg):
    return 1
