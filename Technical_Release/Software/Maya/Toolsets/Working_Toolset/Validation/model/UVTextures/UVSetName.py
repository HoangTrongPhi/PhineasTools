# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\UVTextures\UVSetName.py
# Compiled at: 2021-06-26 21:43:23
"""
        UVSetName.py
    Created by otis - Nguyen Dang Khoa at 1/6/2021
    Update 10:47 AM - 06/01/2021
    
"""
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'UVset Name'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    err = []
    for mesh in nodes:
        uvSetList = cmds.polyUVSet(mesh, query=True, allUVSets=True)
        if uvSetList[0] != 'map1':
            err.append(mesh)

    return err


def fix(*arg):
    print 'Fixing...'
    currSelLong = cmds.ls(selection=True, long=True, dagObjects=True, type='transform') or []
    for mesh in currSelLong:
        uvSetList = cmds.polyUVSet(mesh, query=True, allUVSets=True)
        if 'map1' not in uvSetList:
            if uvSetList[0] != 'map1':
                cmds.polyUVSet(mesh, rename=True, newUVSet='map1')

    return 1


def doc(*arg):
    mess = 'UVsets has wrong name: UVset bi sai naming\n\nHowToFix: UVset 1 phai ten la map1'
    return mess


def report(*arg):
    return 1
