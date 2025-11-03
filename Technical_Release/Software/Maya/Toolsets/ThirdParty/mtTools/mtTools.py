import os
import sys
import importlib
import maya.OpenMayaUI as mui
import maya.cmds as cmds

# Try PySide6 (Maya 2025+), fallback to PySide2 (Maya 2022-2024)
try:
    from PySide6 import QtCore, QtWidgets, QtUiTools, QtGui
    from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QColorDialog
    from PySide6.QtGui import QMovie, QImageReader
    from PySide6.QtCore import QTimer
    from shiboken6 import wrapInstance
    QT_VERSION = 6
except ImportError:
    from PySide2 import QtCore, QtWidgets, QtUiTools, QtGui
    from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget, QColorDialog
    from PySide2.QtGui import QMovie, QImageReader
    from PySide2.QtCore import QTimer
    from shiboken2 import wrapInstance
    QT_VERSION = 2


#Directories
rootPath = os.path.dirname(os.path.abspath(__file__))
scriptPath = os.path.join(rootPath, "Scripts")
iconPath = os.path.join(rootPath, "Icons")
gifsPath = os.path.join(rootPath, "Gifs\\")
mayaVersion = cmds.about(version=True)
jsonFile = rootPath + "/mtTools.json"


if scriptPath not in sys.path:
    sys.path.append(os.environ['USERPROFILE'] + '/Documents/maya/scripts/mtTools/Scripts')

from Software.Maya.Toolsets.ThirdParty.mtTools.Scripts import Pivot, nameCleaner, meshExtract, meshRename, patternSelect, planar, edgeAverage, edgeSelect, edgeAlign, uv, baking, cleanScene, exportFbx, mtWrap, pipe, shelf, billboard, winFix, alignPivot, lightGroup, raycastSnap, selection, hair, jsonManager



#ExplodingOffset
stepInput = 100

titleBarPressed = False
windowScalePressed = False
#Colors
def get_maya_window():
    ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(int(ptr), QtWidgets.QWidget)

class mtToolsWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = get_maya_window()):
        super(mtToolsWindow, self).__init__(parent)

        mtToolsWindow._instance = self  # Set the instance to the current window
        
        #Load UI
        uiFilePath = os.path.join(
            rootPath + "/mtTools.ui"
        )
        loader = QtUiTools.QUiLoader()
        uiFile = QtCore.QFile(uiFilePath)

        uiFile.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(uiFile, None)
        uiFile.close()
        
        self.ui.setParent(parent)  # Set the parent correctly
        self.ui.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.NonModal)

        #Window Scale
        self.ui.resize(jsonManager.load("windowSizeX", jsonFile), jsonManager.load("windowSizeY", jsonFile)) 
        self._resize_start_pos = None
        

        #HoverTime
        self.hover_timer = None  
        self.hover_delay = 1000  
        self.lastHoveredWidget = None

        #Connect UI
        self.init_connections()

        self.ui.show()


    def closeEvent(self, event):
            mtToolsWindow._instance = None  # Clear the instance reference on close
            event.accept()  # Accept the close event to allow the window to close

    def eventFilter(self, widget, event):

        global titleBarPressed
        global windowScalePressed

        if event.type() == QtCore.QEvent.WindowDeactivate:
            self.raise_()
            self.activateWindow()  

        #TitleBar
        if(widget == self.ui.titleBar or titleBarPressed==True):
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.globalPos()
                titleBarPressed = True

            elif event.type() == QtCore.QEvent.MouseMove and titleBarPressed == True:
                delta = QtCore.QPoint(event.globalPos() - self.oldPos)
                self.ui.move(self.ui.x() + delta.x(), self.ui.y() + delta.y())
                self.oldPos = event.globalPos()

            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                titleBarPressed = False

        #WindowScale Button
        elif(widget == self.ui.windowScale_Button or windowScalePressed==True):
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.ui._resize_start_pos = event.globalPos()
                self.ui._start_size = self.ui.size()
                windowScalePressed = True

            elif event.type() == QtCore.QEvent.MouseMove and windowScalePressed == True:
                    delta = event.globalPos() - self.ui._resize_start_pos
                    new_size = QtCore.QSize(
                        self.ui._start_size.width() + delta.x(),
                        self.ui._start_size.height() + delta.y()
                    )
                    self.ui.resize(new_size)

            elif event.type() == QtCore.QEvent.Enter and widget == self.ui.windowScale_Button:
                widget.setCursor(QtCore.Qt.SizeFDiagCursor)
            elif event.type() == QtCore.QEvent.Leave and widget == self.ui.windowScale_Button:
                widget.unsetCursor()
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                windowSize = self.ui.size()
                jsonManager.save("windowSizeX", windowSize.width(), jsonFile)
                jsonManager.save("windowSizeY", windowSize.height(), jsonFile)
                windowScalePressed = False

        #Button Tooltips
        else:
            
            if event.type() == QtCore.QEvent.HoverEnter:
                self.startHoverTimer(widget)
                return True

            if event.type() == QtCore.QEvent.HoverLeave:
                # Cancel any active hover timer
                if self.hover_timer:
                    self.hover_timer.stop()
                    self.hover_timer = None

                # Hide the popup when hover leaves
                if self.lastHoveredWidget == widget:
                    popUp.hide()
                    self.lastHoveredWidget = None

                return True

        return False

    def startHoverTimer(self, widget):
        # Start timer delay 
        if self.hover_timer:
            self.hover_timer.stop() 

        # Set the new hover timer
        self.hover_timer = QTimer(self)
        self.hover_timer.setSingleShot(True) 
        self.hover_timer.timeout.connect(lambda: self.showPopup(widget))
        self.hover_timer.start(self.hover_delay)  
        
    def showPopup(self, widget):

        if(self.ui.useGifTooltips.isChecked() == False):
            return
        
        position = self.ui.mapToGlobal(self.pos())

        if widget.toolTip() and os.path.isfile(gifsPath + widget.objectName() + '.gif'):
            popUp.updateMessage(gifsPath + widget.objectName() + '.gif')

           
            popUp.move(position.x() -  QImageReader(gifsPath + widget.objectName() + '.gif').size().width(), position.y() )
            popUp.show()
            self.lastHoveredWidget = widget

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def init_connections(self):
        global exportPath

        self.ui.titleBar.installEventFilter(self)
        self.ui.exit_Button.clicked.connect(self.exitApp)
        self.ui.minimize_Button.clicked.connect(self.minimizeApp) 
        self.ui.windowScale_Button.installEventFilter(self)
        addIcon(self.ui.windowScale_Button, 'windowScale.png')
        #Fix GroupBox Style
        self.ui.pivotBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.pivotBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.wrapBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.wrapBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.ToolsBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.ToolsBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.exportBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.exportBox.setStyleSheet("background-color:#2b2c2e; ")
        self.ui.namingBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.namingBox.setStyleSheet("background-color:#2b2c2e; ")
        self.ui.uvBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.uvBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.transformBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.transformBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.pairingBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.pairingBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.pastedBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.pastedBox.setStyleSheet("background-color:#2b2c2e;")
        self.ui.cleanupBox.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.ui.cleanupBox.setStyleSheet("background-color:#2b2c2e;")

        #MODELING
        #Pivot

        self.ui.pivOrigin_Button.clicked.connect(self.pivOrigin)
        self.ui.pivOrigin_Button.installEventFilter(self)
        addIcon(self.ui.pivOrigin_Button, 'pivotOrigin.png')

        self.ui.pivX_Button.clicked.connect(self.pivX)
        self.ui.pivX_Button.installEventFilter(self)

        self.ui.pivY_Button.clicked.connect(self.pivY)
        self.ui.pivY_Button.installEventFilter(self)

        self.ui.pivZ_Button.clicked.connect(self.pivZ)
        self.ui.pivZ_Button.installEventFilter(self)

        self.ui.centerPiv_Button.clicked.connect(self.centerPiv)
        self.ui.centerPiv_Button.installEventFilter(self)
        addIcon(self.ui.centerPiv_Button, 'pivotCenter.png')

        self.ui.transferPiv_Button.clicked.connect(self.transferPiv)
        self.ui.transferPiv_Button.installEventFilter(self)
        addIcon(self.ui.transferPiv_Button, 'pivotTransfer.png')

        self.ui.alignPiv_Button.clicked.connect(self.alignPiv)
        self.ui.alignPiv_Button.installEventFilter(self)
        addIcon(self.ui.alignPiv_Button, 'pivotAlignToSurface.png')

        self.ui.pasted_Button.clicked.connect(self.pasted)
        self.ui.pasted_Button.installEventFilter(self)
        self.ui.pastedPlus_Button.clicked.connect(self.pastedPlus)
        self.ui.pastedPlus_Button.installEventFilter(self)

        #Modeling Tools
        self.ui.instanceX_Button.clicked.connect(self.instanceX)
        self.ui.instanceX_Button.installEventFilter(self)
        addIcon(self.ui.instanceX_Button, 'instanceX.png')

        self.ui.instanceY_Button.clicked.connect(self.instanceY)
        self.ui.instanceY_Button.installEventFilter(self)
        addIcon(self.ui.instanceY_Button, 'instanceY.png')

        self.ui.instanceZ_Button.clicked.connect(self.instanceZ)
        self.ui.instanceZ_Button.installEventFilter(self)
        addIcon(self.ui.instanceZ_Button, 'instanceZ.png')

        self.ui.rotateInstanceX_Button.clicked.connect(self.rotateInstanceX)
        self.ui.rotateInstanceX_Button.installEventFilter(self)
        addIcon(self.ui.rotateInstanceX_Button, 'rotateInstanceX.png')

        self.ui.rotateInstanceY_Button.clicked.connect(self.rotateInstanceY)
        self.ui.rotateInstanceY_Button.installEventFilter(self)
        addIcon(self.ui.rotateInstanceY_Button, 'rotateInstanceY.png')

        self.ui.rotateInstanceZ_Button.clicked.connect(self.rotateInstanceZ)
        self.ui.rotateInstanceZ_Button.installEventFilter(self)
        addIcon(self.ui.rotateInstanceZ_Button, 'rotateInstanceZ.png')

        self.ui.radialInstanceCount.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.radialInstanceCount.valueChanged.connect(self.RadialInstanceCount)
        self.ui.radialInstanceCount.setValue(jsonManager.load("RadialInstanceCount", jsonFile))
        self.ui.radialInstanceCount.setStyleSheet("QSpinBox { background-color: #252527; color: #62e5ff; }")

        self.ui.instanceAroundOrigin.setChecked(jsonManager.load("InstanceAroundOrigin", jsonFile))
        self.ui.instanceAroundOrigin.toggled.connect(lambda state: jsonManager.save("InstanceAroundOrigin", state, jsonFile))
        self.ui.instanceAroundOrigin.installEventFilter(self)
        
        self.ui.removeInstances_Button.clicked.connect(self.removeInstances)
        self.ui.removeInstances_Button.installEventFilter(self)
        addIcon(self.ui.removeInstances_Button, 'removeInstances.png')

        self.ui.DupDetach_Button.clicked.connect(self.DupDetach)
        self.ui.DupDetach_Button.installEventFilter(self)
        addIcon(self.ui.DupDetach_Button, 'dupDetach.png')

        self.ui.Detach_Button.clicked.connect(self.Detach)
        self.ui.Detach_Button.installEventFilter(self)
        addIcon(self.ui.Detach_Button, 'detach.png')

        self.ui.Combine_Button.clicked.connect(self.Combine)
        self.ui.Combine_Button.installEventFilter(self)
        addIcon(self.ui.Combine_Button, 'combine.png')

        self.ui.edgeAlign_Button.clicked.connect(self.edgeAlign)
        self.ui.edgeAlign_Button.installEventFilter(self)
        addIcon(self.ui.edgeAlign_Button, 'edgeAlign.png')

        self.ui.planar_Button.clicked.connect(self.planar)
        self.ui.planar_Button.installEventFilter(self)
        addIcon(self.ui.planar_Button, 'planarFaces.png')

        self.ui.edgeAverage_Button.clicked.connect(self.edgeAverage)
        self.ui.edgeAverage_Button.installEventFilter(self)
        addIcon(self.ui.edgeAverage_Button, 'edgeLengthAverage.png')

        self.ui.edgeAverageTarget_Button.clicked.connect(self.edgeAverageTarget)
        self.ui.edgeAverageTarget_Button.installEventFilter(self)
        addIcon(self.ui.edgeAverageTarget_Button, 'edgeLengthTarget.png')

        self.ui.mtUnwrap_Button.clicked.connect(self.mtUnwrap)
        self.ui.mtUnwrap_Button.installEventFilter(self)
        addIcon(self.ui.mtUnwrap_Button, 'mtUnwrap.png')

        self.ui.mtWrap_Button.clicked.connect(self.mtWrap)
        self.ui.mtWrap_Button.installEventFilter(self)
        addIcon(self.ui.mtWrap_Button, 'mtWrap.png')

        self.ui.mtWrapToggle_Button.clicked.connect(self.mtWrapToggle)
        self.ui.mtWrapToggle_Button.installEventFilter(self)
        addIcon(self.ui.mtWrapToggle_Button, 'mtWrapToggle.png')

        self.ui.edgeSelect_Button.clicked.connect(self.edgeSelect)
        self.ui.edgeSelect_Button.installEventFilter(self)
        addIcon(self.ui.edgeSelect_Button, 'edgeSelect.png')
        
        self.ui.edgePattern_Button.clicked.connect(self.edgePattern)
        self.ui.edgePattern_Button.installEventFilter(self)
        addIcon(self.ui.edgePattern_Button, 'pattern.png')

        self.ui.pipe_Button.clicked.connect(self.pipe)
        self.ui.pipe_Button.installEventFilter(self)
        addIcon(self.ui.pipe_Button, 'pipe.png')

        self.ui.raycastSnap_Button.clicked.connect(self.raycastSnap)
        self.ui.raycastSnap_Button.installEventFilter(self)
        addIcon(self.ui.raycastSnap_Button, 'raycast.png')

        self.ui.edgeFlow_Button.clicked.connect(self.edgeFlow)
        self.ui.edgeFlow_Button.installEventFilter(self)
        addIcon(self.ui.edgeFlow_Button, 'edgeFlow.png')

        self.ui.hardEdgeSel_Button.clicked.connect(self.hardEdgeSel)
        self.ui.hardEdgeSel_Button.installEventFilter(self)
        addIcon(self.ui.hardEdgeSel_Button, 'selectHardEdges.png')

        #Subdivision
        self.ui.subdivideHardEdges_Button.clicked.connect(self.subdivide)
        self.ui.subdivideHardEdges_Button.installEventFilter(self)
        addIcon(self.ui.subdivideHardEdges_Button, 'subdivide.png')

        self.ui.hardEdgeCrease_Button.clicked.connect(self.hardEdgeToCrease)
        self.ui.hardEdgeCrease_Button.installEventFilter(self)
        addIcon(self.ui.hardEdgeCrease_Button, 'HardEdgeCrease.png')

        #UV
        self.ui.offsetUVs_Button.clicked.connect(self.offsetUVs)
        self.ui.offsetUVs_Button.installEventFilter(self)
        self.ui.symStraighten_Button.clicked.connect(self.symStraighten)
        self.ui.symStraighten_Button.installEventFilter(self)
        self.ui.compressUVs_Button.clicked.connect(self.compressUVs)
        self.ui.compressUVs_Button.installEventFilter(self)

        self.ui.uvMoveUp_Button.clicked.connect(self.uvMoveUp)
        self.ui.uvMoveUp_Button.installEventFilter(self)
        self.ui.uvMoveDown_Button.clicked.connect(self.uvMoveDown)
        self.ui.uvMoveDown_Button.installEventFilter(self)
        self.ui.uvMoveLeft_Button.clicked.connect(self.uvMoveLeft)
        self.ui.uvMoveLeft_Button.installEventFilter(self)
        self.ui.uvMoveRight_Button.clicked.connect(self.uvMoveRight)
        self.ui.uvMoveRight_Button.installEventFilter(self)

        self.ui.densityGet_Button.clicked.connect(self.densityGet)
        self.ui.densityGet_Button.installEventFilter(self)
        self.ui.densitySet_Button.clicked.connect(self.densitySet)
        self.ui.densitySet_Button.installEventFilter(self)

        self.ui.scaleUVHoriz1_Button.clicked.connect(self.scaleUVHoriz1)
        self.ui.scaleUVHoriz1_Button.installEventFilter(self)
        self.ui.scaleUVHoriz2_Button.clicked.connect(self.scaleUVHoriz2)
        self.ui.scaleUVHoriz2_Button.installEventFilter(self)
        self.ui.scaleUVVert1_Button.clicked.connect(self.scaleUVVert1)
        self.ui.scaleUVVert1_Button.installEventFilter(self)
        self.ui.scaleUVVert2_Button.clicked.connect(self.scaleUVVert2)
        self.ui.scaleUVVert2_Button.installEventFilter(self)
        self.ui.Backfaces_Button.clicked.connect(self.backfaces)
        self.ui.Backfaces_Button.installEventFilter(self)
        self.ui.Orient_Button.clicked.connect(self.orient)
        self.ui.Orient_Button.installEventFilter(self)
        

        self.ui.uvSnap_Button.clicked.connect(self.uvSnap)
        self.ui.uvSnap_Button.installEventFilter(self)
        self.ui.uvSnapX.currentIndexChanged.connect(self.xResUpdate)
        self.ui.uvSnapX.installEventFilter(self)
        self.ui.uvSnapX.setCurrentIndex(jsonManager.load("UVSnapshotResX", jsonFile))
        
        self.ui.uvSnapY.currentIndexChanged.connect(self.yResUpdate)
        self.ui.uvSnapY.installEventFilter(self)
        self.ui.uvSnapY.setCurrentIndex(jsonManager.load("UVSnapshotResY", jsonFile))

        self.ui.uvTexture_Button.clicked.connect(self.uvTexture)
        self.ui.uvTexture_Button.installEventFilter(self)
        addIcon(self.ui.uvTexture_Button, 'checker.png')

        self.ui.uvTexture_ScaleUp_Button.clicked.connect(self.uvTextureScaleUp)
        self.ui.uvTexture_ScaleUp_Button.installEventFilter(self)
        self.ui.uvTexture_ScaleDown_Button.clicked.connect(self.uvTextureScaleDown)
        self.ui.uvTexture_ScaleDown_Button.installEventFilter(self)

        self.ui.hardUVs_Button.clicked.connect(self.hardUVs)
        self.ui.hardUVs_Button.installEventFilter(self)
        addIcon(self.ui.hardUVs_Button, 'uvEdges.png')

        self.ui.mergeUVs_Button.clicked.connect(self.mergeUVs)
        self.ui.mergeUVs_Button.installEventFilter(self)
        addIcon(self.ui.mergeUVs_Button, 'mergeUVs.png')

        self.ui.unwrapUVs_Button.clicked.connect(self.unfoldUVs)
        self.ui.unwrapUVs_Button.installEventFilter(self)
        addIcon(self.ui.unwrapUVs_Button, 'uvUnfold.png')


        #BAKING

        self.ui.nameHigh_Button.clicked.connect(self.nameHigh)
        self.ui.nameHigh_Button.installEventFilter(self)
        self.ui.nameLow_Button.clicked.connect(self.nameLow)
        self.ui.nameLow_Button.installEventFilter(self)
        self.ui.nameLod1_Button.clicked.connect(self.nameLod1)
        self.ui.nameLod1_Button.installEventFilter(self)
        self.ui.nameMesh_Button.clicked.connect(self.nameMesh)
        self.ui.nameMesh_Button.installEventFilter(self)
        self.ui.nameLod2_Button.clicked.connect(self.nameLod2)
        self.ui.nameLod2_Button.installEventFilter(self)
        self.ui.nameLod3_Button.clicked.connect(self.nameLod3)
        self.ui.nameLod3_Button.installEventFilter(self)
        self.ui.selectLow_Button.clicked.connect(self.selectLow)
        self.ui.selectLow_Button.installEventFilter(self)
        self.ui.selectMesh_Button.clicked.connect(self.selectMesh)
        self.ui.selectMesh_Button.installEventFilter(self)
        self.ui.selectHigh_Button.clicked.connect(self.selectHigh)
        self.ui.selectHigh_Button.installEventFilter(self)


        self.ui.pickColor_Button.clicked.connect(self.pickColor)
        bg = jsonManager.load("bgColor", jsonFile)  
        self.ui.pickColor_Button.setStyleSheet(f"background-color: rgb({bg.get('r', 0)}, {bg.get('g', 0)}, {bg.get('b', 0)});") 

        addIcon(self.ui.pickColor_Button, 'colorPicker.png')

        self.ui.nameColor_Button.clicked.connect(self.setOutlinerColor)
        addIcon(self.ui.nameColor_Button, 'outlinerColorFill.png')
  
        self.ui.wireframeColor_Button.clicked.connect(self.setWireframeColor)
        addIcon(self.ui.wireframeColor_Button, 'wireframeColorFill.png')

        self.ui.useBakeGroups.setChecked(jsonManager.load("useBakeGroups", jsonFile))
        self.ui.useBakeGroups.toggled.connect(lambda state: jsonManager.save("useBakeGroups", state, jsonFile))
        self.ui.useBakeGroups.installEventFilter(self)


        #Exploding
        self.ui.stepInput.textChanged.connect(self.stepUpdate)
        self.ui.stepInput.installEventFilter(self)
        self.ui.stepInput.setText(str(jsonManager.load("ExplodeStep", jsonFile)))
        
        self.ui.explodeNegZ_Button.clicked.connect(self.explodeNegZ)
        self.ui.explodeNegZ_Button.installEventFilter(self)
        self.ui.explodePosZ_Button.clicked.connect(self.explodePosZ)
        self.ui.explodePosZ_Button.installEventFilter(self)
        self.ui.explodeNegX_Button.clicked.connect(self.explodeNegX)
        self.ui.explodeNegX_Button.installEventFilter(self)
        self.ui.explodePosX_Button.clicked.connect(self.explodePosX)
        self.ui.explodePosX_Button.installEventFilter(self)

        self.ui.attachLow_Button.clicked.connect(self.attachLow)
        self.ui.attachLow_Button.installEventFilter(self)

        #EXPORT
    
        #MISC
        self.ui.cleanBake_Button.clicked.connect(self.cleanScene_Bake)
        self.ui.cleanBake_Button.installEventFilter(self)
        addIcon(self.ui.cleanBake_Button, 'cleanScene.png')

        self.ui.WindowFix_Button.clicked.connect(self.windowFix)
        self.ui.WindowFix_Button.installEventFilter(self)
        addIcon(self.ui.WindowFix_Button, 'windowsToOrigin.png')

        self.ui.billboard_Button.clicked.connect(self.billboard)
        self.ui.billboard_Button.installEventFilter(self)
        addIcon(self.ui.billboard_Button, 'billboard.png')
    
        self.ui.lightGroup_Button.clicked.connect(self.lightGroup)
        self.ui.lightGroup_Button.installEventFilter(self)
        addIcon(self.ui.lightGroup_Button, 'lightRig.png')

        self.ui.cameraReset_Button.clicked.connect(self.cameraReset)
        self.ui.cameraReset_Button.installEventFilter(self)
        addIcon(self.ui.cameraReset_Button, 'cameraReset.png')

        self.ui.shelf_Button.clicked.connect(self.makeShelf)
        self.ui.shelf_Button.installEventFilter(self)
        addIcon(self.ui.shelf_Button, 'icon.png')

        self.ui.info_Button.clicked.connect(self.info)
        self.ui.info_Button.installEventFilter(self)
        addIcon(self.ui.info_Button, 'info.png')

        self.ui.useGifTooltips.setChecked(jsonManager.load("useGifTooltips", jsonFile))
        self.ui.useGifTooltips.toggled.connect(lambda state: jsonManager.save("useGifTooltips", state, jsonFile))
        self.ui.useGifTooltips.installEventFilter(self)

        #Rename
        def renameAll():
            meshRename.replace(True, str(self.ui.renameOldText.text()),str(self.ui.renameNewText.text()))
        def renameSel():
            meshRename.replace(False, str(self.ui.renameOldText.text()),str(self.ui.renameNewText.text()))  

        self.ui.renameAll_Button.clicked.connect(renameAll)
        self.ui.renameAll_Button.installEventFilter(self) 
        self.ui.renameSel_Button.clicked.connect(renameSel)
        self.ui.renameSel_Button.installEventFilter(self) 
                
        self.ui.exportPathText.setText(jsonManager.load("ExportPath", jsonFile))

        #Update line edit text with changes from user browsing
        def updateExportPath():
            path = self.exportBrowse()
            self.ui.exportPathText.setText(path)
            jsonManager.save("ExportPath", path, jsonFile)


        def exportFbxAll():
            self.export(str(self.ui.exportPathText.text()), self.ui.useBakeGroups.isChecked(), False ) #Path Text + Checkbox Status
        def exportFbxSel():
            self.export(str(self.ui.exportPathText.text()), self.ui.useBakeGroups.isChecked(), True) #Path Text + Checkbox Status           

        self.ui.exportBrowse_Button.clicked.connect(updateExportPath)
        self.ui.exportBrowse_Button.installEventFilter(self)
        self.ui.exportAll_Button.clicked.connect(exportFbxAll)
        self.ui.exportAll_Button.installEventFilter(self)
        self.ui.exportSelected_Button.clicked.connect(exportFbxSel)
        self.ui.exportSelected_Button.installEventFilter(self)

        #self.ui.marmoset_Button.clicked.connect(self.marmoset)
    #@QtCore.Slot()

    
    #Functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #MENUBAR

    def exitApp(self):    #ExitButton
        self.ui.close()

    def minimizeApp(self):
        self.ui.showMinimized()

    #MODELING 
        #Pivot
    def pivOrigin(self):
        Pivot.movePiv('Origin')
    def pivX(self):
        Pivot.movePiv('X')
    def pivY(self):
        Pivot.movePiv('Y')
    def pivZ(self):
        Pivot.movePiv('Z')
    def centerPiv(self):
        Pivot.centerPiv()
    def transferPiv(self):
        Pivot.transferPiv()
    def alignPiv(self):
        Pivot.alignPiv()


    def instanceX(self):
        meshExtract.mirrorInstance(jsonManager.load("InstanceAroundOrigin", jsonFile), -1,1,1)
    def instanceY(self):
        meshExtract.mirrorInstance(jsonManager.load("InstanceAroundOrigin", jsonFile), 1,-1,1)
    def instanceZ(self):
        meshExtract.mirrorInstance(jsonManager.load("InstanceAroundOrigin", jsonFile), 1,1,-1)
    def rotateInstanceX(self):
        meshExtract.rotateInstance(jsonManager.load("RadialInstanceCount", jsonFile), jsonManager.load("InstanceAroundOrigin", jsonFile),0)
    def rotateInstanceY(self):
        meshExtract.rotateInstance(jsonManager.load("RadialInstanceCount", jsonFile), jsonManager.load("InstanceAroundOrigin", jsonFile),1)
    def rotateInstanceZ(self):
        meshExtract.rotateInstance(jsonManager.load("RadialInstanceCount", jsonFile), jsonManager.load("InstanceAroundOrigin", jsonFile),2)
    def RadialInstanceCount(self):
        jsonManager.save("RadialInstanceCount", self.ui.radialInstanceCount.value(), jsonFile)
    def removeInstances(self):
        cleanScene.removeInstances()
    def InstanceSpaceToggle():
        jsonManager.toggle("InstanceAroundOrigin", jsonFile)

    def DupDetach(self):
        meshExtract.dupExtract()
    def Detach(self):
        meshExtract.extract()
    def Combine(self):
        meshExtract.combine()
    def edgeAlign(self):
        edgeAlign.edgeAlign()
    def planar(self):
        planar.planar()
    def edgeAverage(self):
        edgeAverage.edgeAverage(False)
    def edgeAverageTarget(self):
        edgeAverage.edgeAverage(True)
    def edgeSelect(self):
        edgeSelect.edgeSelect()
    def mtUnwrap(self):
        mtWrap.mtUnwrap()
    def mtWrap(self):
        mtWrap.mtWrap()
    def mtWrapToggle(self):
        mtWrap.mtWrapToggle()
    def edgePattern(self):
        patternSelect.pattern()
    def pipe(self):
        pipe.makePipe()
    def raycastSnap(self):
        raycastSnap.Start()
    def edgeFlow(self):
        edgeAlign.edgeFlow()
    def hardEdgeSel(self):
        selection.hardEdgeSelect()
    def subdivide(self):
        selection.hardEdgeSubdivide()
    def hardEdgeToCrease(self):
        selection.hardEdgeToCrease()



    #UV
    def offsetUVs(self):
        uv.Offset()
    def symStraighten(self):
        uv.symStraighten()
    def compressUVs(self):
        uv.Compress()

    def uvMoveUp(self):
        uv.Move(0,1)
    def uvMoveDown(self):
        uv.Move(0,-1)
    def uvMoveLeft(self):
        uv.Move(-1,0)
    def uvMoveRight(self):
        uv.Move(1,0)
    def densityGet(self):
        uv.DensityGet()
    def densitySet(self):
        uv.DensitySet()
    def scaleUVHoriz1(self):
        uv.Scale(0,0.5,0.5,1)
    def scaleUVHoriz2(self):
        uv.Scale(0,0.5,2,1)
    def scaleUVVert1(self):
        uv.Scale(0.5,0,1,0.5)
    def scaleUVVert2(self):
        uv.Scale(0.5,0,1,2)
    def backfaces(self):
        uv.Backfaces()
    def orient(self):
        uv.Orient()
    def hardUVs(self):
        uv.hardenUVShellBorders()
    def mergeUVs(self):
        uv.mergeUVs()
    def unfoldUVs(self):
        uv.UnfoldUVs()
    #SnapShot
    def xResUpdate(self, input):
        Xres = int(self.ui.uvSnapX.itemText(input))

        jsonManager.save("UVSnapshotResX", self.ui.uvSnapX.currentIndex(), jsonFile)

    def yResUpdate(self, input):
        Yres = int(self.ui.uvSnapY.itemText(input))
        jsonManager.save("UVSnapshotResY", self.ui.uvSnapY.currentIndex(), jsonFile)

    def uvSnap(self):
        uv.Snapshot(jsonManager.load("UVSnapshotResX", jsonFile), jsonManager.load("UVSnapshotResY", jsonFile))

    #UV Checker
    def uvTexture(self):
        uv.applyUVMaterial(iconPath)
    def uvTextureScaleUp(self):
        uv.checkerScaleUp()
    def uvTextureScaleDown(self):
        uv.checkerScaleDown()


    #BAKING

        #Naming
    def nameHigh(self):
        meshRename.rename('_HIGH',0.965, 0.353, 0.353)
    def nameLow(self):
        meshRename.rename('_LOW', 0.337, 0.929, 0.365)
    def nameMesh(self):
        meshRename.rename('_MESH', 0.337, 0.929, 0.365)
    def nameLod1(self):
        meshRename.rename('_LOD1', 0.353, 0.612, 0.965)
    def nameLod2(self):
        meshRename.rename('_LOD2', 0.97255, 0.59608, 0.29804)
    def nameLod3(self):
        meshRename.rename('_LOD3', 0.965, 0.353, 0.353)
    def nameLod4(self):
        meshRename.rename('_LOD4', 0.804, 0.318, 0.965)
    def selectHigh(self):
        meshRename.selectMesh('_HIGH')
    def selectLow(self):
        meshRename.selectMesh('_LOW')
    def selectMesh(self):
        meshRename.selectMesh('_MESH')

    def setOutlinerColor(self):
        targetColor = self.ui.pickColor_Button.palette().background().color()
        meshRename.colorSelectedObjects(True, targetColor.red()/255,targetColor.green()/255,targetColor.blue()/255)

    def setWireframeColor(self):
        targetColor = self.ui.pickColor_Button.palette().background().color()
        meshRename.colorSelectedObjects(False, targetColor.red()/255,targetColor.green()/255,targetColor.blue()/255)

    def pickColor(self):
        ogColor = self.ui.pickColor_Button.palette().background().color()
        color = QColorDialog.getColor()

        if color.isValid():  # Ensure a color was selected
            self.ui.pickColor_Button.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
            jsonManager.save("bgColor", {"r": color.red(), "g": color.green(), "b": color.blue()}, jsonFile)

        #Exploding ( X, Z )
    def stepUpdate(self, input):
        global stepInput
        stepInput = int(input)
        jsonManager.save("ExplodeStep", stepInput, jsonFile)

    def explodeNegZ(self):
        baking.explodeMesh(0,-stepInput)
    def explodePosZ(self):
        baking.explodeMesh(0,stepInput)
    def explodeNegX(self):
        baking.explodeMesh(-stepInput,0)
    def explodePosX(self):
        baking.explodeMesh(stepInput,0)

    def attachLow(self):
        baking.attachLow()

    #EXPORT
    def cleanScene_Bake(self):
        cleanScene.Main('Bake')

    def exportBrowse(self):
        exportPath = exportFbx.exportBrowse()
        return exportPath

    def export(self, path, useBakeGroups, useSelected):#Export Fbx

        if(path):
            exportFbx.export(path, useBakeGroups, useSelected)
        else:
            cmds.warning('Choose an valid file location and try again')

    #MISC
    def pasted(self):
        nameCleaner.pasted()
    def pastedPlus(self):
        nameCleaner.pastedPlus()

    def windowFix(self):
        winFix.WinFix()

    def billboard(self):
        billboard.billboard()
    
    def lightGroup(self):
        lightGroup.lightGroup()

    def cameraReset(self):
        cleanScene.cameraReset()

    def makeShelf(self):
        shelf.Start()

    def info(self):
        import webbrowser
        webbrowser.open("https://emptyworks.gumroad.com/l/mtTools")




