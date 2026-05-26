# Blender_ValidationTool/Status.py
#
# All status state lives here: the enum items, the icon mapping,
# and the small draw helper. Anything that wants to render a status
# imports from this single module.

import os
import bpy
import bpy.utils.previews

STATUS_NONE    = "none"
STATUS_OK      = "ok"
STATUS_WARNING = "warning"
STATUS_ERROR   = "error"

# For bpy.props.EnumProperty(items=...)
STATUS_ITEMS = [
    (STATUS_NONE,    "None",    ""),
    (STATUS_OK,      "OK",      ""),
    (STATUS_WARNING, "Warning", ""),
    (STATUS_ERROR,   "Error",   ""),
]

# Drop matching PNGs into ./icons next to this file.
# STATUS_NONE intentionally has no PNG — it keeps the built-in DOT icon.
_ICON_FILES = {
    STATUS_OK:      "ok.png",
    STATUS_WARNING: "warning.png",
    STATUS_ERROR:   "error.png",
}

# Used when the custom PNG for a status is missing.
_FALLBACK_ICON = {
    STATUS_NONE:    "DOT",
    STATUS_OK:      "CHECKMARK",
    STATUS_WARNING: "ERROR",
    STATUS_ERROR:   "CANCEL",
}

_preview_collection = None


def draw_status(layout, status):
    """Render a single status icon into the given layout row."""
    if _preview_collection is not None and status in _preview_collection:
        layout.label(text="", icon_value=_preview_collection[status].icon_id)
    else:
        layout.label(text="", icon=_FALLBACK_ICON.get(status, "DOT"))


def register():
    global _preview_collection
    _preview_collection = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    for status, filename in _ICON_FILES.items():
        path = os.path.join(icons_dir, filename)
        if os.path.isfile(path):
            _preview_collection.load(status, path, 'IMAGE')


def unregister():
    global _preview_collection
    if _preview_collection is not None:
        bpy.utils.previews.remove(_preview_collection)
        _preview_collection = None
