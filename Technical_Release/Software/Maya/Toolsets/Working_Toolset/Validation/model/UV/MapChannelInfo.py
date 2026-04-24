# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Date: 22/04/2026
    Maya 2026+ (Python 3)
    Notes: Check Mesh có nhiều UV set
"""
import maya.cmds as cmds

NAME = 'Multiple UV Sets'

def run(nodes=None, selectionMesh=None):
    """
    Check meshes that have more than 1 UV set
    """
    print('[QC] Running: {}'.format(NAME))
    if not nodes:
        return []
    error_meshes = []
    for node in nodes:
        if not cmds.objExists(node):
            continue
        # Đảm bảo là mesh shape
        shapes = cmds.listRelatives(node, shapes=True, fullPath=True) or []
        mesh_shapes = [s for s in shapes if cmds.nodeType(s) == 'mesh']
        for shape in mesh_shapes:
            try:
                uv_sets = cmds.polyUVSet(shape, q=True, allUVSets=True) or []
            except Exception:
                continue

            if len(uv_sets) > 1:
                error_meshes.append(node)
                break  # tránh duplicate node
    return error_meshes

def fix(nodes=None):
    """
    This check is NOT auto-fixable safely
    (UV sets cần quyết định thủ công)
    """
    print('[QC] This issue cannot be auto-fixed safely.')
    return False


def notification():
    return 'Mesh has more than 1 UV Channel'


def doc():
    return (
        "UV Channel Issue:\n"
        "- Mesh có nhiều hơn 1 UV Set\n\n"
        "Why it's a problem:\n"
        "- Game pipeline (Unreal/Maya) thường chỉ dùng 1 UV chính\n"
        "- UV dư có thể gây lỗi lightmap hoặc export\n\n"
        "How to fix:\n"
        "1. Dùng Master Cleanup tool\n"
        "2. Hoặc thủ công:\n"
        "   UV > UV Set Editor\n"
        "   -> Delete các UV Set không cần\n"
    )


def report():
    return {
        "name": NAME,
        "check": CHECK,
        "fixable": FIXABLE
    }