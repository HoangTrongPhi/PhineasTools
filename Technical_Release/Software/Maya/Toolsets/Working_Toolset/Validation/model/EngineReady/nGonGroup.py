
import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.mel as mel

name = 'N-GONS'
check = 1
fixAble = 1


def run(nodes, selectionMesh):
    print('Running ' + __name__)

    ngons = []
    selIt = om.MItSelectionList(selectionMesh)

    while not selIt.isDone():
        dagPath = selIt.getDagPath()
        faceIt = om.MItMeshPolygon(dagPath)

        objectName = dagPath.fullPathName()

        while not faceIt.isDone():
            # Fast check: ngon = >4 vertices
            if faceIt.polygonVertexCount() > 4:
                ngons.append(f"{objectName}.f[{faceIt.index()}]")

            faceIt.next()

        selIt.next()

    return ngons


def fix(*arg):
    currSel = cmds.ls(selection=True, long=True) or []
    if not currSel:
        return 0

    cmds.select(currSel)

    mel.eval('''
    ConvertSelectionToFaces;
    polySelectConstraint -m 2 -t 8 -sz 3;
    polyTriangulate -ch 0;
    polyQuad -a 30 -kgb 1 -ktb 1 -khe 1 -ws 1 -ch 0;
    polySelectConstraint -m 0;
    resetPolySelectConstraint;
    ''')

    cmds.select(currSel)
    return 1


def doc(*arg):
    mess = 'N-GON: Check loi 1 face co nhieu hon 5 canh(5 vertex)\n\nHowToFix: Can dieu chinh luoi lai cho hop ly'
    return mess


def report(*arg):
    return 1
