"""
    Author : Hoàng Trọng Phi
    26/6/2025

Chức năng:
    - Cấu hình thư viện Asset
    - Cho phép người dùng chọn thư mục chứa thư viện Asset
    - Lưu đường dẫn thư mục vào file cấu hình config.json
"""
#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore

import os
import importlib
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as Config_libs_path
importlib.reload(Config_libs_path)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Categories as Categories
importlib.reload(Categories)

class ConfigureDialog(QtWidgets.QDialog):
    path_saved = QtCore.Signal(str)  # Tín hiệu phát ra khi đường dẫn được lưu
    """
        Chức năng chính:
        - Browse folder 
        - Save Folder Path vừa tìm --->> config.son
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Asset Library")
        self.setMinimumSize(400, 50)
        self.resize(400, 50)

        # Layout
        self.layout = QtWidgets.QHBoxLayout(self)  # Layout ngang

        self.path_edit = QtWidgets.QLineEdit(self)  # Ô nhập đường dẫn thư viện
        self.browse_btn = QtWidgets.QPushButton("Browse", self)  # Nút chọn thư mục
        self.save_btn = QtWidgets.QPushButton("Save", self)  # Nút lưu đường dẫn

        self.layout.addWidget(self.path_edit)
        self.layout.addWidget(self.browse_btn)
        self.layout.addWidget(self.save_btn)

        #Gán giá trị mặc định từ file cấu hình
        self.path_edit.setText(Config_libs_path.Configuration.get_asset_library_path())

        self.root_folder = Config_libs_path.Configuration.get_asset_library_path()  # Lưu đường dẫn thư mục gốc
        #Kết nối tín hiệu các nút
        self.browse_btn.clicked.connect(self.browse_folder)
        self.save_btn.clicked.connect(self.save_path)

    def browse_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Library Folder")
        if folder:
            self.path_edit.setText(folder)

    def save_path(self):
        path = self.path_edit.text()
        Config_libs_path.Configuration.set_asset_library_path(path)
        self.path_saved.emit(path) 
        self.accept()

    # Ở cuối file ConfigureDialog.py
    def Refresh_Library(comboBox=None):
        """
        Làm mới danh sách categories cho UI hoặc chỉ lấy lại data JSON.
        """
        if comboBox is not None:
            Categories.Categories.refresh_categories(comboBox)
        else:
            category_path = Config_libs_path.Configuration.get_categories_json_path()
            import json, os
            if os.path.exists(category_path):
                with open(category_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                return data.get("categories", [])
            else:
                return []

