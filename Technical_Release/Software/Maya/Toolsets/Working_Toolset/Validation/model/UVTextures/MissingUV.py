# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\UVTextures\MissingUV.py
# Compiled at: 2021-06-26 21:43:23
"""
    MissingUV.py
Created by otis - Nguyen Dang Khoa at 8/17/2020
Update 3:25 PM - 17/08/2020

"""
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Faces Missing UV'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    missingUVs = []
    selIt = om.MItSelectionList(selectionMesh)
    while not selIt.isDone():
        faceIt = om.MItMeshPolygon(selIt.getDagPath())
        objectName = selIt.getDagPath().getPath()
        while not faceIt.isDone():
            if faceIt.hasUVs() == False:
                componentName = str(objectName) + '.f[' + str(faceIt.index()) + ']'
                missingUVs.append(componentName)
            faceIt.next(None)

        selIt.next()

    return missingUVs


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'Faces Missing UV: face chua duoc Unwrap UV\n\nHowToFix: Chon cac face bi loi va Unwrap UV'
    return mess


def report(*arg):
    return 1
