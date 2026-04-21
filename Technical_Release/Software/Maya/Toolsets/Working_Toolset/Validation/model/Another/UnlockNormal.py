# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\zExtra\UnlockNormal.py
# Compiled at: 2021-06-26 21:43:23
"""
        UnlockNormal.py
    Created by otis - Nguyen Dang Khoa at 11/6/2020
    Update 5:26 PM - 06/11/2020
    
 """
import maya.cmds as cmds
name = 'Mesh have Lock Normal'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print 'Running ' + __name__
    err = []
    for node in nodes:
        vtxCount = cmds.polyEvaluate(node, vertex=True)
        i = 0
        while i < vtxCount:
            vtxLock = ('{}.vtx[{}]').format(node, i)
            status = cmds.polyNormalPerVertex(vtxLock, query=True, freezeNormal=True)
            if True in status:
                err.append(vtxLock)
            i += 1

    return err


def fix(*arg):
    print 'Fixing...'
    return 1


def doc(*arg):
    mess = 'LockNormal: Mesh co vertex bi lock normal\n\nHowToFix: Mesh Display > chon Vertex va click Unlock Normal \nCan kiem tra lai Hard va Soft Edge'
    return mess


def report(*arg):
    return 1
