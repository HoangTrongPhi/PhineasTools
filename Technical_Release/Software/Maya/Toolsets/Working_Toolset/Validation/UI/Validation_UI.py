# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Validation_UI.ui'
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
QHBoxLayout = QtWidgets.QHBoxLayout
QTreeWidget = QtWidgets.QTreeWidget
QSpacerItem = QtWidgets.QSpacerItem
QSize = QtCore.QSize
QProgressBar = QtWidgets.QProgressBar

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1001, 709)
        font = QFont()
        font.setBold(False)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.act_Export_INFOR = QAction(mainWindow)
        self.act_Export_INFOR.setObjectName(u"act_Export_INFOR")
        self.act_Open_Explore = QAction(mainWindow)
        self.act_Open_Explore.setObjectName(u"act_Open_Explore")
        self.act_Refresh_Tool = QAction(mainWindow)
        self.act_Refresh_Tool.setObjectName(u"act_Refresh_Tool")
        self.act_Geo = QAction(mainWindow)
        self.act_Geo.setObjectName(u"act_Geo")
        self.act_UV = QAction(mainWindow)
        self.act_UV.setObjectName(u"act_UV")
        self.act_Texture = QAction(mainWindow)
        self.act_Texture.setObjectName(u"act_Texture")
        self.act_Naming = QAction(mainWindow)
        self.act_Naming.setObjectName(u"act_Naming")
        self.act_Scene = QAction(mainWindow)
        self.act_Scene.setObjectName(u"act_Scene")
        self.act_GameReady = QAction(mainWindow)
        self.act_GameReady.setObjectName(u"act_GameReady")
        self.act_GeoHelp = QAction(mainWindow)
        self.act_GeoHelp.setObjectName(u"act_GeoHelp")
        self.act_UVHelp = QAction(mainWindow)
        self.act_UVHelp.setObjectName(u"act_UVHelp")
        self.act_TexHelp = QAction(mainWindow)
        self.act_TexHelp.setObjectName(u"act_TexHelp")
        self.act_NamingHelp = QAction(mainWindow)
        self.act_NamingHelp.setObjectName(u"act_NamingHelp")
        self.act_SceneHelp = QAction(mainWindow)
        self.act_SceneHelp.setObjectName(u"act_SceneHelp")
        self.act_UnrealHelp = QAction(mainWindow)
        self.act_UnrealHelp.setObjectName(u"act_UnrealHelp")
        self.act_UnityHelp = QAction(mainWindow)
        self.act_UnityHelp.setObjectName(u"act_UnityHelp")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.HF_author = QLabel(self.centralwidget)
        self.HF_author.setObjectName(u"HF_author")
        self.HF_author.setGeometry(QRect(12, 640, 66, 16))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(False)
        self.HF_author.setFont(font1)
        self.HF_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:9pt \"Bahnschrift SemiBold SemiConden\";")
        self.btnFAQs = QPushButton(self.centralwidget)
        self.btnFAQs.setObjectName(u"btnFAQs")
        self.btnFAQs.setGeometry(QRect(966, 1, 25, 23))
        self.btnRefreshTool = QPushButton(self.centralwidget)
        self.btnRefreshTool.setObjectName(u"btnRefreshTool")
        self.btnRefreshTool.setGeometry(QRect(800, 317, 194, 35))
        self.btnRefreshTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")
        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(21, 612, 978, 20))
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_Console = QLabel(self.centralwidget)
        self.lbl_Console.setObjectName(u"lbl_Console")
        self.lbl_Console.setGeometry(QRect(635, 9, 91, 20))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(False)
        self.lbl_Console.setFont(font2)
        self.lbl_Console.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_AnotherTools = QLabel(self.centralwidget)
        self.lbl_AnotherTools.setObjectName(u"lbl_AnotherTools")
        self.lbl_AnotherTools.setGeometry(QRect(378, 333, 133, 20))
        self.lbl_AnotherTools.setFont(font2)
        self.lbl_AnotherTools.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Tips = QLabel(self.centralwidget)
        self.lbl_Tips.setObjectName(u"lbl_Tips")
        self.lbl_Tips.setGeometry(QRect(373, 587, 327, 29))
        self.lbl_Tips.setFont(font2)
        self.lbl_Tips.setStyleSheet(u"color: rgb(255, 180, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.txEd_Console = QTextEdit(self.centralwidget)
        self.txEd_Console.setObjectName(u"txEd_Console")
        self.txEd_Console.setGeometry(QRect(634, 30, 364, 278))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 29, 321, 97))
        self.horizontalLayout_geo = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_geo.setObjectName(u"horizontalLayout_geo")
        self.horizontalLayout_geo.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_geo_01 = QVBoxLayout()
        self.verticalLayout_geo_01.setSpacing(4)
        self.verticalLayout_geo_01.setObjectName(u"verticalLayout_geo_01")
        self.chbx_ConcaveFaces = QCheckBox(self.horizontalLayoutWidget)
        self.chbx_ConcaveFaces.setObjectName(u"chbx_ConcaveFaces")

        self.verticalLayout_geo_01.addWidget(self.chbx_ConcaveFaces)

        self.chbx_LanimaFaces = QCheckBox(self.horizontalLayoutWidget)
        self.chbx_LanimaFaces.setObjectName(u"chbx_LanimaFaces")

        self.verticalLayout_geo_01.addWidget(self.chbx_LanimaFaces)

        self.chbx_NonManifold = QCheckBox(self.horizontalLayoutWidget)
        self.chbx_NonManifold.setObjectName(u"chbx_NonManifold")

        self.verticalLayout_geo_01.addWidget(self.chbx_NonManifold)

        self.chbx_ZeroEdge = QCheckBox(self.horizontalLayoutWidget)
        self.chbx_ZeroEdge.setObjectName(u"chbx_ZeroEdge")

        self.verticalLayout_geo_01.addWidget(self.chbx_ZeroEdge)


        self.horizontalLayout_geo.addLayout(self.verticalLayout_geo_01)

        self.verticalLayout_geo_02 = QVBoxLayout()
        self.verticalLayout_geo_02.setObjectName(u"verticalLayout_geo_02")
        self.fr_ConcaveFaces = QFrame(self.horizontalLayoutWidget)
        self.fr_ConcaveFaces.setObjectName(u"fr_ConcaveFaces")
        self.fr_ConcaveFaces.setMinimumSize(QSize(18, 18))
        self.fr_ConcaveFaces.setMaximumSize(QSize(18, 18))
        font3 = QFont()
        font3.setStyleStrategy(QFont.PreferDefault)
        self.fr_ConcaveFaces.setFont(font3)
        self.fr_ConcaveFaces.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_ConcaveFaces.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ConcaveFaces.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_geo_02.addWidget(self.fr_ConcaveFaces)

        self.fr_LaminaFaces = QFrame(self.horizontalLayoutWidget)
        self.fr_LaminaFaces.setObjectName(u"fr_LaminaFaces")
        self.fr_LaminaFaces.setMinimumSize(QSize(18, 18))
        self.fr_LaminaFaces.setMaximumSize(QSize(18, 18))
        self.fr_LaminaFaces.setFont(font3)
        self.fr_LaminaFaces.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_LaminaFaces.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_LaminaFaces.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_geo_02.addWidget(self.fr_LaminaFaces)

        self.fr_NonManifold = QFrame(self.horizontalLayoutWidget)
        self.fr_NonManifold.setObjectName(u"fr_NonManifold")
        self.fr_NonManifold.setMinimumSize(QSize(18, 18))
        self.fr_NonManifold.setMaximumSize(QSize(18, 18))
        self.fr_NonManifold.setFont(font3)
        self.fr_NonManifold.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_NonManifold.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_NonManifold.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_geo_02.addWidget(self.fr_NonManifold)

        self.fr_ZeroEdge = QFrame(self.horizontalLayoutWidget)
        self.fr_ZeroEdge.setObjectName(u"fr_ZeroEdge")
        self.fr_ZeroEdge.setMinimumSize(QSize(18, 18))
        self.fr_ZeroEdge.setMaximumSize(QSize(18, 18))
        self.fr_ZeroEdge.setFont(font3)
        self.fr_ZeroEdge.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_ZeroEdge.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ZeroEdge.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_geo_02.addWidget(self.fr_ZeroEdge)


        self.horizontalLayout_geo.addLayout(self.verticalLayout_geo_02)

        self.verticalLayout_geo_03 = QVBoxLayout()
        self.verticalLayout_geo_03.setObjectName(u"verticalLayout_geo_03")
        self.btnCh_ConcaveFaces = QPushButton(self.horizontalLayoutWidget)
        self.btnCh_ConcaveFaces.setObjectName(u"btnCh_ConcaveFaces")
        self.btnCh_ConcaveFaces.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_geo_03.addWidget(self.btnCh_ConcaveFaces)

        self.btnCh_LaminaFaces = QPushButton(self.horizontalLayoutWidget)
        self.btnCh_LaminaFaces.setObjectName(u"btnCh_LaminaFaces")
        self.btnCh_LaminaFaces.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_geo_03.addWidget(self.btnCh_LaminaFaces)

        self.btnCh_NonManifold = QPushButton(self.horizontalLayoutWidget)
        self.btnCh_NonManifold.setObjectName(u"btnCh_NonManifold")
        self.btnCh_NonManifold.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_geo_03.addWidget(self.btnCh_NonManifold)

        self.btnCh_ZeroEdge = QPushButton(self.horizontalLayoutWidget)
        self.btnCh_ZeroEdge.setObjectName(u"btnCh_ZeroEdge")
        self.btnCh_ZeroEdge.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_geo_03.addWidget(self.btnCh_ZeroEdge)


        self.horizontalLayout_geo.addLayout(self.verticalLayout_geo_03)

        self.horizontalLayout_geo.setStretch(0, 1)
        self.lbl_Geo = QLabel(self.centralwidget)
        self.lbl_Geo.setObjectName(u"lbl_Geo")
        self.lbl_Geo.setGeometry(QRect(12, 8, 124, 21))
        self.lbl_Geo.setFont(font2)
        self.lbl_Geo.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_UV = QLabel(self.centralwidget)
        self.lbl_UV.setObjectName(u"lbl_UV")
        self.lbl_UV.setGeometry(QRect(12, 129, 155, 18))
        self.lbl_UV.setFont(font2)
        self.lbl_UV.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 147, 320, 76))
        self.horizontalLayout_uv = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_uv.setObjectName(u"horizontalLayout_uv")
        self.horizontalLayout_uv.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_uv_01 = QVBoxLayout()
        self.verticalLayout_uv_01.setObjectName(u"verticalLayout_uv_01")
        self.chbx_MisUV = QCheckBox(self.horizontalLayoutWidget_2)
        self.chbx_MisUV.setObjectName(u"chbx_MisUV")

        self.verticalLayout_uv_01.addWidget(self.chbx_MisUV)

        self.chbx_MoreUV = QCheckBox(self.horizontalLayoutWidget_2)
        self.chbx_MoreUV.setObjectName(u"chbx_MoreUV")

        self.verticalLayout_uv_01.addWidget(self.chbx_MoreUV)

        self.chbx_OverlapUV = QCheckBox(self.horizontalLayoutWidget_2)
        self.chbx_OverlapUV.setObjectName(u"chbx_OverlapUV")

        self.verticalLayout_uv_01.addWidget(self.chbx_OverlapUV)


        self.horizontalLayout_uv.addLayout(self.verticalLayout_uv_01)

        self.verticalLayout_uv_02 = QVBoxLayout()
        self.verticalLayout_uv_02.setObjectName(u"verticalLayout_uv_02")
        self.fr_MisUV = QFrame(self.horizontalLayoutWidget_2)
        self.fr_MisUV.setObjectName(u"fr_MisUV")
        self.fr_MisUV.setMinimumSize(QSize(18, 18))
        self.fr_MisUV.setMaximumSize(QSize(18, 18))
        self.fr_MisUV.setFont(font3)
        self.fr_MisUV.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_MisUV.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_MisUV.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_uv_02.addWidget(self.fr_MisUV)

        self.fr_MoreUV = QFrame(self.horizontalLayoutWidget_2)
        self.fr_MoreUV.setObjectName(u"fr_MoreUV")
        self.fr_MoreUV.setMinimumSize(QSize(18, 18))
        self.fr_MoreUV.setMaximumSize(QSize(18, 18))
        self.fr_MoreUV.setFont(font3)
        self.fr_MoreUV.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_MoreUV.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_MoreUV.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_uv_02.addWidget(self.fr_MoreUV)

        self.fr_OverlapUV = QFrame(self.horizontalLayoutWidget_2)
        self.fr_OverlapUV.setObjectName(u"fr_OverlapUV")
        self.fr_OverlapUV.setMinimumSize(QSize(18, 18))
        self.fr_OverlapUV.setMaximumSize(QSize(18, 18))
        self.fr_OverlapUV.setFont(font3)
        self.fr_OverlapUV.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_OverlapUV.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_OverlapUV.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_uv_02.addWidget(self.fr_OverlapUV)


        self.horizontalLayout_uv.addLayout(self.verticalLayout_uv_02)

        self.verticalLayout_uv_03 = QVBoxLayout()
        self.verticalLayout_uv_03.setObjectName(u"verticalLayout_uv_03")
        self.btnCh_MisUV = QPushButton(self.horizontalLayoutWidget_2)
        self.btnCh_MisUV.setObjectName(u"btnCh_MisUV")
        self.btnCh_MisUV.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_uv_03.addWidget(self.btnCh_MisUV)

        self.btnCh_MoreUV = QPushButton(self.horizontalLayoutWidget_2)
        self.btnCh_MoreUV.setObjectName(u"btnCh_MoreUV")
        self.btnCh_MoreUV.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_uv_03.addWidget(self.btnCh_MoreUV)

        self.btnCh_Overlap = QPushButton(self.horizontalLayoutWidget_2)
        self.btnCh_Overlap.setObjectName(u"btnCh_Overlap")
        self.btnCh_Overlap.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_uv_03.addWidget(self.btnCh_Overlap)


        self.horizontalLayout_uv.addLayout(self.verticalLayout_uv_03)

        self.horizontalLayout_uv.setStretch(0, 1)
        self.lbl_Texture = QLabel(self.centralwidget)
        self.lbl_Texture.setObjectName(u"lbl_Texture")
        self.lbl_Texture.setGeometry(QRect(13, 232, 155, 16))
        self.lbl_Texture.setFont(font2)
        self.lbl_Texture.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 249, 319, 80))
        self.horizontalLayout_tex = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_tex.setObjectName(u"horizontalLayout_tex")
        self.horizontalLayout_tex.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_tex_01 = QVBoxLayout()
        self.verticalLayout_tex_01.setObjectName(u"verticalLayout_tex_01")
        self.chbx_MissingTextures = QCheckBox(self.horizontalLayoutWidget_3)
        self.chbx_MissingTextures.setObjectName(u"chbx_MissingTextures")

        self.verticalLayout_tex_01.addWidget(self.chbx_MissingTextures)

        self.chbx_InvalidTexturePath = QCheckBox(self.horizontalLayoutWidget_3)
        self.chbx_InvalidTexturePath.setObjectName(u"chbx_InvalidTexturePath")

        self.verticalLayout_tex_01.addWidget(self.chbx_InvalidTexturePath)

        self.chbx_UnusedMaterials = QCheckBox(self.horizontalLayoutWidget_3)
        self.chbx_UnusedMaterials.setObjectName(u"chbx_UnusedMaterials")

        self.verticalLayout_tex_01.addWidget(self.chbx_UnusedMaterials)


        self.horizontalLayout_tex.addLayout(self.verticalLayout_tex_01)

        self.verticalLayout_tex_02 = QVBoxLayout()
        self.verticalLayout_tex_02.setObjectName(u"verticalLayout_tex_02")
        self.fr_MissingTextures = QFrame(self.horizontalLayoutWidget_3)
        self.fr_MissingTextures.setObjectName(u"fr_MissingTextures")
        self.fr_MissingTextures.setMinimumSize(QSize(18, 18))
        self.fr_MissingTextures.setMaximumSize(QSize(18, 18))
        self.fr_MissingTextures.setFont(font3)
        self.fr_MissingTextures.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_MissingTextures.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_MissingTextures.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_tex_02.addWidget(self.fr_MissingTextures)

        self.fr_InvalidTexturePath = QFrame(self.horizontalLayoutWidget_3)
        self.fr_InvalidTexturePath.setObjectName(u"fr_InvalidTexturePath")
        self.fr_InvalidTexturePath.setMinimumSize(QSize(18, 18))
        self.fr_InvalidTexturePath.setMaximumSize(QSize(18, 18))
        self.fr_InvalidTexturePath.setFont(font3)
        self.fr_InvalidTexturePath.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_InvalidTexturePath.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_InvalidTexturePath.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_tex_02.addWidget(self.fr_InvalidTexturePath)

        self.fr_UnusedMaterials = QFrame(self.horizontalLayoutWidget_3)
        self.fr_UnusedMaterials.setObjectName(u"fr_UnusedMaterials")
        self.fr_UnusedMaterials.setMinimumSize(QSize(18, 18))
        self.fr_UnusedMaterials.setMaximumSize(QSize(18, 18))
        self.fr_UnusedMaterials.setFont(font3)
        self.fr_UnusedMaterials.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_UnusedMaterials.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_UnusedMaterials.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_tex_02.addWidget(self.fr_UnusedMaterials)


        self.horizontalLayout_tex.addLayout(self.verticalLayout_tex_02)

        self.verticalLayout_tex_03 = QVBoxLayout()
        self.verticalLayout_tex_03.setObjectName(u"verticalLayout_tex_03")
        self.btnCh_MissingTextures = QPushButton(self.horizontalLayoutWidget_3)
        self.btnCh_MissingTextures.setObjectName(u"btnCh_MissingTextures")
        self.btnCh_MissingTextures.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_tex_03.addWidget(self.btnCh_MissingTextures)

        self.btnCh_InvalidTexturePath = QPushButton(self.horizontalLayoutWidget_3)
        self.btnCh_InvalidTexturePath.setObjectName(u"btnCh_InvalidTexturePath")
        self.btnCh_InvalidTexturePath.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_tex_03.addWidget(self.btnCh_InvalidTexturePath)

        self.btnCh_UnusedMaterials = QPushButton(self.horizontalLayoutWidget_3)
        self.btnCh_UnusedMaterials.setObjectName(u"btnCh_UnusedMaterials")
        self.btnCh_UnusedMaterials.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_tex_03.addWidget(self.btnCh_UnusedMaterials)


        self.horizontalLayout_tex.addLayout(self.verticalLayout_tex_03)

        self.horizontalLayout_tex.setStretch(0, 1)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(9, 472, 320, 102))
        self.horizontalLayout_scene = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_scene.setObjectName(u"horizontalLayout_scene")
        self.horizontalLayout_scene.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_scene_01 = QVBoxLayout()
        self.verticalLayout_scene_01.setObjectName(u"verticalLayout_scene_01")
        self.chbx_EmptyTransform = QCheckBox(self.horizontalLayoutWidget_4)
        self.chbx_EmptyTransform.setObjectName(u"chbx_EmptyTransform")

        self.verticalLayout_scene_01.addWidget(self.chbx_EmptyTransform)

        self.chbx_HiddenObj = QCheckBox(self.horizontalLayoutWidget_4)
        self.chbx_HiddenObj.setObjectName(u"chbx_HiddenObj")

        self.verticalLayout_scene_01.addWidget(self.chbx_HiddenObj)

        self.chbx_FrozenTransform = QCheckBox(self.horizontalLayoutWidget_4)
        self.chbx_FrozenTransform.setObjectName(u"chbx_FrozenTransform")

        self.verticalLayout_scene_01.addWidget(self.chbx_FrozenTransform)

        self.chbx_History = QCheckBox(self.horizontalLayoutWidget_4)
        self.chbx_History.setObjectName(u"chbx_History")

        self.verticalLayout_scene_01.addWidget(self.chbx_History)


        self.horizontalLayout_scene.addLayout(self.verticalLayout_scene_01)

        self.verticalLayout_scene_02 = QVBoxLayout()
        self.verticalLayout_scene_02.setObjectName(u"verticalLayout_scene_02")
        self.fr_EmptyTransform = QFrame(self.horizontalLayoutWidget_4)
        self.fr_EmptyTransform.setObjectName(u"fr_EmptyTransform")
        self.fr_EmptyTransform.setMinimumSize(QSize(18, 18))
        self.fr_EmptyTransform.setMaximumSize(QSize(18, 18))
        self.fr_EmptyTransform.setFont(font3)
        self.fr_EmptyTransform.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_EmptyTransform.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_EmptyTransform.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_scene_02.addWidget(self.fr_EmptyTransform)

        self.fr_HiddenObj = QFrame(self.horizontalLayoutWidget_4)
        self.fr_HiddenObj.setObjectName(u"fr_HiddenObj")
        self.fr_HiddenObj.setMinimumSize(QSize(18, 18))
        self.fr_HiddenObj.setMaximumSize(QSize(18, 18))
        self.fr_HiddenObj.setFont(font3)
        self.fr_HiddenObj.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_HiddenObj.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_HiddenObj.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_scene_02.addWidget(self.fr_HiddenObj)

        self.fr_FrozenTransform = QFrame(self.horizontalLayoutWidget_4)
        self.fr_FrozenTransform.setObjectName(u"fr_FrozenTransform")
        self.fr_FrozenTransform.setMinimumSize(QSize(18, 18))
        self.fr_FrozenTransform.setMaximumSize(QSize(18, 18))
        self.fr_FrozenTransform.setFont(font3)
        self.fr_FrozenTransform.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_FrozenTransform.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_FrozenTransform.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_scene_02.addWidget(self.fr_FrozenTransform)

        self.fr_History = QFrame(self.horizontalLayoutWidget_4)
        self.fr_History.setObjectName(u"fr_History")
        self.fr_History.setMinimumSize(QSize(18, 18))
        self.fr_History.setMaximumSize(QSize(18, 18))
        self.fr_History.setFont(font3)
        self.fr_History.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_History.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_History.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_scene_02.addWidget(self.fr_History)


        self.horizontalLayout_scene.addLayout(self.verticalLayout_scene_02)

        self.verticalLayout_scene_03 = QVBoxLayout()
        self.verticalLayout_scene_03.setObjectName(u"verticalLayout_scene_03")
        self.btnCh_EmptyTransform = QPushButton(self.horizontalLayoutWidget_4)
        self.btnCh_EmptyTransform.setObjectName(u"btnCh_EmptyTransform")
        self.btnCh_EmptyTransform.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_scene_03.addWidget(self.btnCh_EmptyTransform)

        self.btnCh_HiddenObj = QPushButton(self.horizontalLayoutWidget_4)
        self.btnCh_HiddenObj.setObjectName(u"btnCh_HiddenObj")
        self.btnCh_HiddenObj.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_scene_03.addWidget(self.btnCh_HiddenObj)

        self.btnCh_FrozenTransform = QPushButton(self.horizontalLayoutWidget_4)
        self.btnCh_FrozenTransform.setObjectName(u"btnCh_FrozenTransform")
        self.btnCh_FrozenTransform.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_scene_03.addWidget(self.btnCh_FrozenTransform)

        self.btnCh_History = QPushButton(self.horizontalLayoutWidget_4)
        self.btnCh_History.setObjectName(u"btnCh_History")
        self.btnCh_History.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_scene_03.addWidget(self.btnCh_History)


        self.horizontalLayout_scene.addLayout(self.verticalLayout_scene_03)

        self.horizontalLayout_scene.setStretch(0, 1)
        self.lbl_Scene = QLabel(self.centralwidget)
        self.lbl_Scene.setObjectName(u"lbl_Scene")
        self.lbl_Scene.setGeometry(QRect(10, 451, 173, 20))
        self.lbl_Scene.setFont(font2)
        self.lbl_Scene.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 359, 319, 80))
        self.horizontalLayout_name = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_name.setObjectName(u"horizontalLayout_name")
        self.horizontalLayout_name.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_name_01 = QVBoxLayout()
        self.verticalLayout_name_01.setObjectName(u"verticalLayout_name_01")
        self.chbx_DefaultName = QCheckBox(self.horizontalLayoutWidget_5)
        self.chbx_DefaultName.setObjectName(u"chbx_DefaultName")

        self.verticalLayout_name_01.addWidget(self.chbx_DefaultName)

        self.chbx_DuplicateName = QCheckBox(self.horizontalLayoutWidget_5)
        self.chbx_DuplicateName.setObjectName(u"chbx_DuplicateName")

        self.verticalLayout_name_01.addWidget(self.chbx_DuplicateName)

        self.chbx_NamingConvention = QCheckBox(self.horizontalLayoutWidget_5)
        self.chbx_NamingConvention.setObjectName(u"chbx_NamingConvention")

        self.verticalLayout_name_01.addWidget(self.chbx_NamingConvention)


        self.horizontalLayout_name.addLayout(self.verticalLayout_name_01)

        self.verticalLayout_name_02 = QVBoxLayout()
        self.verticalLayout_name_02.setObjectName(u"verticalLayout_name_02")
        self.fr_DefaultName = QFrame(self.horizontalLayoutWidget_5)
        self.fr_DefaultName.setObjectName(u"fr_DefaultName")
        self.fr_DefaultName.setMinimumSize(QSize(18, 18))
        self.fr_DefaultName.setMaximumSize(QSize(18, 18))
        self.fr_DefaultName.setFont(font3)
        self.fr_DefaultName.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_DefaultName.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_DefaultName.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_name_02.addWidget(self.fr_DefaultName)

        self.fr_DuplicateName = QFrame(self.horizontalLayoutWidget_5)
        self.fr_DuplicateName.setObjectName(u"fr_DuplicateName")
        self.fr_DuplicateName.setMinimumSize(QSize(18, 18))
        self.fr_DuplicateName.setMaximumSize(QSize(18, 18))
        self.fr_DuplicateName.setFont(font3)
        self.fr_DuplicateName.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_DuplicateName.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_DuplicateName.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_name_02.addWidget(self.fr_DuplicateName)

        self.fr_NamingConvention = QFrame(self.horizontalLayoutWidget_5)
        self.fr_NamingConvention.setObjectName(u"fr_NamingConvention")
        self.fr_NamingConvention.setMinimumSize(QSize(18, 18))
        self.fr_NamingConvention.setMaximumSize(QSize(18, 18))
        self.fr_NamingConvention.setFont(font3)
        self.fr_NamingConvention.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_NamingConvention.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_NamingConvention.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_name_02.addWidget(self.fr_NamingConvention)


        self.horizontalLayout_name.addLayout(self.verticalLayout_name_02)

        self.verticalLayout_name_03 = QVBoxLayout()
        self.verticalLayout_name_03.setObjectName(u"verticalLayout_name_03")
        self.btnCh_DefaultName = QPushButton(self.horizontalLayoutWidget_5)
        self.btnCh_DefaultName.setObjectName(u"btnCh_DefaultName")
        self.btnCh_DefaultName.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_name_03.addWidget(self.btnCh_DefaultName)

        self.btnCh_DuplicateName = QPushButton(self.horizontalLayoutWidget_5)
        self.btnCh_DuplicateName.setObjectName(u"btnCh_DuplicateName")
        self.btnCh_DuplicateName.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_name_03.addWidget(self.btnCh_DuplicateName)

        self.btnCh_NamingConvention = QPushButton(self.horizontalLayoutWidget_5)
        self.btnCh_NamingConvention.setObjectName(u"btnCh_NamingConvention")
        self.btnCh_NamingConvention.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_name_03.addWidget(self.btnCh_NamingConvention)


        self.horizontalLayout_name.addLayout(self.verticalLayout_name_03)

        self.horizontalLayout_name.setStretch(0, 1)
        self.lbl_Naming = QLabel(self.centralwidget)
        self.lbl_Naming.setObjectName(u"lbl_Naming")
        self.lbl_Naming.setGeometry(QRect(11, 340, 173, 20))
        self.lbl_Naming.setFont(font2)
        self.lbl_Naming.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(350, 0, 16, 616))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(386, 33, 242, 128))
        self.horizontalLayout_engine = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_engine.setObjectName(u"horizontalLayout_engine")
        self.horizontalLayout_engine.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_engine_01 = QVBoxLayout()
        self.verticalLayout_engine_01.setObjectName(u"verticalLayout_engine_01")
        self.chbx_PivotCenter = QCheckBox(self.horizontalLayoutWidget_6)
        self.chbx_PivotCenter.setObjectName(u"chbx_PivotCenter")

        self.verticalLayout_engine_01.addWidget(self.chbx_PivotCenter)

        self.chbx_RotateZero = QCheckBox(self.horizontalLayoutWidget_6)
        self.chbx_RotateZero.setObjectName(u"chbx_RotateZero")

        self.verticalLayout_engine_01.addWidget(self.chbx_RotateZero)

        self.chbx_Scale = QCheckBox(self.horizontalLayoutWidget_6)
        self.chbx_Scale.setObjectName(u"chbx_Scale")

        self.verticalLayout_engine_01.addWidget(self.chbx_Scale)

        self.chbx_TrisCount = QCheckBox(self.horizontalLayoutWidget_6)
        self.chbx_TrisCount.setObjectName(u"chbx_TrisCount")

        self.verticalLayout_engine_01.addWidget(self.chbx_TrisCount)

        self.chbx_NgonGroup = QCheckBox(self.horizontalLayoutWidget_6)
        self.chbx_NgonGroup.setObjectName(u"chbx_NgonGroup")

        self.verticalLayout_engine_01.addWidget(self.chbx_NgonGroup)


        self.horizontalLayout_engine.addLayout(self.verticalLayout_engine_01)

        self.verticalLayout_engine_02 = QVBoxLayout()
        self.verticalLayout_engine_02.setObjectName(u"verticalLayout_engine_02")
        self.fr_PivotCenter = QFrame(self.horizontalLayoutWidget_6)
        self.fr_PivotCenter.setObjectName(u"fr_PivotCenter")
        self.fr_PivotCenter.setMinimumSize(QSize(18, 18))
        self.fr_PivotCenter.setMaximumSize(QSize(18, 18))
        self.fr_PivotCenter.setFont(font3)
        self.fr_PivotCenter.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_PivotCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_PivotCenter.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_engine_02.addWidget(self.fr_PivotCenter)

        self.fr_RotateZero = QFrame(self.horizontalLayoutWidget_6)
        self.fr_RotateZero.setObjectName(u"fr_RotateZero")
        self.fr_RotateZero.setMinimumSize(QSize(18, 18))
        self.fr_RotateZero.setMaximumSize(QSize(18, 18))
        self.fr_RotateZero.setFont(font3)
        self.fr_RotateZero.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_RotateZero.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_RotateZero.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_engine_02.addWidget(self.fr_RotateZero)

        self.fr_Scale = QFrame(self.horizontalLayoutWidget_6)
        self.fr_Scale.setObjectName(u"fr_Scale")
        self.fr_Scale.setMinimumSize(QSize(18, 18))
        self.fr_Scale.setMaximumSize(QSize(18, 18))
        self.fr_Scale.setFont(font3)
        self.fr_Scale.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_Scale.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_Scale.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_engine_02.addWidget(self.fr_Scale)

        self.fr_TrisCount = QFrame(self.horizontalLayoutWidget_6)
        self.fr_TrisCount.setObjectName(u"fr_TrisCount")
        self.fr_TrisCount.setMinimumSize(QSize(18, 18))
        self.fr_TrisCount.setMaximumSize(QSize(18, 18))
        self.fr_TrisCount.setFont(font3)
        self.fr_TrisCount.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_TrisCount.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_TrisCount.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_engine_02.addWidget(self.fr_TrisCount)

        self.fr_NgonGroup = QFrame(self.horizontalLayoutWidget_6)
        self.fr_NgonGroup.setObjectName(u"fr_NgonGroup")
        self.fr_NgonGroup.setMinimumSize(QSize(18, 18))
        self.fr_NgonGroup.setMaximumSize(QSize(18, 18))
        self.fr_NgonGroup.setFont(font3)
        self.fr_NgonGroup.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: 3px solid rgb(30, 30, 30); \n"
