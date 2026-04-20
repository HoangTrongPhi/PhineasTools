"""
    Author: Hoàng Trọng Phi
    28/6/2025
"""
import maya.cmds as cmds
import os
import sys
import json
import subprocess

import gc   # bắt maya xóa GUI thừa, giải phóng bộ nhớ garbage clear
from maya import OpenMayaUI as omui
from unicodedata import category

#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
Signal = QtCore.Signal


from functools import partial  # passing args during signal function calls

import importlib

#------- Common----------
import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

import Libs.TransformFunction as TransformFunction
importlib.reload(TransformFunction)

#------- Logic Modules----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as Config
importlib.reload(Config)


# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.AssetLibs_UI as AssetLibs_UI
importlib.reload(AssetLibs_UI)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.MeshItem_UI as MeshItem_UI
importlib.reload(MeshItem_UI)

#------- UI/VisualModules----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Categories as Categories
importlib.reload(Categories)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.setupTreeView as setupTreeView
importlib.reload(setupTreeView)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Widgets.MeshItemWidget as MeshItemWidget
importlib.reload(MeshItemWidget)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.asset_tabler as asset_tabler
importlib.reload(asset_tabler)

#------- UI/VisualModules/Dialogs----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Dialogs.ConfigureDialog as ConfigureDialog
importlib.reload(ConfigureDialog)

#------- Logic Modules----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.AssetExport as AsExport
importlib.reload(AsExport)

import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.AssetSpawn as AssetSpawn
importlib.reload(AssetSpawn)
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


