# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Updated: 2026-04-24
    Maya 2026+ (Python 3)
"""

import maya.cmds as cmds
import maya.mel as mel

import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om, sys
name = 'EdgeLength <0.00000001'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print ('Running ' + __name__)
    currSel = cmds.ls(selection=True) or []
    cmds.select(nodes)
    mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","0","1e-05","1","0.01","0","1e-05","0","-1","0","0" }')
    zeroLengthEdges = cmds.ls(selection=True) or []
    vertexConnectedList = cmds.polyListComponentConversion(zeroLengthEdges, fromEdge=True, toVertex=True)
    if currSel == []:
        cmds.selectMode(object=True)
    cmds.select(currSel)
    return vertexConnectedList


def fix(*arg):
    print ('Fixing...')
    return 1


def doc(*arg):
    mess = 'Edge Length: Check cac Edge qua nho\n\nHowToFix: Weld diem lai'
    return mess


def report(*arg):
    return 1








































"""# Mặc định ban đầu
name = 'Edge Length Check'
check = 1
fixAble = 0

import maya.api.OpenMaya as om

name = 'Close Vertices'
check = 1
fixAble = 1  # có thể merge


import maya.api.OpenMaya as om

def run(nodes=None, selectionMesh=None, threshold=1):
    print(f'Running Close Vertices with Threshold: {threshold}')

    if not nodes:
        return []

    bad_vertices = set()

    #Convert nodes -> MSelectionList
    selList = om.MSelectionList()
    for node in nodes:
        try:
            selList.add(node)
        except:
            pass

    selIt = om.MItSelectionList(selList)

    while not selIt.isDone():
        dagPath = selIt.getDagPath()
        meshFn = om.MFnMesh(dagPath)

        points = meshFn.getPoints(om.MSpace.kWorld)

        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]

                if p1.distanceTo(p2) < threshold:
                    bad_vertices.add(f"{dagPath.fullPathName()}.vtx[{i}]")
                    bad_vertices.add(f"{dagPath.fullPathName()}.vtx[{j}]")

        selIt.next()

    return list(bad_vertices)


def doc():
    return (
        'Edge Length:\n'
        '- Kiểm tra các edge có độ dài cực nhỏ (degenerate edges)\n\n'
        'Cách chỉnh tham số:\n'
        '- Bạn có thể thay đổi threshold trong hàm run() tùy theo scale của scene.'
    )


def report():
    return 1"""