"    border-radius: 10px;                \n"
"}\n"
"\n"
"QFrame[status=\"ok\"] {\n"
"    background-color: rgb(0, 200, 0);\n"
"    border: 3px solid rgb(0, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"warning\"] {\n"
"    background-color: rgb(255, 180, 0);\n"
"    border: 3px solid rgb(180, 120, 0);\n"
"}\n"
"\n"
"QFrame[status=\"error\"] {\n"
"    background-color: rgb(220, 50, 50);\n"
"    border: 3px solid rgb(140, 20, 20);\n"
"}")
        self.fr_NgonGroup.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_NgonGroup.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_engine_02.addWidget(self.fr_NgonGroup)


        self.horizontalLayout_engine.addLayout(self.verticalLayout_engine_02)

        self.verticalLayout_engine_03 = QVBoxLayout()
        self.verticalLayout_engine_03.setObjectName(u"verticalLayout_engine_03")
        self.btnCh_PivotCenter = QPushButton(self.horizontalLayoutWidget_6)
        self.btnCh_PivotCenter.setObjectName(u"btnCh_PivotCenter")
        self.btnCh_PivotCenter.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_engine_03.addWidget(self.btnCh_PivotCenter)

        self.btnCh_RotateZero = QPushButton(self.horizontalLayoutWidget_6)
        self.btnCh_RotateZero.setObjectName(u"btnCh_RotateZero")
        self.btnCh_RotateZero.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_engine_03.addWidget(self.btnCh_RotateZero)

        self.btnCh_Scale = QPushButton(self.horizontalLayoutWidget_6)
        self.btnCh_Scale.setObjectName(u"btnCh_Scale")
        self.btnCh_Scale.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_engine_03.addWidget(self.btnCh_Scale)

        self.btnCh_TrisCount = QPushButton(self.horizontalLayoutWidget_6)
        self.btnCh_TrisCount.setObjectName(u"btnCh_TrisCount")
        self.btnCh_TrisCount.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_engine_03.addWidget(self.btnCh_TrisCount)

        self.btnCh_NgonGroup = QPushButton(self.horizontalLayoutWidget_6)
        self.btnCh_NgonGroup.setObjectName(u"btnCh_NgonGroup")
        self.btnCh_NgonGroup.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_engine_03.addWidget(self.btnCh_NgonGroup)


        self.horizontalLayout_engine.addLayout(self.verticalLayout_engine_03)

        self.horizontalLayout_engine.setStretch(0, 1)
        self.lbl_Engine = QLabel(self.centralwidget)
        self.lbl_Engine.setObjectName(u"lbl_Engine")
        self.lbl_Engine.setGeometry(QRect(389, 10, 143, 16))
        self.lbl_Engine.setFont(font2)
        self.lbl_Engine.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(376, 356, 247, 225))
        self.horizontalLayout_3rd_Tool = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_3rd_Tool.setSpacing(14)
        self.horizontalLayout_3rd_Tool.setObjectName(u"horizontalLayout_3rd_Tool")
        self.horizontalLayout_3rd_Tool.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3rdTool_1 = QVBoxLayout()
        self.verticalLayout_3rdTool_1.setObjectName(u"verticalLayout_3rdTool_1")
        self.btnPivotTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnPivotTool.setObjectName(u"btnPivotTool")
        self.btnPivotTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_1.addWidget(self.btnPivotTool)

        self.btnMeshPosTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnMeshPosTool.setObjectName(u"btnMeshPosTool")
        self.btnMeshPosTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_1.addWidget(self.btnMeshPosTool)

        self.btnMatRePathTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnMatRePathTool.setObjectName(u"btnMatRePathTool")
        self.btnMatRePathTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_1.addWidget(self.btnMatRePathTool)

        self.btnRenameTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnRenameTool.setObjectName(u"btnRenameTool")
        self.btnRenameTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_1.addWidget(self.btnRenameTool)


        self.horizontalLayout_3rd_Tool.addLayout(self.verticalLayout_3rdTool_1)

        self.verticalLayout_3rdTool_2 = QVBoxLayout()
        self.verticalLayout_3rdTool_2.setObjectName(u"verticalLayout_3rdTool_2")
        self.btnGadgetTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnGadgetTool.setObjectName(u"btnGadgetTool")
        self.btnGadgetTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_2.addWidget(self.btnGadgetTool)

        self.btnAssetLibTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnAssetLibTool.setObjectName(u"btnAssetLibTool")
        self.btnAssetLibTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_2.addWidget(self.btnAssetLibTool)

        self.btnTeleportTool = QPushButton(self.horizontalLayoutWidget_7)
        self.btnTeleportTool.setObjectName(u"btnTeleportTool")
        self.btnTeleportTool.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_2.addWidget(self.btnTeleportTool)

        self.btnComingSoon = QPushButton(self.horizontalLayoutWidget_7)
        self.btnComingSoon.setObjectName(u"btnComingSoon")
        self.btnComingSoon.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")

        self.verticalLayout_3rdTool_2.addWidget(self.btnComingSoon)


        self.horizontalLayout_3rd_Tool.addLayout(self.verticalLayout_3rdTool_2)

        self.btnCheckAll = QPushButton(self.centralwidget)
        self.btnCheckAll.setObjectName(u"btnCheckAll")
        self.btnCheckAll.setGeometry(QRect(385, 172, 69, 35))
        self.btnCheckAll.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 40, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")
        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")
        self.btnRun.setGeometry(QRect(460, 172, 169, 35))
        self.btnRun.setStyleSheet(u"QPushButton {\n"
"    font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 140, 40);\n"
"\n"
"    border: 1px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(25, 25, 25);\n"
"    border: 3px solid rgb(24, 103, 155);\n"
"    border-radius: 4px;\n"
"}")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(389, 218, 239, 32))
        self.progressBar.setValue(24)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1001, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEditable = QMenu(self.menubar)
        self.menuEditable.setObjectName(u"menuEditable")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditable.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.act_Export_INFOR)
        self.menuFile.addAction(self.act_Open_Explore)
        self.menuFile.addAction(self.act_Refresh_Tool)
        self.menuEditable.addAction(self.act_Geo)
        self.menuEditable.addAction(self.act_UV)
        self.menuEditable.addAction(self.act_Texture)
        self.menuEditable.addSeparator()
        self.menuEditable.addAction(self.act_Naming)
        self.menuEditable.addAction(self.act_Scene)
        self.menuEditable.addAction(self.act_GameReady)
        self.menuHelp.addAction(self.act_GeoHelp)
        self.menuHelp.addAction(self.act_UVHelp)
        self.menuHelp.addAction(self.act_TexHelp)
        self.menuHelp.addAction(self.act_NamingHelp)
        self.menuHelp.addAction(self.act_SceneHelp)
        self.menuHelp.addAction(self.act_UnrealHelp)
        self.menuHelp.addAction(self.act_UnityHelp)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.act_Export_INFOR.setText(QCoreApplication.translate("mainWindow", u"Export infor to JSON", None))
        self.act_Open_Explore.setText(QCoreApplication.translate("mainWindow", u"Open Explore JSON", None))
        self.act_Refresh_Tool.setText(QCoreApplication.translate("mainWindow", u"Refresh Tool", None))
        self.act_Geo.setText(QCoreApplication.translate("mainWindow", u"Geometry", None))
        self.act_UV.setText(QCoreApplication.translate("mainWindow", u"UV", None))
        self.act_Texture.setText(QCoreApplication.translate("mainWindow", u"Texture/Material", None))
        self.act_Naming.setText(QCoreApplication.translate("mainWindow", u"Naming ", None))
        self.act_Scene.setText(QCoreApplication.translate("mainWindow", u"Scene", None))
        self.act_GameReady.setText(QCoreApplication.translate("mainWindow", u"Engine Game Ready", None))
        self.act_GeoHelp.setText(QCoreApplication.translate("mainWindow", u"Geometry", None))
        self.act_UVHelp.setText(QCoreApplication.translate("mainWindow", u"UV", None))
        self.act_TexHelp.setText(QCoreApplication.translate("mainWindow", u"Texture / Material", None))
        self.act_NamingHelp.setText(QCoreApplication.translate("mainWindow", u"Naming Convetion", None))
        self.act_SceneHelp.setText(QCoreApplication.translate("mainWindow", u"Scene", None))
        self.act_UnrealHelp.setText(QCoreApplication.translate("mainWindow", u"Unreal / Game ready", None))
        self.act_UnityHelp.setText(QCoreApplication.translate("mainWindow", u"Unity / Game ready", None))
        self.HF_author.setText(QCoreApplication.translate("mainWindow", u"@HuangFei", None))
        self.btnFAQs.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnRefreshTool.setText(QCoreApplication.translate("mainWindow", u"Refresh Tool", None))
        self.lbl_Console.setText(QCoreApplication.translate("mainWindow", u"Console", None))
        self.lbl_AnotherTools.setText(QCoreApplication.translate("mainWindow", u"Another Tools", None))
        self.lbl_Tips.setText(QCoreApplication.translate("mainWindow", u"Tips: Xem th\u00eam h\u01b0\u01a1\u0301ng d\u00e2\u0303n ta\u0323i @Help", None))
        self.chbx_ConcaveFaces.setText(QCoreApplication.translate("mainWindow", u"Concave Faces", None))
        self.chbx_LanimaFaces.setText(QCoreApplication.translate("mainWindow", u"Lamina faces", None))
        self.chbx_NonManifold.setText(QCoreApplication.translate("mainWindow", u"Non-manifold", None))
        self.chbx_ZeroEdge.setText(QCoreApplication.translate("mainWindow", u"Zero Edge Length", None))
        self.btnCh_ConcaveFaces.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_LaminaFaces.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_NonManifold.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_ZeroEdge.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.lbl_Geo.setText(QCoreApplication.translate("mainWindow", u"Geometry", None))
        self.lbl_UV.setText(QCoreApplication.translate("mainWindow", u"UV", None))
        self.chbx_MisUV.setText(QCoreApplication.translate("mainWindow", u"Missing UV", None))
        self.chbx_MoreUV.setText(QCoreApplication.translate("mainWindow", u"More than 1 UV Channel", None))
        self.chbx_OverlapUV.setText(QCoreApplication.translate("mainWindow", u"Overlapping UV", None))
        self.btnCh_MisUV.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_MoreUV.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_Overlap.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.lbl_Texture.setText(QCoreApplication.translate("mainWindow", u"Texture / Material", None))
        self.chbx_MissingTextures.setText(QCoreApplication.translate("mainWindow", u"Missing Textures", None))
        self.chbx_InvalidTexturePath.setText(QCoreApplication.translate("mainWindow", u"Invalid Texture Path", None))
        self.chbx_UnusedMaterials.setText(QCoreApplication.translate("mainWindow", u"Unused Materials", None))
        self.btnCh_MissingTextures.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_InvalidTexturePath.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_UnusedMaterials.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.chbx_EmptyTransform.setText(QCoreApplication.translate("mainWindow", u"Empty Transform", None))
        self.chbx_HiddenObj.setText(QCoreApplication.translate("mainWindow", u"Hidden Objects (optional)", None))
        self.chbx_FrozenTransform.setText(QCoreApplication.translate("mainWindow", u"Frozen Transform (optional)", None))
        self.chbx_History.setText(QCoreApplication.translate("mainWindow", u"History not Deleted", None))
        self.btnCh_EmptyTransform.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_HiddenObj.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_FrozenTransform.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_History.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.lbl_Scene.setText(QCoreApplication.translate("mainWindow", u"Scene ", None))
        self.chbx_DefaultName.setText(QCoreApplication.translate("mainWindow", u"Default name", None))
        self.chbx_DuplicateName.setText(QCoreApplication.translate("mainWindow", u"Duplicate names", None))
        self.chbx_NamingConvention.setText(QCoreApplication.translate("mainWindow", u"Naming convention", None))
        self.btnCh_DefaultName.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_DuplicateName.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_NamingConvention.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.lbl_Naming.setText(QCoreApplication.translate("mainWindow", u"Naming QC", None))
        self.chbx_PivotCenter.setText(QCoreApplication.translate("mainWindow", u"Pivot centered", None))
        self.chbx_RotateZero.setText(QCoreApplication.translate("mainWindow", u"Rotation zero", None))
        self.chbx_Scale.setText(QCoreApplication.translate("mainWindow", u"Scale 1,1,1", None))
        self.chbx_TrisCount.setText(QCoreApplication.translate("mainWindow", u"Tris-count over", None))
        self.chbx_NgonGroup.setText(QCoreApplication.translate("mainWindow", u"Ngon group hierarchy", None))
        self.btnCh_PivotCenter.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_RotateZero.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_Scale.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_TrisCount.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.btnCh_NgonGroup.setText(QCoreApplication.translate("mainWindow", u"Check", None))
        self.lbl_Engine.setText(QCoreApplication.translate("mainWindow", u"Engine Game Ready", None))
        self.btnPivotTool.setText(QCoreApplication.translate("mainWindow", u"Pivot", None))
        self.btnMeshPosTool.setText(QCoreApplication.translate("mainWindow", u"Mesh Position", None))
        self.btnMatRePathTool.setText(QCoreApplication.translate("mainWindow", u"Material Re-Path", None))
        self.btnRenameTool.setText(QCoreApplication.translate("mainWindow", u"Rename", None))
        self.btnGadgetTool.setText(QCoreApplication.translate("mainWindow", u"Gadget", None))
        self.btnAssetLibTool.setText(QCoreApplication.translate("mainWindow", u"AssetLib", None))
        self.btnTeleportTool.setText(QCoreApplication.translate("mainWindow", u"Teleport", None))
        self.btnComingSoon.setText(QCoreApplication.translate("mainWindow", u"Coming Soon", None))
        self.btnCheckAll.setText(QCoreApplication.translate("mainWindow", u"Check All", None))
        self.btnRun.setText(QCoreApplication.translate("mainWindow", u"Run", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
        self.menuEditable.setTitle(QCoreApplication.translate("mainWindow", u"Editable", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainWindow", u"Help", None))
    # retranslateUi