class Asset_Libs_Control(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ Asset_Libs_Control Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None
    filePath_requested = Signal()

    def __init__(self, parent=getMayaMainWindow()):
        super(Asset_Libs_Control, self).__init__(parent=parent)
        self.ui = AssetLibs_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setObjectName("Asset_Libs_Control_window")
        self.setWindowTitle("Asset Library")

        # Khởi tạo AssetTable
        table_widget = self.ui.tableWidget
        asset_folder = Config.Configuration.get_asset_library_path()
        assignments_dict = Config.Configuration.get_assignments_dict()
        self.asset_tabler = asset_tabler.AssetTable(
            table_widget=table_widget,
            asset_folder=asset_folder,
            assignments_dict=assignments_dict,
            max_columns=4,
            item_widget_cls=MeshItemWidget.MeshItemWidget
        )
        self.folder_tree = setupTreeView.FolderTreeView(self.ui.treeView_libs)
        #self.Categories_ctrl = Categories.Categories(self.ui.listView_Categories)
        self.ui.actionSet_Library_Path.triggered.connect(self.filePath_requested.emit)

        # Gắn action cho Refresh
        self.ui.actionRefresh.triggered.connect(self.refresh_library)
        saved_path = Config.Configuration.get_asset_library_path()
        if saved_path:
            self.folder_tree.set_directory(saved_path)

        self.Categories_control()

        #------ filter asset by category -------
        self.categories = Categories.Categories()
        self.categories.category_selected.connect(self.filter_asset_by_category)

        # refresh and clean assignments
        Config.Configuration.cleaned_assignments()
        self.reload_view()

        # LUÔN cập nhật asset_folder từ saved_path (đường dẫn thư viện đã lưu trong config)
        saved_path = Config.Configuration.get_asset_library_path()
        if saved_path:
            self.folder_tree.set_directory(saved_path)
            self.asset_tabler.update_folder(saved_path)

        # LUÔN cập nhật lại assignments_dict từ file
        self.asset_tabler.update_assignments(Config.Configuration.get_assignments_dict())

        # LUÔN gọi populate với 'All' để hiện toàn bộ asset (không filter)
        self.asset_tabler.populate("All")

        self.folder_tree.directory_selected.connect(self.on_directory_selected)

        # Kết nối signal
        self.createConnection()

    def createConnection(self):

        self.ui.actionSet_Library_Path.triggered.connect(self.open_configure_dialog)
        self.ui.btn_Add.clicked.connect(self.add_selected_mesh)

        # ------  sort all with fbx and obj
        self.ui.actionSort_All_With_FBX.triggered.connect(self.sort_all_fbx)
        self.ui.actionSort_All_with_OBJ.triggered.connect(self.sort_all_obj)

        self.sort_all()
        self.ui.rbtn_All.toggled.connect(self.handle_radio_filter)
        self.ui.rbtn_FBX.toggled.connect(self.handle_radio_filter)
        self.ui.rbtn_OBJ.toggled.connect(self.handle_radio_filter)

        # --------- sort with folder tree view ---------
        self.ui.ckb_treeFolder.stateChanged.connect(self.handle_treefolder_checkbox)

        # Connect openExplore action
        self.ui.actionOpenExplore.triggered.connect(self.openExplore)

    def table_Widget(self, category):
        if hasattr(self, 'asset_tabler'):
            self.asset_tabler.populate(category)

    def add_selected_mesh(self):
        """
        Hàm này sẽ lấy folder được chọn trong treeView, sau đó gọi hàm export_selected_mesh
        """
        selected_folder = self.folder_tree.get_selected_directory()
        if not selected_folder or not os.path.isdir(selected_folder):
            QtWidgets.QMessageBox.warning(self, "Chưa chọn folder", "Hãy chọn folder trong Library để save trước.")
            return
        export_path, thumbnail_path = AsExport.AssetExport.export_selected_mesh(self, selected_folder)
        if export_path:
            # Lấy assignments hiện tại từ file (nếu chưa có thì dict rỗng)
            assignments_dict = Config.Configuration.get_assignments_dict()

            # Lấy tên asset vừa add (không đuôi)
            asset_name = os.path.splitext(os.path.basename(export_path))[0]

            # Gán mặc định category là "All" hoặc số, ví dụ 2
            default_category = "All"  # hoặc default_category = 2 nếu bạn muốn dùng số
            assignments_dict[asset_name] = default_category

            # Lưu lại assignments ra file (phải có dòng này!)
            Config.Configuration.save_assignments(assignments_dict)

            # Update lại cho asset_tabler
            self.asset_tabler.update_assignments(assignments_dict)
            self.asset_tabler.update_folder(selected_folder)
            self.asset_tabler.populate(default_category)

    # Hàm này sẽ được gọi khi người dùng chọn một thư mục trong folder tree
    def on_directory_selected(self, folder_path):
        if self.ui.ckb_treeFolder.isChecked():
            self.sort_mesh_in_selected_folder(folder_path)
        else:
            current_category = self.ui.cbb_tableView.currentText()
            self.asset_tabler.populate(current_category)

    # Hàm mở dialog để cấu hình đường dẫn thư viện asset
    def open_configure_dialog(self):
        self.dialog = ConfigureDialog.ConfigureDialog(self)
        self.dialog.path_saved.connect(self.folder_tree.set_directory)
        self.dialog.exec()


    # -------- Categories control --------
    def Categories_control(self):
        # Tạo đối tượng categories control, gắn vào listView_Categories
        self.categories_view = Categories.Categories(self.ui.listView_Categories)
        self.ui.listView_Categories.setModel(self.categories_view.model)  # Đảm bảo model gắn đúng

        # Kết nối signal: Khi chọn category ở listView, filter asset trên table
        self.categories_view.category_selected.connect(self.on_category_selected)

        # Làm mới danh sách category cho comboBox filter
        Categories.Categories.refresh_categories(self.ui.cbb_tableView)

        # Kết nối comboBox để filter khi thay đổi
        self.ui.cbb_tableView.currentTextChanged.connect(self.on_combobox_category_changed)

    def on_category_selected(self, category_name):
        """
        Hàm này sẽ filter asset khi chọn category trên listView.
        Đồng thời cập nhật combobox filter cho đồng bộ.
        """
        # Đặt combobox filter đúng với category vừa chọn (nếu khác)
        index = self.ui.cbb_tableView.findText(category_name)
        if index >= 0:
            self.ui.cbb_tableView.setCurrentIndex(index)
        # Hiển thị asset theo category
        self.asset_tabler.populate(category_name)

    def on_combobox_category_changed(self, category_name):
        """
        Khi chọn category ở combobox filter, filter asset table (nếu cần đồng bộ 2 chiều).
        """
        self.asset_tabler.populate(category_name)


    #-------- Sort all asset by type --------
    def sort_all_fbx(self):
        asset_folder = Config.Configuration.get_asset_library_path()
        if not asset_folder or not os.path.exists(asset_folder):
            QtWidgets.QMessageBox.warning(self, "Error", "Đường dẫn Asset Library không tồn tại!")
            return
        fbx_files = CommonPyFunction.find_files_with_extension(asset_folder, ".fbx")
        self.ui.rbtn_FBX.setChecked(True)  # tự động tick radio FBX
        self.handle_radio_filter()

        if not fbx_files:
            QtWidgets.QMessageBox.information(self, "Attention", "Không tìm thấy file FBX nào!")
            return
        self.asset_tabler.populate_with_filelist(fbx_files)  # << dùng đúng asset widget

    def sort_all_obj(self):
        asset_folder = Config.Configuration.get_asset_library_path()
        if not asset_folder or not os.path.exists(asset_folder):
            QtWidgets.QMessageBox.warning(self, "Error", "Đường dẫn Asset Library không tồn tại!")
            return
        obj_files = CommonPyFunction.find_files_with_extension(asset_folder, ".obj")
        self.ui.rbtn_OBJ.setChecked(True)  # tự động tick radio FBX
        self.handle_radio_filter()

        if not obj_files:
            QtWidgets.QMessageBox.information(self, "Attention", "Không tìm thấy file OBJ nào!")
            return
        self.asset_tabler.populate_with_filelist(obj_files)

    def sort_all_usd(self):
        self.ui.rbtn_USD.setChecked(True)
        self.handle_radio_filter()

    def sort_all(self):
        self.ui.rbtn_All.setChecked(True)
        self.handle_radio_filter()

    # Hàm xử lý radio button để lọc asset theo loại
    def handle_radio_filter(self):
        # Nếu đang bật sort theo folder thì chỉ lọc file trong folder đang chọn
        if self.ui.ckb_treeFolder.isChecked():
            folder = self.folder_tree.get_selected_directory()
            if folder:
                self.sort_mesh_in_selected_folder(folder)
            return

        # Ngược lại dùng logic lọc theo radio như cũ...
        asset_folder = Config.Configuration.get_asset_library_path()
        if not asset_folder or not os.path.exists(asset_folder):
            QtWidgets.QMessageBox.warning(self, "Error", "Đường dẫn Asset Library không tồn tại!")
            return
        if self.ui.rbtn_All.isChecked():
            files = (CommonPyFunction.find_files_with_extension(asset_folder, ".fbx")
                     + CommonPyFunction.find_files_with_extension(asset_folder, ".obj"))
        elif self.ui.rbtn_FBX.isChecked():
            files = CommonPyFunction.find_files_with_extension(asset_folder, ".fbx")
        elif self.ui.rbtn_OBJ.isChecked():
            files = CommonPyFunction.find_files_with_extension(asset_folder, ".obj")
        elif self.ui.rbtn_USD.isChecked():
            files = [] # Chưa hỗ trợ USD, có thể thêm logic tương tự như FBX/OBJ, để sau này có thể mở rộng
        else:
            files = []  # không có gì được chọn
        self.asset_tabler.populate_with_filelist(files)



    #-------- Filter by category --------
    def filter_asset_by_category(self, category_name):
        """
            Hàm này sẽ lọc các asset theo category được chọn từ Categories listView.
        """
        # Đọc lại assignments từ file hoặc từ biến đã load trước
        with open("assignments.json", "r", encoding="utf-8") as f:
            assignments = json.load(f)

        # Lọc các asset thuộc category được chọn
        filtered_assets = [
            asset for asset, cat in assignments.items()
            if cat.lower() == category_name.lower() or category_name.lower() == "all"
        ]
        # Gọi hàm cập nhật view asset
        self.update_asset_view(filtered_assets)

    def update_asset_view(self, asset_list):
        self.assetView.clear()
        for asset in asset_list:
            self.assetView.addItem(asset)

    # -------- Handle tree folder checkbox --------
    def handle_treefolder_checkbox(self, state):
        # Nếu bật checkbox, update luôn mesh theo folder đang chọn
        if self.ui.ckb_treeFolder.isChecked():
            # Lọc luôn theo folder hiện tại nếu đang bật checkbox
            folder = self.folder_tree.get_selected_directory()
            if folder:
                self.sort_mesh_in_selected_folder(folder)
        else:
            # Nếu bỏ tick thì trở về logic sort all như cũ
            self.sort_all()

    def sort_mesh_in_selected_folder(self, folder_path):
        if not os.path.isdir(folder_path):
            return

        # Lọc file theo radio FBX/OBJ/ALL
        filter_exts = []
        if self.ui.rbtn_FBX.isChecked():
            filter_exts = ['.fbx']
        elif self.ui.rbtn_OBJ.isChecked():
            filter_exts = ['.obj']
        else:
            filter_exts = ['.fbx', '.obj']

        files = []
        for f in os.listdir(folder_path):
            file_path = os.path.join(folder_path, f)
            if os.path.isfile(file_path) and os.path.splitext(f)[1].lower() in filter_exts:
                files.append(file_path)

        self.asset_tabler.populate_with_filelist(files)

    #-------- Refresh Library ----
    def refresh_library(self):
        """
        Hàm này sẽ làm mới danh sách categories và cập nhật lại asset table view.
        """
        # refresh Categories
        Categories.Categories.refresh_categories(self.ui.cbb_tableView)
        if hasattr(self, 'categories_view'):
            self.categories_view.load_categories()
            # Cập nhật lại view asset cho đúng filter đang chọn
            current_category = self.ui.cbb_tableView.currentText()
            self.asset_tabler.populate(current_category)


    def reload_view(self):
        """
        Hàm này sẽ làm mới lại toàn bộ view của Asset Library.
        """
        # 1. Lấy lại folder chứa asset (có thể lấy từ config, hoặc folder tree nếu user đã chọn)
        asset_folder = Config.Configuration.get_asset_library_path()
        if not os.path.exists(asset_folder):
            QtWidgets.QMessageBox.warning(self, "Error", "Đường dẫn Asset Library không tồn tại!")
            QtWidgets.QMessageBox.warning(self, "Attention", "Hãy thiết lập lại đường dẫn thư viện Asset")

        # 2. Lấy lại assignments mới nhất từ file
        assignments_dict = Config.Configuration.get_assignments_dict()

        # 3. Cập nhật cho asset_tabler
        self.asset_tabler.update_folder(asset_folder)
        self.asset_tabler.update_assignments(assignments_dict)

        # 4. Lấy category hiện tại (All hoặc filter)
        current_category = self.ui.cbb_tableView.currentText() if self.ui.cbb_tableView.count() else "All"

        # 5. Populate lại
        self.asset_tabler.populate(current_category)

    def openExplore(self):
        asset_folder = Config.Configuration.get_asset_library_path()
        if asset_folder and os.path.exists(asset_folder):
            os.startfile(asset_folder)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Đường dẫn Asset Library không tồn tại!")
            QtWidgets.QMessageBox.warning(self, "Attention", "Bạn phải set path trước !!! ")

def openWindow():
    mayaMainWindow = getMayaMainWindow()
    objectName = "Asset_Libs_Control_window"
    for widget in mayaMainWindow.findChildren(QtWidgets.QWidget):
        if widget.objectName() == objectName:
            widget.hide()
            widget.setParent(None)
            widget.deleteLater()
    gc.collect()
    mainWin = Asset_Libs_Control(parent=mayaMainWindow)
    mainWin.setObjectName(objectName)
    mainWin.show()
    return mainWin

openWindow()

### Debug
"""
#Hàm kiểm tra lặp lại UI Zombie
def printAllAssetLibUI():
    mayaMainWindow = getMayaMainWindow()
    for widget in mayaMainWindow.findChildren(QtWidgets.QWidget):
        if "Asset" in widget.objectName():
            print(widget, widget.objectName())
printAllAssetLibUI()

#Debug trong reload view
asset_folder = Config.Configuration.get_asset_library_path()
assignments_path = Config.Configuration.get_assignments_json_path()
print("Assignments path:", assignments_path)
print("Assignments exists:", os.path.exists(assignments_path))
print("Asset folder:", asset_folder)
print("Asset folder exists:", os.path.exists(asset_folder))
print("Assignments dict:", Config.Configuration.get_assignments_dict())
print("Asset files:", os.listdir(asset_folder) if os.path.exists(asset_folder) else [])
        
"""
