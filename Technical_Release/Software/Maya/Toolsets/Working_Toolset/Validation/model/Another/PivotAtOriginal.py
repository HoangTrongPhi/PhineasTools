# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\zExtra\PivotAtOriginal.py
# Compiled at: 2021-06-26 21:43:23
"""
        PivotAtOriginal.py
    Created by otis - Nguyen Dang Khoa at 8/20/2020
    Update 2:48 PM - 20/08/2020
    
 """
import maya.cmds as cmds, sys
name = 'Pivot at [0,0,0]'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    currSel = cmds.ls(selection=True) or []
    err = []
    for node in nodes:
        transformNode = node
        if cmds.objectType(node) != 'transform':
            transformNode = cmds.listRelatives(node, parent=True, fullPath=True)[0]
        pivotPos = cmds.xform(transformNode, query=1, ws=1, rp=1)
        if pivotPos != [0.0, 0.0, 0.0]:
            err.append(node)

    cmds.select(currSel)
    return err


def fix(*arg):
    print 'Move Pivot to 0,0,0 Done'
    currSel = cmds.ls(selection=True) or []
    for obj in currSel:
        transformNode = obj
        if cmds.objectType(obj) != 'transform':
            transformNode = cmds.listRelatives(obj, parent=True, fullPath=True)[0]
        cmds.move(0, 0, 0, transformNode + '.scalePivot', transformNode + '.rotatePivot', absolute=True)

    return 1


def notification():
    mess = 'Move Pivot to 0,0,0 Done'
    return mess


def doc(*arg):
    mess = 'Pivot not 0,0,0: Cac mesh can pivot tai Original 0,0,0\n\nHowToFix: Nhan nut Fix de set Pivot 0,0,0'
    return mess


def report(*arg):
    return 1
