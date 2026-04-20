# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeleportTool_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

QWidget = QtWidgets.QWidget
QFrame = QtWidgets.QFrame
QSizePolicy = QtWidgets.QSizePolicy
QVBoxLayout = QtWidgets.QVBoxLayout
QLabel = QtWidgets.QLabel
QPushButton = QtWidgets.QPushButton
QRect = QtCore.QRect
QCoreApplication = QtCore.QCoreApplication
QMetaObject = QtCore.QMetaObject
Qt = QtCore.Qt
QLayout = QtWidgets.QLayout
try:
    QAction = QtGui.QAction
except:
    QAction = QtWidgets.QAction

QComboBox = QtWidgets.QComboBox
QListView = QtWidgets.QListView
QTreeView = QtWidgets.QTreeView
QTableWidget = QtWidgets.QTableWidget
QRadioButton = QtWidgets.QRadioButton
QMenuBar = QtWidgets.QMenuBar
QMenu = QtWidgets.QMenu
QCheckBox = QtWidgets.QCheckBox
QStatusBar = QtWidgets.QStatusBar
QFont = QtGui.QFont
QTextEdit = QtWidgets.QTextEdit


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(410, 671)
        font = QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.HF_author = QLabel(self.centralwidget)
        self.HF_author.setObjectName(u"HF_author")
        self.HF_author.setGeometry(QRect(12, 590, 66, 16))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(False)
        self.HF_author.setFont(font1)
        self.HF_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:9pt \"Bahnschrift SemiBold SemiConden\";")
        self.btnFAQs_all = QPushButton(self.centralwidget)
        self.btnFAQs_all.setObjectName(u"btnFAQs_all")
        self.btnFAQs_all.setGeometry(QRect(380, 0, 25, 23))
        self.btnImptMaya = QPushButton(self.centralwidget)
        self.btnImptMaya.setObjectName(u"btnImptMaya")
        self.btnImptMaya.setGeometry(QRect(13, 40, 185, 64))
        self.btnImptMaya.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExptShare = QPushButton(self.centralwidget)
        self.btnExptShare.setObjectName(u"btnExptShare")
        self.btnExptShare.setGeometry(QRect(6, 340, 137, 44))
        self.btnExptShare.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExportExplore = QPushButton(self.centralwidget)
        self.btnExportExplore.setObjectName(u"btnExportExplore")
        self.btnExportExplore.setGeometry(QRect(10, 159, 36, 36))
        self.btnExportExplore.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExptOBJ = QPushButton(self.centralwidget)
        self.btnExptOBJ.setObjectName(u"btnExptOBJ")
        self.btnExptOBJ.setGeometry(QRect(9, 204, 88, 44))
        self.btnExptOBJ.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_MayaBlender = QLabel(self.centralwidget)
        self.label_MayaBlender.setObjectName(u"label_MayaBlender")
        self.label_MayaBlender.setGeometry(QRect(10, 10, 133, 20))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(False)
        self.label_MayaBlender.setFont(font2)
        self.label_MayaBlender.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnOpenExplore = QPushButton(self.centralwidget)
        self.btnOpenExplore.setObjectName(u"btnOpenExplore")
        self.btnOpenExplore.setGeometry(QRect(276, 160, 124, 36))
        self.btnOpenExplore.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnFAQs_export = QPushButton(self.centralwidget)
        self.btnFAQs_export.setObjectName(u"btnFAQs_export")
        self.btnFAQs_export.setGeometry(QRect(377, 132, 25, 23))
        self.textEditPath = QTextEdit(self.centralwidget)
        self.textEditPath.setObjectName(u"textEditPath")
        self.textEditPath.setGeometry(QRect(50, 160, 220, 36))
        self.btExptBlender = QPushButton(self.centralwidget)
        self.btExptBlender.setObjectName(u"btExptBlender")
        self.btExptBlender.setGeometry(QRect(203, 40, 185, 64))
        self.btExptBlender.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_Advanced = QLabel(self.centralwidget)
        self.label_Advanced.setObjectName(u"label_Advanced")
        self.label_Advanced.setGeometry(QRect(10, 140, 74, 20))
        self.label_Advanced.setFont(font2)
        self.label_Advanced.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(0, 110, 400, 16))
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnExptUSD = QPushButton(self.centralwidget)
        self.btnExptUSD.setObjectName(u"btnExptUSD")
        self.btnExptUSD.setGeometry(QRect(107, 204, 88, 44))
        self.btnExptUSD.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_Share = QLabel(self.centralwidget)
        self.label_Share.setObjectName(u"label_Share")
        self.label_Share.setGeometry(QRect(9, 310, 147, 20))
        self.label_Share.setFont(font2)
        self.label_Share.setStyleSheet(u"color: rgb(128, 80, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1, 260, 400, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnImptShare = QPushButton(self.centralwidget)
        self.btnImptShare.setObjectName(u"btnImptShare")
        self.btnImptShare.setGeometry(QRect(147, 340, 168, 44))
        self.btnImptShare.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnShareExplore = QPushButton(self.centralwidget)
        self.btnShareExplore.setObjectName(u"btnShareExplore")
        self.btnShareExplore.setGeometry(QRect(318, 340, 81, 44))
        self.btnShareExplore.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_TeleEngine = QLabel(self.centralwidget)
        self.label_TeleEngine.setObjectName(u"label_TeleEngine")
        self.label_TeleEngine.setGeometry(QRect(10, 421, 133, 20))
        self.label_TeleEngine.setFont(font2)
        self.label_TeleEngine.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnImptMayaEngine = QPushButton(self.centralwidget)
        self.btnImptMayaEngine.setObjectName(u"btnImptMayaEngine")
        self.btnImptMayaEngine.setGeometry(QRect(25, 449, 119, 44))
        self.btnImptMayaEngine.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExptUE = QPushButton(self.centralwidget)
        self.btnExptUE.setObjectName(u"btnExptUE")
        self.btnExptUE.setGeometry(QRect(151, 449, 137, 44))
        self.btnExptUE.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnFAQs_export_2 = QPushButton(self.centralwidget)
        self.btnFAQs_export_2.setObjectName(u"btnFAQs_export_2")
        self.btnFAQs_export_2.setGeometry(QRect(375, 423, 25, 23))
        self.btnExptUnity = QPushButton(self.centralwidget)
        self.btnExptUnity.setObjectName(u"btnExptUnity")
        self.btnExptUnity.setGeometry(QRect(150, 503, 137, 44))
        self.btnExptUnity.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnEnginePath = QPushButton(self.centralwidget)
        self.btnEnginePath.setObjectName(u"btnEnginePath")
        self.btnEnginePath.setGeometry(QRect(352, 449, 45, 44))
        self.btnEnginePath.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 569, 400, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnMaterialsTool = QPushButton(self.centralwidget)
        self.btnMaterialsTool.setObjectName(u"btnMaterialsTool")
        self.btnMaterialsTool.setGeometry(QRect(353, 504, 45, 44))
        self.btnMaterialsTool.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 410, 33))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.HF_author.setText(QCoreApplication.translate("mainWindow", u"@HuangFei", None))
        self.btnFAQs_all.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnImptMaya.setText(QCoreApplication.translate("mainWindow", u"Import to Maya", None))
        self.btnExptShare.setText(QCoreApplication.translate("mainWindow", u"Export SHARE", None))
        self.btnExportExplore.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.btnExptOBJ.setText(QCoreApplication.translate("mainWindow", u"OBJ", None))
        self.label_MayaBlender.setText(QCoreApplication.translate("mainWindow", u"MAYA ----- BLENDER", None))
        self.btnOpenExplore.setText(QCoreApplication.translate("mainWindow", u"Explore", None))
        self.btnFAQs_export.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btExptBlender.setText(QCoreApplication.translate("mainWindow", u"Export to Blender", None))
        self.label_Advanced.setText(QCoreApplication.translate("mainWindow", u"ADVANCED", None))
        self.btnExptUSD.setText(QCoreApplication.translate("mainWindow", u"USD", None))
        self.label_Share.setText(QCoreApplication.translate("mainWindow", u"Share file to another one", None))
        self.btnImptShare.setText(QCoreApplication.translate("mainWindow", u"Import SHARE", None))
        self.btnShareExplore.setText(QCoreApplication.translate("mainWindow", u"Explore", None))
        self.label_TeleEngine.setText(QCoreApplication.translate("mainWindow", u"TELEPORT TO ENGINE", None))
        self.btnImptMayaEngine.setText(QCoreApplication.translate("mainWindow", u"Import to Maya", None))
        self.btnExptUE.setText(QCoreApplication.translate("mainWindow", u"Export to Unreal", None))
        self.btnFAQs_export_2.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnExptUnity.setText(QCoreApplication.translate("mainWindow", u"Export to UNITY", None))
        self.btnEnginePath.setText(QCoreApplication.translate("mainWindow", u"path", None))
        self.btnMaterialsTool.setText(QCoreApplication.translate("mainWindow", u"Mat", None))
    # retranslateUi

