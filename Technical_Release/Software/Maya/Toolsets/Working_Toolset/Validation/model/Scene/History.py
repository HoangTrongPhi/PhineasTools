# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (Optimized)
    22/4/2026
    Maya 2026+ (Python 3)

"""
import maya.cmds as cmds

name = 'Need Clear History'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    print(f'Running {__name__}')
    err = []
    for node in nodes:
        shape = node
        if cmds.objectType(node) == 'transform':
            relatives = cmds.listRelatives(node, shapes=True, fullPath=True)
            if relatives:
                shape = relatives[0]
        if shape and cmds.nodeType(shape) == 'mesh':
            history_list = cmds.listHistory(shape, future=True)
            ok_history_list = []
            for his in history_list:
                his_type = cmds.objectType(his)
                if his_type not in ('shadingEngine', 'groupId', 'objectSet'):
                    ok_history_list.append(his)

            history_size = len(ok_history_list)
            if history_size > 1:
                err.append(node)

    return err


def fix(*arg):
    print('Clear History Done')
    curr_sel = cmds.ls(selection=True) or []
    cmds.delete(curr_sel, constructionHistory=True)
    return 1


def notification():
    mess = 'Clear History Done'
    return mess


def doc(*arg):
    mess = 'Obj have history: Cac obj can phai clear history\n\nHowToFix: Nhan nut Fix de Clear history hoac Menu: Edit>Delete By Type>History'
    return mess


def report(*arg):
    return 1
