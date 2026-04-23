import maya.cmds as cmds
import os
import sys
from maya import OpenMayaUI as omui

try:
    from shiboken2 import wrapInstance

    from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QIODevice
    from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QFileDialog
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    from shiboken6 import wrapInstance

    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QFileDialog
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.Validation.UI.Validation_UI as Validation_UI
importlib.reload(Validation_UI)


# Validation Model

#--- Geometry---
import Software.Maya.Toolsets.Working_Toolset.Validation.model.Geometry.ConcaveFaces as ConcaveFaces
importlib.reload(ConcaveFaces)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.Geometry.LaminaFaces as LaminaFaces
importlib.reload(LaminaFaces)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.Geometry.NonManifold as NonManifold
importlib.reload(NonManifold)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.Geometry.ZeroEdegeLength as ZeroEdegeLength
importlib.reload(ZeroEdegeLength)
#--- UV---

def getDirectoryofModule(modulename):
    """
    Input: module as string
    OUtput:
        List: name as string and directory of module
    """
    module = modulename
    try:
        module = importlib.import_module(modulename)        # importlib.import_module(name, package)
    except:
        pass

    currWD = os.path.dirname(module.__file__)
    return currWD

#####
def getMayaMainWindow():
    """Lấy cửa sổ chính của Maya."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    return None

class ValidationControl(QtWidgets.QMainWindow):
    """
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(ValidationControl, self).__init__(parent=parent)

        self.ui = Validation_UI.Ui_mainWindow()
        self.ui.setupUi(self)

        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("ValidationControl_window")
        self.setWindowTitle("ValidationTool")


        # Kết nối các tín hiệu (signal) từ widget tới các hàm (slot)
        self.createConnection()
        self.initState()
        self.buildCheckMap()


    # ===============================
    # INIT
    # ===============================
    def initState(self):
        """Set default UI state"""
        frames = [
            self.ui.fr_ConcaveFaces,
            self.ui.fr_LaminaFaces,
            self.ui.fr_NonManifold,
            self.ui.fr_ZeroEdge
        ]

        for fr in frames:
            self.setStatus(fr, None)  # reset (xám)

    def buildCheckMap(self):
        """Map checkbox → function → frame"""
        self.checkMap = {
            self.ui.chbx_ConcaveFaces: (self.checkConcaveFaces, self.ui.fr_ConcaveFaces),
            self.ui.chbx_LanimaFaces: (self.checkLaminaFaces, self.ui.fr_LaminaFaces),
            self.ui.chbx_NonManifold: (self.checkNonManifold, self.ui.fr_NonManifold),
            self.ui.chbx_ZeroEdge: (self.checkZeroEdge, self.ui.fr_ZeroEdge),
        }

    # ===============================
    # CONNECTION
    # ===============================
    def createConnection(self):
        """
        Kết nối các nút bấm và widget khác với các hàm xử lý.
        """
        self.ui.btnRefreshTool.clicked.connect(self.refresh)

        # check từng cái
        # --- Geometry ---
        self.ui.btnCh_ConcaveFaces.clicked.connect(self.runCheckConcave)
        self.ui.btnCh_LaminaFaces.clicked.connect(self.runCheckLamina)
        self.ui.btnCh_NonManifold.clicked.connect(self.runCheckNonManifold)
        self.ui.btnCh_ZeroEdge.clicked.connect(self.runCheckZeroEdge)


        # self.ui.btnCheckAll.clicked.connect(self.runAllChecks)
    # ============== UTILS ==============
    # ===================================

    def getSelectedMeshes(self):
        sel = cmds.ls(selection=True, long=True) or []
        return sel

    #--- setStatus ---
    def setStatus(self, frame, status):
        """
        status: 'ok' | 'warning' | 'error'
        """
        if status:
            frame.setProperty("status", status)
        else:
            frame.setProperty("status", "")

        frame.style().unpolish(frame)
        frame.style().polish(frame)
        frame.update()

    #--- log ---
    def log(self, text):
        self.ui.txEd_Console.append(text)

    def refresh(self):
        # Clear console
        self.ui.txEd_Console.clear()
        cmds.warning("  Console Reset Done  ")

    # ===============================
    # RUN SINGLE CHECK (checkbox gate)
    # ===============================

    # ----- Geometry ------
    def runCheckConcave(self):
        if self.ui.chbx_ConcaveFaces.isChecked():
            self.checkConcaveFaces()
        else:
            self.setStatus(self.ui.fr_ConcaveFaces, "warning")

    def runCheckLamina(self):
        if self.ui.chbx_LanimaFaces.isChecked():
            self.checkLaminaFaces()
        else:
            self.setStatus(self.ui.fr_LaminaFaces, "warning")

    def runCheckNonManifold(self):
        if self.ui.chbx_NonManifold.isChecked():
            self.checkNonManifold()
        else:
            self.setStatus(self.ui.fr_NonManifold, "warning")

    def runCheckZeroEdge(self):
        if self.ui.chbx_ZeroEdge.isChecked():
            self.checkZeroEdge()
        else:
            self.setStatus(self.ui.fr_ZeroEdge, "warning")

    # ===============================
    # CORE CHECK LOGIC
    # ===============================

    def checkConcaveFaces(self):
        nodes = self.getSelectedMeshes()

        if not nodes:
            self.setStatus(self.ui.fr_ConcaveFaces, "warning")
            self.log("[Concave] Không có mesh nào được chọn")
            return

        result = ConcaveFaces.run(nodes)

        if not result:
            self.setStatus(self.ui.fr_ConcaveFaces, "ok")
            self.log("[Concave] OK")
        else:
            self.setStatus(self.ui.fr_ConcaveFaces, "error")
            self.log(f"[Concave] Found {len(result)} faces")

    def checkLaminaFaces(self):
        nodes = self.getSelectedMeshes()

        if not nodes:
            self.setStatus(self.ui.fr_LaminaFaces, "warning")
            self.log("[Lamina] No selection")
            return

        result = LaminaFaces.run(nodes)

        if not result:
            self.setStatus(self.ui.fr_LaminaFaces, "ok")
            self.log("[Lamina] OK")
        else:
            self.setStatus(self.ui.fr_LaminaFaces, "error")
            self.log(f"[Lamina] Found {len(result)}")

    def checkNonManifold(self):
        nodes = self.getSelectedMeshes()

        if not nodes:
            self.setStatus(self.ui.fr_NonManifold, "warning")
            self.log("[NonManifold] No selection")
            return

        result = NonManifold.run(nodes)

        if not result:
            self.setStatus(self.ui.fr_NonManifold, "ok")
            self.log("[NonManifold] OK")
        else:
            self.setStatus(self.ui.fr_NonManifold, "error")
            self.log(f"[NonManifold] Found {len(result)}")

    def checkZeroEdge(self):
        nodes = self.getSelectedMeshes()

        if not nodes:
            self.setStatus(self.ui.fr_ZeroEdge, "warning")
            self.log("[ZeroEdge] No selection")
            return

        result = ZeroEdegeLength.run(nodes)

        if not result:
            self.setStatus(self.ui.fr_ZeroEdge, "ok")
            self.log("[ZeroEdge] OK")
        else:
            self.setStatus(self.ui.fr_ZeroEdge, "error")
            self.log(f"[ZeroEdge] Found {len(result)}")




    # ===============================
    # RUN ALL (optional)
    # ===============================
    def runAllChecks(self):
        for checkbox, (func, frame) in self.checkMap.items():
            if checkbox.isChecked():
                func()
            else:
                self.setStatus(frame, "warning")



def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "ValidationControl_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    # Tạo và hiển thị cửa sổ tool
    mainWin = ValidationControl(parent=mayaMainWindow)
    mainWin.setObjectName("ValidationControl_window")
    mainWin.show()
    return mainWin



openWindow()

