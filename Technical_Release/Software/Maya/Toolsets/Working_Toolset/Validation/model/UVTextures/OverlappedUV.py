# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\UVTextures\OverlappedUV.py
# Compiled at: 2021-06-26 21:43:23
"""
        OverlappedUV.py
    Created by otis - Nguyen Dang Khoa at 8/20/2020
    Update 3:11 PM - 20/08/2020
    
 """
import maya.cmds as cmds
name = 'UV Overlapped'
check = 0
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    err = []
    for node in nodes:
        convertToFaces = cmds.ls(cmds.polyListComponentConversion(node, tf=True), fl=True)
        overlapping = cmds.polyUVOverlap(convertToFaces, oc=True)
        if overlapping is not None:
            for face in overlapping:
                err.append(face)

    return err


def fix(*arg):
    print 'UV Overlapped...'
    return 1


def doc(*arg):
    mess = 'UV Overlapped: UV bi Overlapped\n\nHowToFix: Edit UV to avoid Overlap UV'
    return mess


def report(*arg):
    return 1
