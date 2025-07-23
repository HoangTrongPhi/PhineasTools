# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeshItem_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#------- PyQt/PySide imports ----------
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

class Ui_meshItem(object):
    def setupUi(self, meshItem):
        if not meshItem.objectName():
            meshItem.setObjectName(u"meshItem")
        meshItem.resize(192, 192)
        self.verticalLayoutWidget = QWidget(meshItem)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 171, 151))
        self.imgLabel_Layout = QVBoxLayout(self.verticalLayoutWidget)
        self.imgLabel_Layout.setSpacing(6)
        self.imgLabel_Layout.setObjectName(u"imgLabel_Layout")
        self.imgLabel_Layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.imgLabel_Layout.setContentsMargins(0, 0, 0, 0)
        self.img_Frame = QFrame(self.verticalLayoutWidget)
        self.img_Frame.setObjectName(u"img_Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_Frame.sizePolicy().hasHeightForWidth())
        self.img_Frame.setSizePolicy(sizePolicy)
        self.img_Frame.setFrameShape(QFrame.Shape.Box)
        self.img_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.imageLabel = QLabel(self.img_Frame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(-2, -1, 171, 151))
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.img_Frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(-10, -10, 192, 192))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 60);  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 200, 255, 100);   \n"
"}\n"
"")

        self.imgLabel_Layout.addWidget(self.img_Frame)

        self.verticalLayoutWidget_2 = QWidget(meshItem)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 160, 171, 21))
        self.nameLabel_Layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.nameLabel_Layout.setObjectName(u"nameLabel_Layout")
        self.nameLabel_Layout.setContentsMargins(0, 0, 0, 0)
        self.nameFrame = QFrame(self.verticalLayoutWidget_2)
        self.nameFrame.setObjectName(u"nameFrame")
        self.nameFrame.setStyleSheet(u"background-color: rgb(75, 75, 75);")
        self.nameFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.nameFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.nameLabel = QLabel(self.nameFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(-2, 0, 171, 20))
        self.nameLabel.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nameLabel_Layout.addWidget(self.nameFrame)


        self.retranslateUi(meshItem)

        QMetaObject.connectSlotsByName(meshItem)
    # setupUi

    def retranslateUi(self, meshItem):
        meshItem.setWindowTitle(QCoreApplication.translate("meshItem", u"Form", None))
        self.imageLabel.setText(QCoreApplication.translate("meshItem", u"imageLabel", None))
        self.pushButton.setText("")
        self.nameLabel.setText(QCoreApplication.translate("meshItem", u"nameLabel", None))
    # retranslateUi

