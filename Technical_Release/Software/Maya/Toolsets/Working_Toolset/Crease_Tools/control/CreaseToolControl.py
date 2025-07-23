from Software.Maya.Toolsets.Working_Toolset.Crease_Tools.UI.Crease_tool_UI import Crease_tool_UI
import Software.Maya.Toolsets.Working_Toolset.Crease_Tools.model.crease_bevel_bool_mirror_hardedge as group1
import Software.Maya.Toolsets.Working_Toolset.Crease_Tools.model.crease_smooth as group2
import Software.Maya.Toolsets.Working_Toolset.Crease_Tools.model.crease_extension as group3

from PySide6.QtWidgets import QMessageBox

class CreaseToolControl:
    def __init__(self):
        self.ui = Crease_tool_UI()
        self.setup_connections()

    def setup_connections(self):
        # Nhóm 1
        self.ui.btn_cp_hbevel.clicked.connect(lambda: group1.cp_hbevel())
        self.ui.btn_cp_hedge_sel.clicked.connect(lambda: group1.cp_hedge_sel())
        self.ui.btn_cp_hard_display.clicked.connect(lambda: group1.cp_hard_display())
        self.ui.btn_cp_panel_bool.clicked.connect(lambda: group1.cp_panel_bool())
        self.ui.btn_cp_display_bool.clicked.connect(lambda: group1.cp_display_bool())
        self.ui.btn_cp_keep_bool.clicked.connect(lambda: group1.cp_keep_bool())
        self.ui.btn_cp_instance_bool.clicked.connect(lambda: group1.cp_instance_bool())
        self.ui.btn_cp_bak_that_nod.clicked.connect(self.bak_that_nod_dialog)
        self.ui.btn_cp_nod_baker.clicked.connect(lambda: group1.cp_nod_baker())
        self.ui.btn_cp_mirror.clicked.connect(lambda: group1.cp_mirror())
        self.ui.btn_cp_mesh_slicer.clicked.connect(lambda: group1.cp_mesh_slicer())

        # Nhóm 2
        self.ui.btn_cp_qsmooth.clicked.connect(lambda: group2.cp_qsmooth())
        self.ui.btn_cp_shape_shifter.clicked.connect(lambda: group2.cp_shape_shifter())
        self.ui.btn_cp_goz.clicked.connect(lambda: group2.cp_goz())
        self.ui.btn_cp_get_goz.clicked.connect(lambda: group2.cp_get_goz())

        # Nhóm 3
        self.ui.btn_sp_smart_lvl.clicked.connect(lambda: group3.sp_smart_lvl())
        self.ui.btn_sp_fast_crease.clicked.connect(lambda: group3.sp_fast_crease())
        self.ui.btn_sp_no_crease.clicked.connect(lambda: group3.sp_no_crease())
        self.ui.btn_sp_smooth_os.clicked.connect(lambda: group3.sp_smooth_os())
        self.ui.btn_smooth_sg.clicked.connect(lambda: group3.smooth_sg())
        self.ui.btn_sp_crease_preset.clicked.connect(lambda: group3.sp_crease_preset())
        self.ui.btn_sp_level.clicked.connect(lambda: group3.sp_level())
        self.ui.btn_sp_physical_crease.clicked.connect(lambda: group3.sp_physical_crease())
        self.ui.btn_sp_show_crease_ed.clicked.connect(lambda: group3.sp_show_crease_ed())

    def bak_that_nod_dialog(self):
        try:
            from maya import cmds
            sel = cmds.ls(selection=True)
            if not sel:
                QMessageBox.warning(self.ui, "Thông báo", "Hãy chọn một object!")
                return
            group1.cp_bak_that_nod(sel[0])
        except Exception as e:
            QMessageBox.warning(self.ui, "Lỗi", str(e))

    def show(self):
        self.ui.show()
