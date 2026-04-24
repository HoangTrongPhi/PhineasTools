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
    from PySide6.QtWidgets import QApplication

    from PySide6.QtWidgets import QApplication

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
import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.MapChannelInfo as MapChannelInfo
importlib.reload(MapChannelInfo)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.MissingUV as MissingUV
importlib.reload(MissingUV)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.OverlappedUV as OverlappedUV
importlib.reload(OverlappedUV)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.UVInverted as UVInverted
importlib.reload(UVInverted)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.UVOutRange as UVOutRange
importlib.reload(UVOutRange)

import Software.Maya.Toolsets.Working_Toolset.Validation.model.UV.UVSetName as UVSetName
importlib.reload(UVSetName)


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
            self.ui.fr_ZeroEdge,

            self.ui.fr_MisUV,
            self.ui.fr_MoreUV,
            self.ui.fr_OverlapUV,
            self.ui.fr_InvertedUV,
            self.ui.fr_UVOutRange,
            self.ui.fr_UVSetName,
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

            # --- UV Mapping ---
            self.ui.chbx_MisUV: (self.checkMissUV, self.ui.fr_MisUV),
            self.ui.chbx_MoreUV: (self.checkMoreThan1UVset, self.ui.fr_MoreUV),
            self.ui.chbx_OverlapUV: (self.checkOverlapUV, self.ui.fr_OverlapUV),
            self.ui.chbx_InvertedUV: (self.checkUVInverted, self.ui.fr_InvertedUV),
            self.ui.chbx_UVOutRange: (self.checkUVOutRange, self.ui.fr_UVOutRange),
            self.ui.chbx_UVSetName: (self.checkUVSetName, self.ui.fr_UVSetName),
        }

    # ===============================
    # CONNECTION
    # ===============================
    def createConnection(self):
        """
        Kết nối các nút bấm và widget khác với các hàm xử lý.
        """
        self.ui.btnRefreshTool.clicked.connect(self.refresh)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)


        # check từng cái
        # --- Geometry ---
        self.ui.btnCh_ConcaveFaces.clicked.connect(self.runCheckConcave)
        self.ui.btnCh_LaminaFaces.clicked.connect(self.runCheckLamina)
        self.ui.btnCh_NonManifold.clicked.connect(self.runCheckNonManifold)
        self.ui.btnCh_ZeroEdge.clicked.connect(self.runCheckZeroEdge)

        #---- UV ----
        self.ui.btnCh_MisUV.clicked.connect(self.runCheckMissUV)
        self.ui.btnCh_MoreUV.clicked.connect(self.runCheckMoreThan1UVset)
        self.ui.btnCh_Overlap.clicked.connect(self.runOverlapUV)
        self.ui.btnCh_InvertedUV.clicked.connect(self.runUVInverted)
        self.ui.btnCh_UVOutRange.clicked.connect(self.runUVOutRange)
        self.ui.btnCh_UVSetName.clicked.connect(self.runUVSetName)


        # self.ui.btnCheckAll.clicked.connect(self.)
        self.ui.btnRun.clicked.connect(self.runAllChecks)
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
        # Reset Progress Bar
        self.ui.progressBar.setValue(0)
        # Reset các khung trạng thái về mặc định
        self.initState()
        cmds.warning("  Console & UI Reset Done  ")

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

    # ----- UV ------
    def runCheckMissUV(self):
        if self.ui.chbx_MisUV.isChecked():
            self.checkMissUV()
        else:
            self.setStatus(self.ui.fr_MisUV, "warning")

    def runCheckMoreThan1UVset(self):
        if self.ui.chbx_MoreUV.isChecked():
            self.checkMoreThan1UVset()
        else:
            self.setStatus(self.ui.fr_MoreUV, "warning")

    def runOverlapUV(self):
        if self.ui.chbx_OverlapUV.isChecked():
            self.checkOverlapUV()
        else:
            self.setStatus(self.ui.fr_OverlapUV, "warning")

    def runUVInverted(self):
        if self.ui.chbx_InvertedUV.isChecked():
            self.checkUVInverted()
        else:
            self.setStatus(self.ui.fr_InvertedUV, "warning")

    def runUVOutRange(self):
        if self.ui.chbx_UVOutRange.isChecked():
            self.checkUVOutRange()
        else:
            self.setStatus(self.ui.fr_UVOutRange, "warning")

    def runUVSetName(self):
        if self.ui.chbx_UVSetName.isChecked():
            self.checkUVSetName()
        else:
            self.setStatus(self.ui.fr_UVSetName, "warning")
    # ===============================
    # CORE CHECK LOGIC
    # ===============================
    def _generic_check(self, module, frame, label):
        nodes = cmds.ls(selection=True, long=True)

        if not nodes:
            self.setStatus(frame, "warning")
            self.log(f"[{label}] Không có mesh nào được chọn")
            return

        # luôn đảm bảo đang ở select tool
        cmds.setToolTo('selectSuperContext')

        # chạy check (module chỉ return data)
        result = module.run(nodes, selectionMesh=nodes)

        if not result:
            self.setStatus(frame, "ok")
            self.log(f"[{label}] OK")

            # restore object mode
            cmds.select(nodes, r=True)
            cmds.selectMode(object=True)

        else:
            self.setStatus(frame, "error")
            self.log(f"[{label}] Found {len(result)} errors")

            # =========================
            # FORCE FACE MODE
            # =========================
            cmds.selectMode(object=False, component=True)
            cmds.selectType(allComponents=False)
            cmds.selectType(polymeshFace=True)

            # hilite mesh
            meshes = list(set([f.split('.')[0] for f in result]))
            cmds.hilite(meshes)

            # select lỗi
            cmds.select(result, r=True)

        return result

    #----- Geometry ------
    def checkConcaveFaces(self):
        self._generic_check(ConcaveFaces, self.ui.fr_ConcaveFaces, "Concave Faces")

    def checkLaminaFaces(self):
        self._generic_check(LaminaFaces, self.ui.fr_LaminaFaces, "Lamina Faces")

    def checkNonManifold(self):
        self._generic_check(NonManifold, self.ui.fr_NonManifold, "Non-Manifold")

    def checkZeroEdge(self):
        self._generic_check(ZeroEdegeLength, self.ui.fr_ZeroEdge, "ZeroEdegeLength")

    # ----- UV ------
    def checkMissUV(self):
        self._generic_check(MissingUV, self.ui.fr_MisUV, "Missing UV")

    def checkMoreThan1UVset(self):
        self._generic_check(MapChannelInfo, self.ui.fr_MoreUV, "More than 1 UV set")

    def checkOverlapUV(self):
        self._generic_check(OverlappedUV, self.ui.fr_OverlapUV, "Overlap UV")

    def checkUVInverted(self):
        self._generic_check(UVInverted, self.ui.fr_InvertedUV, "Inverted UV")

    def checkUVOutRange(self):
        self._generic_check(UVOutRange, self.ui.fr_UVOutRange, "UV Out Range")

    def checkUVSetName(self):
        self._generic_check(UVSetName, self.ui.fr_UVSetName, "UV Set Name")



    # ===============================
    # RUN ALL (optional)
    # ===============================
    def runAllChecks(self):
        # 1. Lọc ra danh sách các mục thực sự được tick

        items_to_check = []
        for checkbox, (func, frame) in self.checkMap.items():
            if checkbox.isChecked():
                items_to_check.append((func, frame))
            else:
                # Nếu không chọn thì set status về warning/xám tùy ý
                self.setStatus(frame, "warning")

        if not items_to_check:
            self.log(">>> [Warning] Không có mục nào được chọn để kiểm tra!")
            self.ui.progressBar.setValue(0)
            return

        # 2. Thiết lập Progress Bar dựa trên số lượng mục đã chọn
        total_steps = len(items_to_check)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(total_steps)
        self.ui.progressBar.setValue(0)

        self.log(f">>> Bắt đầu kiểm tra {total_steps} mục...")

        # 3. Chạy từng hàm và cập nhật Progress Bar
        for index, (func, frame) in enumerate(items_to_check):
            # Chạy hàm kiểm tra (ví dụ: checkConcaveFaces)
            func()

            # Cập nhật giá trị (index + 1 vì index bắt đầu từ 0)
            self.ui.progressBar.setValue(index + 1)

            # Quan trọng: Buộc Maya/PySide cập nhật giao diện ngay lập tức
            # Nếu không có dòng này, thanh bar sẽ đứng im cho đến khi chạy xong hết
            QtWidgets.QApplication.processEvents()

        self.log(">>> [Done] Xong!")



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

