"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - UI cho hộp thoại đổi tên asset, MeshItemWidget
"""

#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

Signal = QtCore.Signal

import importlib

# -- Logic Modules
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)


class RenameAssetDialog(QtWidgets.QDialog):
    def __init__(self, current_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rename Asset")
        self.setModal(True)
        self.setFixedWidth(320)
        layout = QtWidgets.QVBoxLayout(self)

        row = QtWidgets.QHBoxLayout()
        row.addWidget(QtWidgets.QLabel("Rename:"))
        self.edit = QtWidgets.QLineEdit(current_name)
        row.addWidget(self.edit)
        layout.addLayout(row)

        btns = QtWidgets.QHBoxLayout()
        btns.addStretch()
        self.ok_btn = QtWidgets.QPushButton("OK", self)
        self.cancel_btn = QtWidgets.QPushButton("Cancel", self)
        btns.addWidget(self.ok_btn)
        btns.addWidget(self.cancel_btn)
        layout.addLayout(btns)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def get_new_name(self):
        return self.edit.text().strip()
