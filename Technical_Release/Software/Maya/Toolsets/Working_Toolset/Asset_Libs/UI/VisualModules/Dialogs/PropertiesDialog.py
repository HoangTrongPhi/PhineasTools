"""
    Author: Hoàng Trọng Phi
    1/7/2025
    Chức năng:
        - Hiển thị thông tin chi tiết của asset (tên, category, đường dẫn, ngày tạo, kích thước, số lượng triangle)
        - Cho phép người dùng chọn category từ danh sách đã định nghĩa
        - Lưu category đã chọn vào file assignments.json
        - Hiển thị thông tin này trong một hộp thoại riêng biệt
        - Cho phép người dùng xem và chỉnh sửa thông tin của asset ( Rename, Save Category, xem Properties)
"""
#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore
Signal = QtCore.Signal


import os
import datetime
import json

import importlib

# -- Logic Modules
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)

CATEGORIES_JSON_PATH = config_module.Configuration.get_categories_json_path()

DIALOG_MAX_WIDTH = 460  # Chỉnh theo ý bạn

class PropertiesDialog(QtWidgets.QDialog):
    def __init__(self, file_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Asset Properties")
        self.setModal(True)
        self.setMinimumWidth(380)
        self.setMaximumWidth(DIALOG_MAX_WIDTH)

        self.file_path = file_path
        self.folder = os.path.dirname(file_path)
        self.old_name = os.path.basename(file_path)
        self.base_name, self.ext = os.path.splitext(self.old_name)
        self.png_path = os.path.join(self.folder, self.base_name + ".png")

        # --- Layout chính ---
        layout = QtWidgets.QVBoxLayout(self)

        # Asset name (nằm ngang)
        name_layout = QtWidgets.QHBoxLayout()
        name_label_title = QtWidgets.QLabel("Asset Name:")
        name_label_title.setMinimumWidth(90)
        name_label_title.setMaximumWidth(110)
        self.name_label = QtWidgets.QLabel(self.base_name)
        self.name_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.name_label.setMaximumWidth(220)
        name_layout.addWidget(name_label_title)
        name_layout.addWidget(self.name_label)
        name_layout.addStretch()
        layout.addLayout(name_layout)

        # Category (nằm ngang)
        category_layout = QtWidgets.QHBoxLayout()
        category_label = QtWidgets.QLabel("Category:")
        category_label.setMinimumWidth(90)
        category_label.setMaximumWidth(110)
        self.category_combo = QtWidgets.QComboBox()
        self.category_combo.setMaximumWidth(220)
        category_layout.addWidget(category_label)
        category_layout.addWidget(self.category_combo)
        category_layout.addStretch()
        layout.addLayout(category_layout)

        # File Path (nằm ngang)
        path_layout = QtWidgets.QHBoxLayout()
        path_label = QtWidgets.QLabel("File Path:")
        path_label.setMinimumWidth(90)
        path_label.setMaximumWidth(110)
        show_path = file_path.replace('\\', '/')
        self.path_value = QtWidgets.QLabel(show_path)
        self.path_value.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.path_value.setMaximumWidth(220)
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_value)
        path_layout.addStretch()
        layout.addLayout(path_layout)

        # Created (nằm ngang)
        created_layout = QtWidgets.QHBoxLayout()
        created_label = QtWidgets.QLabel("Created:")
        created_label.setMinimumWidth(90)
        created_label.setMaximumWidth(110)
        self.created_value = QtWidgets.QLabel(self._get_creation_date())
        self.created_value.setMaximumWidth(220)
        created_layout.addWidget(created_label)
        created_layout.addWidget(self.created_value)
        created_layout.addStretch()
        layout.addLayout(created_layout)

        # Size (nằm ngang)
        size_layout = QtWidgets.QHBoxLayout()
        size_label = QtWidgets.QLabel("Size:")
        size_label.setMinimumWidth(90)
        size_label.setMaximumWidth(110)
        self.size_value = QtWidgets.QLabel(self._get_size())
        self.size_value.setMaximumWidth(220)
        size_layout.addWidget(size_label)
        size_layout.addWidget(self.size_value)
        size_layout.addStretch()
        layout.addLayout(size_layout)

        # Triangles (nằm ngang)
        tri_layout = QtWidgets.QHBoxLayout()
        tri_label = QtWidgets.QLabel("Triangles:")
        tri_label.setMinimumWidth(90)
        tri_label.setMaximumWidth(110)
        self.tri_value = QtWidgets.QLabel(self._get_triangle_count())
        self.tri_value.setMaximumWidth(220)
        tri_layout.addWidget(tri_label)
        tri_layout.addWidget(self.tri_value)
        tri_layout.addStretch()
        layout.addLayout(tri_layout)

        # Load categories và category đã gán
        self._load_categories()
        self._load_assigned_category()

        # --- Buttons ---
        btn_layout = QtWidgets.QHBoxLayout()
        self.save_btn = QtWidgets.QPushButton("Save", self)
        self.cancel_btn = QtWidgets.QPushButton("Cancel", self)
        btn_layout.addStretch()
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)

        # Connect
        self.save_btn.clicked.connect(self._apply_changes)
        self.cancel_btn.clicked.connect(self.reject)


    def _get_size(self):
        try:
            size = os.path.getsize(self.file_path)
            return f"{round(size / 1024, 2)} KB"
        except Exception:
            return "N/A"

    def _get_creation_date(self):
        try:
            ts = os.path.getctime(self.file_path)
            return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return "N/A"

    def _get_triangle_count(self):
        """
        Đọc số triangle từ mesh_data.json theo đúng tên file asset.
        Nếu không có thì trả về 'N/A'
        """
        try:
            info = config_module.Configuration.get_mesh_data(os.path.basename(self.file_path))
            if info and "triangle_count" in info:
                return str(info["triangle_count"])
            return "N/A"
        except Exception:
            return "N/A"

    #----- properties  categories -----
    def _load_categories(self):
        self.category_combo.setEditable(False)
        self.category_combo.clear()

        placeholder = "— No category selected —"
        self.category_combo.addItem(placeholder)
        self.category_combo.model().item(0).setEnabled(False)

        if not os.path.exists(CATEGORIES_JSON_PATH):
            return

        with open(CATEGORIES_JSON_PATH, "r") as f:
            data = json.load(f)
        for cat in data.get("categories", []):
            self.category_combo.addItem(cat)
        self.category_combo.setCurrentIndex(0)

    def _load_assigned_category(self):
        try:
            assignments = config_module.Configuration.load_assignments()
            assigned = assignments.get(self.base_name, "")
            index = self.category_combo.findText(assigned)
            if index >= 0:
                self.category_combo.setCurrentIndex(index)
        except Exception as e:
            print(f"Failed to load assigned category: {e}")

    def _apply_changes(self):
        selected_category = self.category_combo.currentText()

        try:
            assignments = config_module.Configuration.load_assignments()
            # Chỉ cập nhật lại category cho asset hiện tại
            assignments[self.base_name] = selected_category
            config_module.Configuration.save_assignments(assignments)
            self.accept()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Category Save Error", str(e))
            return
