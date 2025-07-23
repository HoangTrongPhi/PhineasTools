"""
3/11/2024
Create by HOANG TRONG PHI   @HuangFei
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
    from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    from shiboken6 import wrapInstance
    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt

from functools import partial  # passing args during signal function calls

import importlib
import Software.Maya.Toolsets.Working_Toolset.Gadget.model.GadgetsTool as GadgetsTool
importlib.reload(GadgetsTool)
from Software.Maya.Toolsets.Working_Toolset.Gadget.model.GadgetsTool import*

try:
    from shiboken2 import wrapInstance
    import maya.cmds as cmds, maya.mel as mel, maya.OpenMayaUI as omui, maya.api.OpenMaya as om
    mainSoftware = 'Maya'
    print ('Import success Maya Module')
except:
    pass

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
UI_Path = os.path.dirname(this_file_directory) + r"\UI\Gadget.ui"


#####

class RG_GadgetsTool(QtWidgets.QWidget):
    window = None  # đang rỗng

    def __init__(self, parent=None):
        """
        Initialize class.

        """
        #initialize window and load UI file
        super(RG_GadgetsTool, self).__init__(parent=parent)

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
        self.setFixedSize(240, 480)
        ### Luu y ten bien button trung voi objectName cua QPushButton trong Qt Design
            # Scene Setup
        self.btnResetWorkspace = self.widget.findChild(QtWidgets.QPushButton, "btnResetWorkspace")
        self.btnSortOutliner = self.widget.findChild(QtWidgets.QPushButton, "btnSortOutliner")
        self.btnCheckAperture = self.widget.findChild(QtWidgets.QPushButton, "btnCheckAperture")
        self.btnScaleRef = self.widget.findChild(QtWidgets.QPushButton, "btnScaleRef")
        self.btnChangeAxis = self.widget.findChild(QtWidgets.QPushButton, "btnChangeAxis")
        self.btnFixMesh = self.widget.findChild(QtWidgets.QPushButton, "btnFixMesh")
            
            # Modeling  
        self.btnComingSoon = self.widget.findChild(QtWidgets.QPushButton, "btnComingSoon")

            # Render
        self.btnComingSoon_2 = self.widget.findChild(QtWidgets.QPushButton, "btnComingSoon_2")
        
    # Assign functionally to buttons
    def createConnection(self):
        """
        Your code here
        """
            # Scene Setup
        self.btnResetWorkspace.clicked.connect(self.demoButton)
        self.btnSortOutliner.clicked.connect(self.demoButton)
        self.btnCheckAperture.clicked.connect(self.demoButton)
        self.btnScaleRef.clicked.connect(self.demoButton)
        self.btnChangeAxis.clicked.connect(self.changeAxis)
        self.btnFixMesh.clicked.connect(self.demoButton)
            
            # Modeling    
        self.btnComingSoon.clicked.connect(self.ComingSoon)
        
        
            # Render
        self.btnComingSoon_2.clicked.connect(self.ComingSoon)

        
    ########
    # Your Function

    def demoButton(self):
        print ("Button Da kich hoat" )


    def ResetWorkspace(self):
       pass


    def changeAxis(self):
        current_up_axis = cmds.upAxis(q=True, axis=True)

        # Check the current up axis and set the opposite
        if current_up_axis == 'y':
            cmds.upAxis(ax='z', rv=True)
        elif current_up_axis == 'z':
            cmds.upAxis(ax='y')

        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis(q=True, axis=True)


    def ComingSoon(self):
        cmds.confirmDialog(title='Warining', message='Tab này sẽ được Cập nhật sau', ) 



def openWindow():  # Create UI

    """
    ID Maya and attach tool window.
    """

    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
        #for win in QtWidgets.QApplication.allWindows():
            if "MainWindow" in win.objectName():
                win.destroy()

    # QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    RG_GadgetsTool.window = RG_GadgetsTool(parent=mayaMainWindow)
    RG_GadgetsTool.window.setObjectName("MainWindow")
    RG_GadgetsTool.window.setWindowTitle("RG Gadgets Tool")
    RG_GadgetsTool.window.show()

openWindow()


