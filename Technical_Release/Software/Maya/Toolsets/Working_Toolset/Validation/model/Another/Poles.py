# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\zExtra\Poles.py
# Compiled at: 2021-06-26 21:43:23
"""
        CheckPoles.py
    Created by otis - Nguyen Dang Khoa at 7/22/2020
    Update 2:12 PM - 22/07/2020
    
 """
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Poles'
check = 0
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    poles = []
    selIt = om.MItSelectionList(selectionMesh)
    while not selIt.isDone():
        vertexIt = om.MItMeshVertex(selIt.getDagPath())
        objectName = selIt.getDagPath().getPath()
        while not vertexIt.isDone():
            if vertexIt.numConnectedEdges() > 5:
                vertexIndex = vertexIt.index()
                componentName = str(objectName) + '.vtx[' + str(vertexIndex) + ']'
                poles.append(componentName)
            vertexIt.next()

        selIt.next()

    return poles


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'Poles: Mot vetex duoc noi voi nhieu hon 5 Edges\n\nHowToFix: tuy tinh huong, co the bo qua hoac di luoi lai'
    return mess


def report(*arg):
    return 1
