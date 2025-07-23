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

from maya import OpenMayaUI as omui
from select import select

try:
    from shiboken2 import wrapInstance
    from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QIODevice
    from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    from shiboken6 import wrapInstance
    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt


from functools import partial  # passing args during signal function calls

import importlib
import Software.Maya.Toolsets.Working_Toolset.Pivot.model.PivotTool as PivotTool
importlib.reload(PivotTool)
from Software.Maya.Toolsets.Working_Toolset.Pivot.model.PivotTool import*


def getDirectoryofModule(modulename):

    #Input: module as string
    #OUtput:
        #List: name as string and directory of module

    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = CommonPyFunction.Get_WD(module.__file__)
    return currWD
    pass


this_file_directory = os.path.dirname(__file__)
main_directory = os.path.dirname(this_file_directory)

data = os.path.dirname(this_file_directory) + r"\model\data"
UI_Path = os.path.dirname(this_file_directory) + r"\UI\PivotTool.ui"


#####

class HF_PivotTool(QtWidgets.QWidget):
    window = None  # đang rỗng

    def __init__(self, parent=None):
        """
        Initialize class.

        """
        #initialize window and load UI file
        super(HF_PivotTool, self).__init__(parent=parent)

        ####
        self.createWidgets()
        self.createConnection()
        ###

    def createWidgets(self):

        self.checkerBoxOpt = QtWidgets.QAbstractButton
        self.setWindowFlags(QtCore.Qt.Window)
        self.widget = QtUiTools.QUiLoader().load(UI_Path)
        self.widget.setParent(self)
            # set initial window size
        self.setFixedSize(360, 480)
        ### Luu y ten bien button trung voi objectName cua QPushButton trong Qt Design
        
        self.btnGetPosition = self.widget.findChild(QtWidgets.QPushButton, "btnGetPosition")
        self.btnSetPosition = self.widget.findChild(QtWidgets.QPushButton, "btnSetPosition")

        self.btnCenterPivot = self.widget.findChild(QtWidgets.QPushButton, "btnCenterPivot")
        self.btnPivotOriginal = self.widget.findChild(QtWidgets.QPushButton, "btnPivotOriginal")

        self.btnCenBotPivot = self.widget.findChild(QtWidgets.QPushButton, "btnCenBotPivot")
        self.btnCenTopPivot = self.widget.findChild(QtWidgets.QPushButton, "btnCenTopPivot")

        self.btnSetXmin = self.widget.findChild(QtWidgets.QPushButton, "btnSetXmin")
        self.btnSetXmid = self.widget.findChild(QtWidgets.QPushButton, "btnSetXmid")
        self.btnSetXmax = self.widget.findChild(QtWidgets.QPushButton, "btnSetXmax")

        self.btnSetYmin = self.widget.findChild(QtWidgets.QPushButton, "btnSetYmin")
        self.btnSetYmid = self.widget.findChild(QtWidgets.QPushButton, "btnSetYmid")
        self.btnSetYmax = self.widget.findChild(QtWidgets.QPushButton, "btnSetYmax")

        self.btnSetZmin = self.widget.findChild(QtWidgets.QPushButton, "btnSetZmin")
        self.btnSetZmid = self.widget.findChild(QtWidgets.QPushButton, "btnSetZmid")
        self.btnSetZmax = self.widget.findChild(QtWidgets.QPushButton, "btnSetZmax")



    # Assign functionally to buttons
    def createConnection(self):
        """
        Your code here
        """

        self.btnGetPosition.clicked.connect(self.getPivot)
        self.btnSetPosition.clicked.connect(self.setPivot)

        self.btnCenterPivot.clicked.connect(self.centerPivot)
        self.btnPivotOriginal.clicked.connect(self.pivotOriginal)

        self.btnCenBotPivot.clicked.connect(self.centerBottomPivot)
        self.btnCenTopPivot.clicked.connect(self.centerTopPivot)

        self.btnSetXmin.clicked.connect(self.setXmin)
        self.btnSetXmid.clicked.connect(self.setXmid)
        self.btnSetXmax.clicked.connect(self.setXmax)

        self.btnSetYmin.clicked.connect(self.setYmin)
        self.btnSetYmid.clicked.connect(self.setYmid)
        self.btnSetYmax.clicked.connect(self.setYmax)

        self.btnSetZmin.clicked.connect(self.setZmin)
        self.btnSetZmid.clicked.connect(self.setZmid)
        self.btnSetZmax.clicked.connect(self.setZmax)
    ########

    def getPivot(self):
        getPivotPosition()

    def setPivot(self):
        setPivotPosition()

    def centerBottomPivot(self):
        centerBottomPivot()

    def centerTopPivot(self):
        centerTopPivot()

    def centerPivot(self):
        centerPivot()

    def pivotOriginal(self):
        pivotOriginal()

    def setXmin(self):
        setXmin()

    def setXmid(self):
        setXmid()

    def setXmax(self):
        setXmax()

    def setYmin(self):
        setYmin()

    def setYmid(self):
        setYmid()

    def setYmax(self):
        setYmax()

    def setZmin(self):
        setZmin()

    def setZmid(self):
        setZmid()

    def setZmax(self):
        setZmax()




def openWindow():  # Create UI

    """
    ID Maya and attach tool window.
    """
    # nên hiểu khái niệm object trong code là "Thực thể" thay vì "vật thể"
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy, chỉ 1 window được tồn tại
        for win in QtWidgets.QApplication.allWindows():
            if "MainWindow" in win.objectName():
                win.destroy()

    # QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    HF_PivotTool.window = HF_PivotTool(parent=mayaMainWindow)
    HF_PivotTool.window.setObjectName("MainWindow")
    HF_PivotTool.window.setWindowTitle("HF PivotTool")
    HF_PivotTool.window.show()

openWindow()


