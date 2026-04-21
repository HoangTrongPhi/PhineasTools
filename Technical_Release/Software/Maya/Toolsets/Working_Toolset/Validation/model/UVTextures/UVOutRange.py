# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\UVTextures\UVOutRange.py
# Compiled at: 2021-06-26 21:43:23
"""
        UVOutRange.py
    Created by otis - Nguyen Dang Khoa at 8/17/2020
    Update 4:06 PM - 17/08/2020
    
 """
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'UV OutRange (0,1)'
check = 0
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    uvRange = []
    selIt = om.MItSelectionList(selectionMesh)
    while not selIt.isDone():
        faceIt = om.MItMeshPolygon(selIt.getDagPath())
        objectName = selIt.getDagPath().getPath()
        while not faceIt.isDone():
            if faceIt.hasUVs() == True:
                UVs = faceIt.getUVs()
                for index, eachUVs in enumerate(UVs):
                    if index == 0:
                        for eachUV in eachUVs:
                            if eachUV < 0 or eachUV > 10:
                                componentName = str(objectName) + '.f[' + str(faceIt.index()) + ']'
                                uvRange.append(componentName)
                                break

                    if index == 1:
                        for eachUV in eachUVs:
                            if eachUV < 0:
                                componentName = str(objectName) + '.f[' + str(faceIt.index()) + ']'
                                uvRange.append(componentName)
                                break

            faceIt.next(None)

        selIt.next()

    return uvRange


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'UV OutRange (0,1): Mot so UV bi nam ngoai vung 0,1\n\nHowToFix: Move UV nam trong vung 0,1'
    return mess


def report(*arg):
    return 1