def addIcon(button, image):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(iconPath + '/' + image ))
    button.setIcon(icon)

def psource( module ):
	file = os.path.basename( module )
	dir = os.path.dirname( module )
	toks = file.split( '.' )
	modname = toks[0]
	if( os.path.exists( dir ) ):
		paths = sys.path
		pathfound = 0
		for path in paths:
			if(dir == path):
				pathfound = 1
		if not pathfound:
			sys.path.append( dir )
	exec ('import ' + modname) in globals()
	exec( 'reload( ' + modname + ' )' ) in globals()
	return modname

 #Custom tool tip popup. Used for Gifs
class popUpWindow(QWidget):
    def __init__(self, message, parent=None):
        super(popUpWindow, self).__init__(parent)
        self.message = message
        self.label = QLabel(self)
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowDoesNotAcceptFocus)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setStyleSheet("background: transparent; border: none; padding: 0; margin: 0;")
        self.label.setStyleSheet("background: transparent; border: 10; padding: 0; margin: 0;")
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setContentsMargins(0, 0, 0, 0)
        self.layout().setContentsMargins(0, 0, 0, 0)  # Ensure no layout margin


    def updateMessage(self, gif):

        gif = gif.replace("\\", "/")
        gif = gif.strip()

        movie = QMovie(gif)

        if movie.isValid():
            self.label.setMovie(movie)
            movie.start()
        
            self.show() 
            self.raise_() 
            self.activateWindow() 

            self.resize(movie.currentImage().size())
            self.label.resize(movie.currentImage().size())

            self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
        else:
            self.hide()

            
popUp = popUpWindow('default')



def showUI():
    try:
        import __main__

        if hasattr(__main__, 'Custom_Window'):
            try:
                __main__.Custom_Window.ui.close()
                del __main__.Custom_Window  
            except Exception as e:
                print(f"Error closing existing window: {e}")

        __main__.Custom_Window = mtToolsWindow(parent=get_maya_window())

        return __main__.Custom_Window
    except Exception as e:
        print(f"Error in showUI: {e}")
        
if __name__ == "__main__":
    showUI()

