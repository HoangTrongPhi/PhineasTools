# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Date: 22/04/2026
    Maya 2026+ (Python 3)
    Notes: Check Mesh có 2 UV set
"""

import maya.cmds as cmds

# =========================
# META INFO
# =========================
NAME = 'More than 1 UV Channel'
CHECK = True
FIXABLE = False


# =========================
# CORE
# =========================
def run(nodes=None, selectionMesh=None):
    """
    Check meshes that have more than 1 UV set
    """
    print(f'[QC] Running: {NAME}')

    if not nodes:
        return []

    current_selection = cmds.ls(selection=True) or []
    error_meshes = []

    for node in nodes:
        if not cmds.objExists(node):
            continue

        try:
            uv_sets = cmds.polyUVSet(node, query=True, allUVSets=True) or []
        except Exception:
            continue

        if len(uv_sets) > 1:
            error_meshes.append(node)

    # Restore selection
    if current_selection:
        cmds.select(current_selection)

    return error_meshes


# =========================
# FIX
# =========================
def fix(nodes=None):
    """
    This check is NOT auto-fixable safely
    (UV sets cần quyết định thủ công)
    """
    print('[QC] This issue cannot be auto-fixed safely.')
    return False


# =========================
# UI / INFO
# =========================
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