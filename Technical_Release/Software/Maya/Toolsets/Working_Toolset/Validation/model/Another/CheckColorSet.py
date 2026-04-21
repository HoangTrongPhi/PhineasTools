# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\zExtra\CheckColorSet.py
# Compiled at: 2021-06-26 21:43:23
"""
        CheckColorSet.py
    Created by otis - Nguyen Dang Khoa at 7/23/2020
    Update 6:07 PM - 23/07/2020
    
 """
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Obj have ColorSet'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    currSel = cmds.ls(selection=True) or []
    objColorSetList = []
    for node in nodes:
        clrSet = cmds.polyColorSet(node, query=True, allColorSets=True)
        if clrSet:
            objColorSetList.append(node)

    cmds.select(currSel)
    return objColorSetList


def fix(*arg):
    mel.eval('colorSetEditor')
    return 1


def doc(*arg):
    mess = 'ColorSet: Cac obj co colorset\n\nTrieu chung: mot so Obj bi xuat hien mau den, hoac co mau la\n\nHowToFix: Ban nhan nut Fix va chon ColorSet khong dung -> Delete Hoac Dung tool Master CleanUp'
    return mess


def report(*arg):
    return 1
