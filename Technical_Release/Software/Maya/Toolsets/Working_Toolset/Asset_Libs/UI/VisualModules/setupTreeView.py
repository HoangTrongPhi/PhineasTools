"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - Hiển thị folder tree trong Maya
    - Cho phép create, rename, delete folder
    - reload tree_folder.json khi có thay đổi
    - Sử dụng QFileSystemModel để quản lý file system
    - debug tương thích với cả PySide2 và PySide6
    - reload lại tree view khi thay đổi folder gốc
    - Cho phép chọn folder và phát emit signal khi folder được chọn
    - Cung cấp menu right-click để thao tác với folder
    - reload lại tree view sau khi thao tác tạo, đổi tên, xóa folder
"""
import os
import shutil
import subprocess
import sys
import json



#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
QTreeView = QtWidgets.QTreeView
QFileSystemModel = QtWidgets.QFileSystemModel
QDir = QtCore.QDir
QAbstractItemView = QtWidgets.QAbstractItemView
Qt = QtCore.Qt
QMessageBox = QtWidgets.QMessageBox
QMenu = QtWidgets.QMenu
QInputDialog = QtWidgets.QInputDialog
Signal = QtCore.Signal


import importlib
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as Config
importlib.reload(Config)

class FolderTreeView(QTreeView):
    # Signal phát khi thư mục được chọn
    directory_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # QFileSystemModel cho treeview hiển thị folder
        self.model = QFileSystemModel()
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.model.setReadOnly(False)  # Cho phép thao tác ghi/xóa, nhưng KHÔNG rename trực tiếp trên tree

        self.setModel(self.model)
        self.setHeaderHidden(True)
        # Không bật rename trực tiếp để tránh lỗi PySide2
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.model.setRootPath('')
        self.clicked.connect(self.on_folder_selected)
        self.setMinimumSize(200, 330)
        self.resize(200, 330)

        # Ẩn cột phụ, chỉ hiện tên folder
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)

        # Bật menu chuột phải
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def set_directory(self, path):
        # Chỉ hiển thị tree từ path hợp lệ
        if os.path.isdir(path):
            self.model.setRootPath(path)
            self.setRootIndex(self.model.index(path))

    def on_folder_selected(self, index):
        if self.model.isDir(index):
            self.directory_selected.emit(self.model.filePath(index))

    def get_selected_directory(self):
        index = self.currentIndex()
        return self.model.filePath(index) if index.isValid() else None

    def show_context_menu(self, point):
        # Tạo menu chuột phải, cho phép tạo/đổi tên/xóa folder
        index = self.indexAt(point)
        is_folder = index.isValid() and self.model.isDir(index)
        global_pos = self.viewport().mapToGlobal(point)
        menu = QMenu()
        create_action = menu.addAction("Create Folder")
        open_action = None
        rename_action = delete_action = None

        if is_folder:
            open_action = menu.addAction("Open Folder")
            rename_action = menu.addAction("Rename Folder")
            delete_action = menu.addAction("Delete Folder")
        # DÙNG exec_() cho tương thích cả PySide2 lẫn PySide6 (rất quan trọng)
        selected_action = menu.exec_(global_pos)
        if selected_action == create_action:
            parent_path = self.model.filePath(index) if is_folder else self.model.rootPath()
            self.create_folder_dialog(parent_path)

        elif open_action and selected_action == open_action:
            self.open_folder(index)

        elif rename_action and selected_action == rename_action:
            self.rename_folder(index)

        elif delete_action and selected_action == delete_action:
            self.delete_folder(self.model.filePath(index))

    def reset_filesystem_model(self, new_root):
        # Bỏ kết nối signal cũ để tránh double call
        try:
            self.clicked.disconnect()
        except Exception:
            pass
        try:
            self.customContextMenuRequested.disconnect()
        except Exception:
            pass

        self.setModel(None)
        try:
            del self.model
        except Exception:
            pass

        self.model = QFileSystemModel()
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.model.setReadOnly(False)
        self.setModel(self.model)
        self.setHeaderHidden(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.model.setRootPath(new_root)
        self.setRootIndex(self.model.index(new_root))
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        # Kết nối lại signal đúng 1 lần duy nhất!
        self.clicked.connect(self.on_folder_selected)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def create_folder_dialog(self, parent_path):
        name, ok = QInputDialog.getText(self, "New Folder", "Enter folder name:")
        if ok and name:
            new_path = os.path.join(parent_path, name)
            try:
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                    # Cập nhật lại tree_folder.json ngay lập tức
                    Config.Configuration.set_tree_folder()
                else:
                    QMessageBox.warning(self, "Error", "Folder đã tồn tại.")
            except PermissionError as e:
                QMessageBox.warning(self, "Error",
                                    "Lỗi quyền truy cập (Access Denied).\nHãy đóng hết các file, ứng dụng liên quan rồi thử lại!\n\nChi tiết: {}".format(
                                        str(e))
                                    )
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        # Reset lại hoàn toàn QFileSystemModel để giải phóng mọi handle/lock
        self.reset_filesystem_model(parent_path)


    def rename_folder(self, index):
        old_path = self.model.filePath(index)
        old_name = os.path.basename(old_path)
        parent_dir = os.path.dirname(old_path)
        new_name, ok = QInputDialog.getText(self, "Rename Folder", "New name:", text=old_name)
        if ok and new_name and new_name != old_name:
            new_path = os.path.join(parent_dir, new_name)
            if os.path.exists(new_path):
                QMessageBox.warning(self, "Error", "Tên folder đã tồn tại.")
                return
            try:
                os.rename(old_path, new_path)
                # Cập nhật lại tree_folder.json
                Config.Configuration.set_tree_folder()
            except PermissionError as e:
                QMessageBox.warning(self, "Error",
                                    "Lỗi quyền truy cập (Access Denied).\nHãy đóng hết các file, ứng dụng liên quan rồi thử lại!\n\nChi tiết: {}".format(
                                        str(e))
                                    )
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not rename folder:\n{str(e)}")
        # Reset lại model về parent_dir
        self.reset_filesystem_model(parent_dir)


    def delete_folder(self, folder_path):
        reply = QMessageBox.question(self, "Delete Folder", f"Bạn có chắc là muốn delete:\n{folder_path}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                import time
                shutil.rmtree(folder_path)
                # Cập nhật lại tree_folder.json
                Config.Configuration.set_tree_folder()
                # Dọn lại assignments
                Config.Configuration.cleaned_assignments()
            except PermissionError as e:
                QMessageBox.warning(self, "Error",
                                    "Lỗi quyền truy cập (Access Denied).\nHãy đóng hết các file, ứng dụng liên quan rồi thử lại!\n\nChi tiết: {}".format(
                                        str(e))
                                    )
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        parent_dir = os.path.dirname(folder_path)
        self.reset_filesystem_model(parent_dir)

    def open_folder(self, index=None):
        path = None

        # Ưu tiên folder đang select
        if index and index.isValid():
            path = self.model.filePath(index)

        # Nếu không có → fallback JSON
        if not path:
            json_path = os.path.join(os.path.dirname(__file__), "tree_folder.json")

            if os.path.exists(json_path):
                with open(json_path, "r") as f:
                    data = json.load(f)
                    folder_list = data.get("tree_folder_list", [])
                    if folder_list:
                        path = folder_list[0]

        if not path or not os.path.exists(path):
            QMessageBox.warning(self, "Error", "Path không hợp lệ.")
            return

        path = os.path.normpath(path)

        try:
            if sys.platform == "win32":
                subprocess.Popen(f'explorer "{path}"')
            elif sys.platform == "darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Không mở được folder:\n{str(e)}")