bl_info = {
    "name": "Validation UI",
    "author": "HuangFei",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "category": "3D View",
}

import bpy
import importlib

# ---- Modules ----
from . import   Config, Status, Properties
from .Controller import Refresh, RunAll, RunSingle, UnhideHidden, ApplyHistory
from .Model.Geometry import Concave, LaminaFaces, OverlapVertex
from .Model.UV import Multi_UVset
from .Model.Scene import HiddenObject

# Dev hot-reload. Set DEV_MODE = False when shipping.
# Phải reload các module Model TRƯỚC Config vì Config bind hàm vào dispatch
# table; nếu Config reload trước, nó nhặt phiên bản cũ của Concave/... rồi
# cache lại bản cũ vào CHECK_FUNCTIONS / CHECK_HIGHLIGHT_FUNCTIONS.
DEV_MODE = True
if DEV_MODE:
    for _m in (Concave, LaminaFaces, OverlapVertex, Multi_UVset, HiddenObject,
               Config, Status, Properties, UnhideHidden, ApplyHistory,
               Refresh, RunAll, RunSingle):
        importlib.reload(_m)

# =========================================================
# PANEL
# =========================================================
class VALIDATION_PT_panel(bpy.types.Panel):
    bl_label = "Validation Tools"
    bl_idname = "VIEW3D_PT_validation_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Validation Tools"

    def draw(self, context):
        layout = self.layout
        props = context.scene.validation

        # Header
        row = layout.row(align=True)
        row.operator("validation.run_all", icon='PLAY')
        row.operator("validation.refresh", icon='FILE_REFRESH')

        # Data-driven: categories and items both come from Config.
        for title, items in Config.CHECKS:
            box = layout.box()
            box.label(text=title)
            for key, label in items:
                self._draw_item(box, props, key, label)

    @staticmethod
    def _draw_item(layout, props, key, label):
        row = layout.row(align=True)

        status = getattr(props, f"stt_{key}", Status.STATUS_NONE)

        row.prop(props, key, text="")
        row.label(text=label)
        Status.draw_status(row, status)

        op = row.operator("validation.run_single", text="", icon='PLAY')
        op.check_name = key


# =========================================================
# REGISTER
# =========================================================
# Each module owns its own register/unregister. The UI file only
# orchestrates the call order.
_MODULES = (Status, Properties, UnhideHidden, ApplyHistory, Refresh, RunAll, RunSingle)


def register():
    for m in _MODULES:
        m.register()
    bpy.utils.register_class(VALIDATION_PT_panel)


def unregister():
    bpy.utils.unregister_class(VALIDATION_PT_panel)
    for m in reversed(_MODULES):
        m.unregister()


if __name__ == "__main__":
    register()
