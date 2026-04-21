# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\Geometry\Nonmanifold.py
# Compiled at: 2021-06-26 21:43:23
"""
        Nonmanifold.py
    Created by otis - Nguyen Dang Khoa at 8/17/2020
    Update 3:10 PM - 17/08/2020
    
 """
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Nonmanifold'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    currSel = cmds.ls(selection=True) or []
    cmds.select(nodes)
    mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","0","1e-05","0","0.01","0","1e-05","0","1","0","0" };')
    nonManifoldVertex = cmds.ls(selection=True) or []
    if currSel == []:
        cmds.selectMode(object=True)
    cmds.select(currSel)
    return nonManifoldVertex


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'Nonmanifold: 1 mesh 3D  khong the trai ra thanh 2D duoc\n\nHowToFix: Can dieu chinh luoi lai cho hop ly'
    return mess


def report(*arg):
    return 1
