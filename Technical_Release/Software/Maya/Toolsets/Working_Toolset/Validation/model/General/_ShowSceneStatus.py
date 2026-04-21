# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (HuangFei)
    22/4/2026
"""
import os
import maya.cmds as cmds

# =========================
# CONSTANTS
# =========================
OK_COLOR = "#4fff4f"
BAD_COLOR = "#ff4638"


def format_color(text, is_ok=True):
    """Format color"""
    color = OK_COLOR if is_ok else BAD_COLOR
    return f'<font color="{color}">{text}</font>'


# =========================
# SCENE INFO
# =========================

def get_project_name(script_path=None):
    """Get project name from script path"""
    try:
        path = script_path or __file__
        folder = os.path.dirname(path)
        return os.path.basename(os.path.dirname(folder))
    except Exception:
        return "Unknown"


def get_scene_name():
    """Return scene extension or not saved"""
    scene = cmds.file(query=True, sceneName=True, shortName=True)
    if not scene:
        return format_color("Unsaved", False)

    ext = os.path.splitext(scene)[1]
    return format_color(ext, True)


# =========================
# MAYA SETTINGS
# =========================

def get_unit(expected="cm"):
    """Check linear unit"""
    try:
        unit = cmds.currentUnit(query=True, linear=True)
        return format_color(unit, unit == expected)
    except Exception:
        return format_color("Error", False)


def get_time_unit(expected="film"):
    """Check time unit"""
    try:
        time_unit = cmds.currentUnit(query=True, time=True)
        return format_color(time_unit, time_unit == expected)
    except Exception:
        return format_color("Error", False)


# =========================
# SELECTION HELPERS
# =========================

def get_selection():
    """Safe selection getter"""
    return cmds.ls(selection=True, long=True) or []


def is_valid_transform(obj):
    """Check if object is valid transform"""
    return cmds.objExists(obj) and cmds.objectType(obj) == "transform"


# =========================
# OBJECT INFO
# =========================

def get_object_name(obj):
    """Return object name"""
    if not obj or not cmds.objExists(obj):
        return format_color("None", False)
    return format_color(obj.split("|")[-1], True)


def get_transform_status(obj):
    """Check freeze transform"""
    if not is_valid_transform(obj):
        return format_color("Invalid", False)

    try:
        t = cmds.getAttr(f"{obj}.translate")[0]
        r = cmds.getAttr(f"{obj}.rotate")[0]
        s = cmds.getAttr(f"{obj}.scale")[0]

        is_ok = (
            all(abs(v) < 1e-6 for v in t) and
            all(abs(v) < 1e-6 for v in r) and
            all(abs(v - 1) < 1e-6 for v in s)
        )

        return format_color("OK" if is_ok else "Not Freeze", is_ok)
    except Exception:
        return format_color("Error", False)


def get_pivot_status(obj):
    """Check pivot at world origin"""
    if not is_valid_transform(obj):
        return format_color("Invalid", False)

    try:
        pivot = cmds.xform(obj, query=True, ws=True, rp=True)
        pivot = [round(v, 3) for v in pivot]

        is_ok = pivot == [0.0, 0.0, 0.0]
        return format_color(pivot, is_ok)
    except Exception:
        return format_color("Error", False)


def get_history_status(obj):
    """Check history on mesh"""
    if not is_valid_transform(obj):
        return format_color("Invalid", False)

    shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
    if not shapes:
        return format_color("No Shape", False)

    shape = shapes[0]
    if cmds.nodeType(shape) != "mesh":
        return format_color("Not Mesh", False)

    history = cmds.listHistory(shape) or []

    clean = [
        h for h in history
        if cmds.objectType(h) not in ["shadingEngine", "groupId", "objectSet"]
    ]

    is_ok = len(clean) <= 1
    return format_color("OK" if is_ok else "Has History", is_ok)


# =========================
# AGGREGATOR (FOR CONTROLLER)
# =========================

def collect_scene_status():
    """
    Return dict data for UI/controller
    """
    sel = get_selection()
    obj = sel[0] if len(sel) == 1 else None

    data = {
        "project": get_project_name(),
        "scene": get_scene_name(),
        "unit": get_unit(),
        "time": get_time_unit(),
    }

    if obj:
        data.update({
            "name": get_object_name(obj),
            "pivot": get_pivot_status(obj),
            "transform": get_transform_status(obj),
            "history": get_history_status(obj),
        })
    else:
        data.update({
            "name": format_color("None", False),
            "pivot": format_color("None", False),
            "transform": format_color("None", False),
            "history": format_color("None", False),
        })

    return data