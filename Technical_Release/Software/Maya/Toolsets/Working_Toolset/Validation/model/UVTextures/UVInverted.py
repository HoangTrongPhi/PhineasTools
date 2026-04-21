# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\UVTextures\UVInverted.py
# Compiled at: 2021-06-26 21:43:23
"""
        UVInverted.py
    Created by otis - Nguyen Dang Khoa at 9/24/2020
    Update 2:26 PM - 24/09/2020
    
 """
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'Inverted UV'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    err = []
    currSel = cmds.ls(selection=True)
    for node in nodes:
        cmds.select(node)
        cmds.selectMode(component=True)
        cmds.selectType(facet=True)
        mel.eval('selectUVFaceOrientationComponents {} 0 2 1;')
        invertedFaceList = cmds.ls(selection=True)
        if invertedFaceList != []:
            for face in invertedFaceList:
                err.append(face)

    cmds.selectMode(object=True)
    cmds.select(currSel)
    return err


def fix(*arg):
    print 'Fixing...'
    mel.eval('polyMultiLayoutUV -lm 1 -sc 0 -rbf 0 -fr 1 -ps 0.2 -l 0 -gu 1 -gv 1 -psc 0 -su 1 -sv 1 -ou 0 -ov 0;')
    return 1


def doc(*arg):
    mess = 'UV Inverted: UV bi nguoc, in red\n\nHowToFix: Flip UV lai\n\nNeu van bi bao loi cac ban Clean History nhe'
    return mess


def report(*arg):
    return 1
