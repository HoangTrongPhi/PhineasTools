# Blender_ValidationTool/Status.py
#
# All status state lives here: the enum items, the icon mapping,
# and the small draw helper. Anything that wants to render a status
# imports from this single module.

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

ICON_MAP = {
    STATUS_OK:      "CHECKMARK",
    STATUS_WARNING: "ERROR",
    STATUS_ERROR:   "CANCEL",
    STATUS_NONE:    "DOT",
}

def draw_status(layout, status):
    """Render a single status icon into the given layout row."""
    layout.label(text="", icon=ICON_MAP.get(status, "DOT"))
