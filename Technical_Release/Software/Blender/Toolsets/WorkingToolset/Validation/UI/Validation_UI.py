bl_info = {
    "name": "HF Validation UI",
    "author": "HF",
    "version": (1, 0),
    "blender": (5, 1, 0),
    "category": "3D View",
}

import bpy

# =========================================================
# PROPERTIES (STATE UI)
# =========================================================

class HF_ValidationProps(bpy.types.PropertyGroup):

    # ---------------- GEO ----------------
    geo_concave: bpy.props.BoolProperty(name="Concave Faces")
    geo_lamina: bpy.props.BoolProperty(name="Lamina Faces")
    geo_nonmanifold: bpy.props.BoolProperty(name="Non Manifold")
    geo_zeroedge: bpy.props.BoolProperty(name="Zero Edge")

    # ---------------- UV ----------------
    uv_missing: bpy.props.BoolProperty(name="Missing UV")
    uv_multi: bpy.props.BoolProperty(name="Multiple UV Sets")
    uv_overlap: bpy.props.BoolProperty(name="Overlap UV")
    uv_inverted: bpy.props.BoolProperty(name="Inverted UV")
    uv_out: bpy.props.BoolProperty(name="UV Out of Range")
    uv_setname: bpy.props.BoolProperty(name="UV Set Name")

    # ---------------- TEXTURE ----------------
    tex_missing: bpy.props.BoolProperty(name="Missing Textures")
    tex_invalid: bpy.props.BoolProperty(name="Invalid Texture Path")
    tex_unused: bpy.props.BoolProperty(name="Unused Materials")
    tex_colorset: bpy.props.BoolProperty(name="Color Set")

    # ---------------- SCENE ----------------
    sc_empty: bpy.props.BoolProperty(name="Empty Transform")
    sc_hidden: bpy.props.BoolProperty(name="Hidden Objects")
    sc_frozen: bpy.props.BoolProperty(name="Frozen Transform")
    sc_history: bpy.props.BoolProperty(name="History")

    # ---------------- NAMING ----------------
    name_default: bpy.props.BoolProperty(name="Default Name")
    name_duplicate: bpy.props.BoolProperty(name="Duplicate Name")
    name_convention: bpy.props.BoolProperty(name="Naming Convention")

    # ---------------- STATUS ----------------
    # lưu trạng thái UI (controller sẽ set)
    status_geo_concave: bpy.props.StringProperty(default="none")
    status_geo_lamina: bpy.props.StringProperty(default="none")
    status_geo_nonmanifold: bpy.props.StringProperty(default="none")
    status_geo_zeroedge: bpy.props.StringProperty(default="none")

#=============== UTILS (VIEW HELPER) ======================
def draw_status(layout, status):
    """Hiển thị trạng thái giống QFrame"""
    icon_map = {
        "ok": 'CHECKMARK',
        "warning": 'ERROR',
        "error": 'CANCEL',
        "none": 'DOT'
    }
    layout.label(text="", icon=icon_map.get(status, 'DOT'))

#========== OPERATORS (UI EVENT ONLY) ====================
class HF_OT_RunAll(bpy.types.Operator):
    bl_idname = "hf_validation.run_all"
    bl_label = "Run All"

    def execute(self, context):
        # gọi controller
        print("Run All Triggered")
        return {'FINISHED'}


class HF_OT_RunSingle(bpy.types.Operator):
    bl_idname = "hf_validation.run_single"
    bl_label = "Run Single"

    check_name: bpy.props.StringProperty()

    def execute(self, context):
        print(f"Run check: {self.check_name}")
        return {'FINISHED'}


class HF_OT_Refresh(bpy.types.Operator):
    bl_idname = "hf_validation.refresh"
    bl_label = "Refresh"

    def execute(self, context):
        print("Refresh UI")
        return {'FINISHED'}



#========== PANEL UI ===================
class HF_PT_Validation(bpy.types.Panel):
    bl_label = "HF Validation Tool"
    bl_idname = "HF_PT_validation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HF Tools"

    def draw(self, context):
        layout = self.layout
        props = context.scene.hf_validation

        # ================= HEADER =================
        row = layout.row()
        row.operator("hf_validation.run_all", icon='PLAY')
        row.operator("hf_validation.refresh", icon='FILE_REFRESH')

        # ================= GEO =================
        box = layout.box()
        box.label(text="Geometry")

        self.draw_item(box, props, "geo_concave", "status_geo_concave")
        self.draw_item(box, props, "geo_lamina", "status_geo_lamina")
        self.draw_item(box, props, "geo_nonmanifold", "status_geo_nonmanifold")
        self.draw_item(box, props, "geo_zeroedge", "status_geo_zeroedge")

        # ================= UV =================
        box = layout.box()
        box.label(text="UV")

        self.draw_item(box, props, "uv_missing")
        self.draw_item(box, props, "uv_multi")
        self.draw_item(box, props, "uv_overlap")
        self.draw_item(box, props, "uv_inverted")
        self.draw_item(box, props, "uv_out")
        self.draw_item(box, props, "uv_setname")

        # ================= TEXTURE =================
        box = layout.box()
        box.label(text="Texture")

        self.draw_item(box, props, "tex_missing")
        self.draw_item(box, props, "tex_invalid")
        self.draw_item(box, props, "tex_unused")
        self.draw_item(box, props, "tex_colorset")

        # ================= SCENE =================
        box = layout.box()
        box.label(text="Scene")

        self.draw_item(box, props, "sc_empty")
        self.draw_item(box, props, "sc_hidden")
        self.draw_item(box, props, "sc_frozen")
        self.draw_item(box, props, "sc_history")

        # ================= NAMING =================
        box = layout.box()
        box.label(text="Naming")

        self.draw_item(box, props, "name_default")
        self.draw_item(box, props, "name_duplicate")
        self.draw_item(box, props, "name_convention")


    def draw_item(self, layout, props, prop_name, status_name=None):
        row = layout.row(align=True)

        # checkbox
        row.prop(props, prop_name, text="")

        # label
        row.label(text=prop_name.replace("_", " ").title())

        # status
        if status_name:
            draw_status(row, getattr(props, status_name))

        # button
        op = row.operator("hf_validation.run_single", text="", icon='PLAY')
        op.check_name = prop_name

# ========== REGISTER ==================
classes = (
    HF_ValidationProps,
    HF_OT_RunAll,
    HF_OT_RunSingle,
    HF_OT_Refresh,
    HF_PT_Validation,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.hf_validation = bpy.props.PointerProperty(type=HF_ValidationProps)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.hf_validation

if __name__ == "__main__":
    register()