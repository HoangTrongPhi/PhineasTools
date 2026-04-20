# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PivotTool_UI.ui'
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

class Ui_PivotTool(object):
    def setupUi(self, PivotTool):
        if not PivotTool.objectName():
            PivotTool.setObjectName(u"PivotTool")
        PivotTool.resize(360, 501)
        PivotTool.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(PivotTool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.author = QLabel(self.centralwidget)
        self.author.setObjectName(u"author")
        self.author.setGeometry(QRect(12, 420, 68, 16))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font.setPointSize(9)
        font.setWeight(QFont.Bold)
        font.setItalic(False)
        font.setKerning(False)
        self.author.setFont(font)
        self.author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font: 63 9pt \"Bahnschrift SemiBold SemiConden\";")
        self.btnGetPosition = QPushButton(self.centralwidget)
        self.btnGetPosition.setObjectName(u"btnGetPosition")
        self.btnGetPosition.setGeometry(QRect(9, 50, 171, 42))
        self.btnGetPosition.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(80, 98, 170);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(80, 98, 170);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(87, 138, 207);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetPosition = QPushButton(self.centralwidget)
        self.btnSetPosition.setObjectName(u"btnSetPosition")
        self.btnSetPosition.setGeometry(QRect(190, 50, 159, 41))
        self.btnSetPosition.setStyleSheet(u"QPushButton {font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(170, 80, 143);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 80, 143);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(119, 29, 65);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetXmin = QPushButton(self.centralwidget)
        self.btnSetXmin.setObjectName(u"btnSetXmin")
        self.btnSetXmin.setGeometry(QRect(9, 301, 102, 32))
        self.btnSetXmin.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(170, 80, 107);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(170, 80, 107);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(169, 23, 27);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetXmid = QPushButton(self.centralwidget)
        self.btnSetXmid.setObjectName(u"btnSetXmid")
        self.btnSetXmid.setGeometry(QRect(120, 301, 113, 34))
        self.btnSetXmid.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(170, 80, 107);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:   rgb(170, 80, 107);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(169, 23, 27);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetXmax = QPushButton(self.centralwidget)
        self.btnSetXmax.setObjectName(u"btnSetXmax")
        self.btnSetXmax.setGeometry(QRect(240, 301, 107, 34))
        self.btnSetXmax.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(170, 80, 107);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:   rgb(170, 80, 107);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(169, 23, 27);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetYmin = QPushButton(self.centralwidget)
        self.btnSetYmin.setObjectName(u"btnSetYmin")
        self.btnSetYmin.setGeometry(QRect(9, 341, 102, 32))
        self.btnSetYmin.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(80, 170, 89);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color: rgb(80, 170, 89);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(180, 220, 103);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetYmid = QPushButton(self.centralwidget)
        self.btnSetYmid.setObjectName(u"btnSetYmid")
        self.btnSetYmid.setGeometry(QRect(120, 341, 112, 34))
        self.btnSetYmid.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(80, 170, 89);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color: rgb(80, 170, 89);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(180, 220, 103);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetYmax = QPushButton(self.centralwidget)
        self.btnSetYmax.setObjectName(u"btnSetYmax")
        self.btnSetYmax.setGeometry(QRect(240, 341, 107, 34))
        self.btnSetYmax.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(80, 170, 89);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color: rgb(80, 170, 89);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(180, 220, 103);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetZmax = QPushButton(self.centralwidget)
        self.btnSetZmax.setObjectName(u"btnSetZmax")
        self.btnSetZmax.setGeometry(QRect(240, 380, 107, 34))
        self.btnSetZmax.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(109, 141, 185);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:   rgb(109, 141, 185);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(87, 138, 207);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetZmin = QPushButton(self.centralwidget)
        self.btnSetZmin.setObjectName(u"btnSetZmin")
        self.btnSetZmin.setGeometry(QRect(10, 379, 100, 35))
        self.btnSetZmin.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(109, 141, 185);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:   rgb(109, 141, 185);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(87, 138, 207);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetZmid = QPushButton(self.centralwidget)
        self.btnSetZmid.setObjectName(u"btnSetZmid")
        self.btnSetZmid.setGeometry(QRect(120, 380, 113, 34))
        self.btnSetZmid.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color:  rgb(109, 141, 185);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:   rgb(109, 141, 185);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(87, 138, 207);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnCenBotPivot = QPushButton(self.centralwidget)
        self.btnCenBotPivot.setObjectName(u"btnCenBotPivot")
        self.btnCenBotPivot.setGeometry(QRect(10, 201, 169, 42))
        self.btnCenBotPivot.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnCenBotPivot.setAutoDefault(False)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(13, 250, 331, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnCenTopPivot = QPushButton(self.centralwidget)
        self.btnCenTopPivot.setObjectName(u"btnCenTopPivot")
        self.btnCenTopPivot.setGeometry(QRect(190, 200, 158, 44))
        self.btnCenTopPivot.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnPivotOriginal = QPushButton(self.centralwidget)
        self.btnPivotOriginal.setObjectName(u"btnPivotOriginal")
        self.btnPivotOriginal.setGeometry(QRect(190, 153, 159, 39))
        self.btnPivotOriginal.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnCenterPivot = QPushButton(self.centralwidget)
        self.btnCenterPivot.setObjectName(u"btnCenterPivot")
        self.btnCenterPivot.setGeometry(QRect(10, 153, 169, 39))
        self.btnCenterPivot.setStyleSheet(u"QPushButton {\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(12, 20, 332, 20))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Bold)
        font1.setItalic(False)
        font1.setKerning(False)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font: 63 12pt  \"Bahnschrift SemiBold SemiConden\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 332, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 100, 332, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 270, 332, 20))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        PivotTool.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PivotTool)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 360, 33))
        PivotTool.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PivotTool)
        self.statusbar.setObjectName(u"statusbar")
        PivotTool.setStatusBar(self.statusbar)

        self.retranslateUi(PivotTool)

        self.btnCenBotPivot.setDefault(False)


        QMetaObject.connectSlotsByName(PivotTool)
    # setupUi

    def retranslateUi(self, PivotTool):
        PivotTool.setWindowTitle(QCoreApplication.translate("PivotTool", u"MainWindow", None))
        self.author.setText(QCoreApplication.translate("PivotTool", u"@HuangFei", None))
        self.btnGetPosition.setText(QCoreApplication.translate("PivotTool", u"Get Position", None))
        self.btnSetPosition.setText(QCoreApplication.translate("PivotTool", u"Set Position", None))
        self.btnSetXmin.setText(QCoreApplication.translate("PivotTool", u"Set Xmin", None))
        self.btnSetXmid.setText(QCoreApplication.translate("PivotTool", u"Set Xmid", None))
        self.btnSetXmax.setText(QCoreApplication.translate("PivotTool", u"Set Xmax", None))
        self.btnSetYmin.setText(QCoreApplication.translate("PivotTool", u"Set Ymin", None))
        self.btnSetYmid.setText(QCoreApplication.translate("PivotTool", u"Set Ymid", None))
        self.btnSetYmax.setText(QCoreApplication.translate("PivotTool", u"Set Ymax", None))
        self.btnSetZmax.setText(QCoreApplication.translate("PivotTool", u"Set Zmax", None))
        self.btnSetZmin.setText(QCoreApplication.translate("PivotTool", u"Set Zmin", None))
        self.btnSetZmid.setText(QCoreApplication.translate("PivotTool", u"Set Zmid", None))
        self.btnCenBotPivot.setText(QCoreApplication.translate("PivotTool", u"Center Bottom Pivot", None))
        self.btnCenTopPivot.setText(QCoreApplication.translate("PivotTool", u"CenterTop Pivot", None))
        self.btnPivotOriginal.setText(QCoreApplication.translate("PivotTool", u"Pivot Original", None))
        self.btnCenterPivot.setText(QCoreApplication.translate("PivotTool", u"Center Pivot", None))
        self.label_1.setText(QCoreApplication.translate("PivotTool", u"Copy Pivot Position", None))
        self.label_2.setText(QCoreApplication.translate("PivotTool", u"Basic Pivot Position", None))
        self.label_3.setText(QCoreApplication.translate("PivotTool", u"Advanced Pivot Position", None))
    # retranslateUi

