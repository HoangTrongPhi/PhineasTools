# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\zExtra\OpenEdges.py
# Compiled at: 2021-06-26 21:43:23
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Open Edge'
check = 0
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    openEdges = []
    selIt = om.MItSelectionList(selectionMesh)
    while not selIt.isDone():
        edgeIt = om.MItMeshEdge(selIt.getDagPath())
        objectName = selIt.getDagPath().getPath()
        while not edgeIt.isDone():
            if edgeIt.numConnectedFaces() < 2:
                edgeIndex = edgeIt.index()
                componentName = str(objectName) + '.e[' + str(edgeIndex) + ']'
                openEdges.append(componentName)
            edgeIt.next()

        selIt.next()

    return openEdges


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'OpenEdges: Check cac mesh khong duoc kin, bi hole\n\nHowToFix: tuy tinh huong, co the bo qua hoac cap hole lai'
    return mess


def report(*arg):
    return 1
