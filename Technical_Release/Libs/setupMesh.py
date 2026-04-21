"""
    Hoàng Trọng Phi
    16/6/2025
"""

import maya.cmds as cmds

def clean_history():
    curr_sel = cmds.ls(selection=True)
    if curr_sel:
        cmds.delete(curr_sel, constructionHistory=True)
    return 1

def freeze_transform():
    cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1)
    return 1

def fix_duplicate_names():
    all_nodes = cmds.ls(dag=True, long=True)
    short_names = {}

    for node in all_nodes:
        short = node.split("|")[-1]
        if short in short_names:
            new_name = cmds.rename(node, short + "_fix")
            print(f"Renamed: {node} -> {new_name}")
        else:
            short_names[short] = node
    return 1

def setup_mesh():
    clean_history()
    freeze_transform()
    fix_duplicate_names()
    return 1
####-------------######
