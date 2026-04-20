"""
1/11/2024
Edit by HOANG TRONG PHI   @HuangFei

Done ,testing Maya 2022 -> 2024
"""
import maya.cmds as cmds
import maya.mel as mel


import sys
import os
import json
import gc   # bắt maya xóa GUI thừa, giải phóng bộ nhớ garbage clear
from maya import OpenMayaUI as omui


#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
Signal = QtCore.Signal

from functools import partial  # passing args during signal function calls

import importlib
import Software.Maya.Toolsets.Working_Toolset.Pivot.model.PivotTool as PivotTool
importlib.reload(PivotTool)

import Software.Maya.Toolsets.Working_Toolset.Pivot.UI.PivotTool_UI as PivotTool_UI
importlib.reload(PivotTool_UI)

def getDirectoryofModule(modulename):

    #Input: module as string
    #OUtput:
        #List: name as string and directory of module

    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = os.path.dirname(module.__file__)
    return currWD
    pass

def getMayaMainWindow():
    """Lấy cửa sổ chính của Maya."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    return None

#####

class HF_PivotTool(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ MeshPosition Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None
    filePath_requested = Signal()

    def __init__(self, parent=getMayaMainWindow()):
        super(HF_PivotTool, self).__init__(parent)

        self.ui = PivotTool_UI.Ui_PivotTool()
        self.ui.setupUi(self)

        ####
        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("PivotTool_window")
        self.setWindowTitle("PivotTool")

        self.createWidgets()
        self.createConnection()
        ###

    def createWidgets(self):
        pass



    # Assign functionally to buttons
    def createConnection(self):
        """
        Your code here
        """

        self.ui.btnGetPosition.clicked.connect(self.getPivot)
        self.ui.btnSetPosition.clicked.connect(self.setPivot)

        self.ui.btnCenterPivot.clicked.connect(self.centerPivot)
        self.ui.btnPivotOriginal.clicked.connect(self.pivotOriginal)

        self.ui.btnCenBotPivot.clicked.connect(self.centerBottomPivot)
        self.ui.btnCenTopPivot.clicked.connect(self.centerTopPivot)

        self.ui.btnSetXmin.clicked.connect(self.setXmin)
        self.ui.btnSetXmid.clicked.connect(self.setXmid)
        self.ui.btnSetXmax.clicked.connect(self.setXmax)

        self.ui.btnSetYmin.clicked.connect(self.setYmin)
        self.ui.btnSetYmid.clicked.connect(self.setYmid)
        self.ui.btnSetYmax.clicked.connect(self.setYmax)

        self.ui.btnSetZmin.clicked.connect(self.setZmin)
        self.ui.btnSetZmid.clicked.connect(self.setZmid)
        self.ui.btnSetZmax.clicked.connect(self.setZmax)
    ########

    def getPivot(self):
        PivotTool.getPivotPosition()

    def setPivot(self):
        PivotTool.setPivotPosition()

    def centerBottomPivot(self):
        PivotTool.centerBottomPivot()

    def centerTopPivot(self):
        PivotTool.centerTopPivot()

    def centerPivot(self):
        PivotTool.centerPivot()

    def pivotOriginal(self):
        PivotTool.pivotOriginal()

    def setXmin(self):
        PivotTool.setXmin()

    def setXmid(self):
        PivotTool.setXmid()

    def setXmax(self):
        PivotTool.setXmax()

    def setYmin(self):
        PivotTool.setYmin()

    def setYmid(self):
        PivotTool.setYmid()

    def setYmax(self):
        PivotTool.setYmax()

    def setZmin(self):
        PivotTool.setZmin()

    def setZmid(self):
        PivotTool.setZmid()

    def setZmax(self):
        PivotTool.setZmax()




def openWindow():
    mayaMainWindow = getMayaMainWindow()
    objectName = "PivotTool_window"
    for widget in mayaMainWindow.findChildren(QtWidgets.QWidget):
        if widget.objectName() == objectName:
            widget.hide()
            widget.setParent(None)
            widget.deleteLater()
    gc.collect()
    mainWin = HF_PivotTool(parent=mayaMainWindow)
    mainWin.setObjectName(objectName)
    mainWin.show()
    return mainWin

openWindow()


