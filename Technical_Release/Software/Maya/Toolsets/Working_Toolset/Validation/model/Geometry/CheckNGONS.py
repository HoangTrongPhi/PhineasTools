
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'N-GONS'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print ('Running ' + __name__)
    ngons = []
    selIt = om.MItSelectionList(selectionMesh)
    while not selIt.isDone():
        faceIt = om.MItMeshPolygon(selIt.getDagPath())
        objectName = selIt.getDagPath().getPath()
        while not faceIt.isDone():
            numOfEdges = faceIt.getEdges()
            if len(numOfEdges) > 4:
                faceIndex = faceIt.index()
                componentName = str(objectName) + '.f[' + str(faceIndex) + ']'
                ngons.append(componentName)
            faceIt.next(None)

        selIt.next()

    return ngons


def fix(*arg):
    currSel = cmds.ls(selection=True)
    for sel in currSel:
        cmds.select(sel)
        mel.eval('ConvertSelectionToFaces; polySelectConstraint -m 2 -t 8 -sz 3; polyTriangulate -ch 1 ;  polyQuad  -a 30 -kgb 1 -ktb 1 -khe 1 -ws 1 -ch 0; polySelectConstraint -m 0; resetPolySelectConstraint;')

    cmds.select(currSel)
    return 1


def doc(*arg):
    mess = 'N-GON: Check loi 1 face co nhieu hon 5 canh(5 vertex)\n\nHowToFix: Can dieu chinh luoi lai cho hop ly'
    return mess


def report(*arg):
    return 1
