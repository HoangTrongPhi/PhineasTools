from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton

class Crease_tool_UI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Crease Tool UI")
        self.resize(400, 700)
        main_layout = QVBoxLayout(self)

        # --- Group 1: Crease/Bevel/Bool/Mirror/Hard Edge ---
        group1 = QGroupBox("Crease / Bevel / Boolean / Mirror / Hard Edge")
        group1_layout = QVBoxLayout()
        self.btn_cp_hbevel = QPushButton("Bevel Cạnh Cứng (cp_hbevel)")
        self.btn_cp_hedge_sel = QPushButton("Chọn Hard Edge (cp_hedge_sel)")
        self.btn_cp_hard_display = QPushButton("Hiển thị Hard Edge (cp_hard_display)")
        self.btn_cp_panel_bool = QPushButton("Boolean Panel (cp_panel_bool)")
        self.btn_cp_display_bool = QPushButton("Hiển thị Boolean (cp_display_bool)")
        self.btn_cp_keep_bool = QPushButton("Giữ Boolean (cp_keep_bool)")
        self.btn_cp_instance_bool = QPushButton("Instance Boolean (cp_instance_bool)")
        self.btn_cp_bak_that_nod = QPushButton("Bake Node (cp_bak_that_nod)")
        self.btn_cp_nod_baker = QPushButton("Bake Toàn Bộ Node (cp_nod_baker)")
        self.btn_cp_mirror = QPushButton("Mirror Mesh (cp_mirror)")
        self.btn_cp_mesh_slicer = QPushButton("Slice Mesh (cp_mesh_slicer)")
        for btn in [
            self.btn_cp_hbevel, self.btn_cp_hedge_sel, self.btn_cp_hard_display,
            self.btn_cp_panel_bool, self.btn_cp_display_bool, self.btn_cp_keep_bool,
            self.btn_cp_instance_bool, self.btn_cp_bak_that_nod, self.btn_cp_nod_baker,
            self.btn_cp_mirror, self.btn_cp_mesh_slicer
        ]:
            group1_layout.addWidget(btn)
        group1.setLayout(group1_layout)

        # --- Group 2: Crease & Smooth ---
        group2 = QGroupBox("Crease & Smooth")
        group2_layout = QVBoxLayout()
        self.btn_cp_qsmooth = QPushButton("Smooth Nhanh (cp_qsmooth)")
        self.btn_cp_shape_shifter = QPushButton("Shape Shifter (cp_shape_shifter)")
        self.btn_cp_goz = QPushButton("Gửi GoZ (cp_goz)")
        self.btn_cp_get_goz = QPushButton("Nhận GoZ (cp_get_goz)")
        for btn in [
            self.btn_cp_qsmooth, self.btn_cp_shape_shifter,
            self.btn_cp_goz, self.btn_cp_get_goz
        ]:
            group2_layout.addWidget(btn)
        group2.setLayout(group2_layout)

        # --- Group 3: Extension1 - thao tác crease nâng cao ---
        group3 = QGroupBox("Extension - Thao tác Crease Nâng Cao")
        group3_layout = QVBoxLayout()
        self.btn_sp_smart_lvl = QPushButton("Smart Level (sp_smart_lvl)")
        self.btn_sp_fast_crease = QPushButton("Crease Nhanh (sp_fast_crease)")
        self.btn_sp_no_crease = QPushButton("Xóa Crease (sp_no_crease)")
        self.btn_sp_smooth_os = QPushButton("Smooth Object (sp_smooth_os)")
        self.btn_smooth_sg = QPushButton("Smooth Group (smooth_sg)")
        self.btn_sp_crease_preset = QPushButton("Preset Crease (sp_crease_preset)")
        self.btn_sp_level = QPushButton("Set Level (sp_level)")
        self.btn_sp_physical_crease = QPushButton("Crease Thực (sp_physical_crease)")
        self.btn_sp_show_crease_ed = QPushButton("Hiện Cạnh Có Crease (sp_show_crease_ed)")
        for btn in [
            self.btn_sp_smart_lvl, self.btn_sp_fast_crease, self.btn_sp_no_crease,
            self.btn_sp_smooth_os, self.btn_smooth_sg, self.btn_sp_crease_preset,
            self.btn_sp_level, self.btn_sp_physical_crease, self.btn_sp_show_crease_ed
        ]:
            group3_layout.addWidget(btn)
        group3.setLayout(group3_layout)

        # --- Main Layout ---
        for group in [group1, group2, group3]:
            main_layout.addWidget(group)
        main_layout.addStretch(1)
