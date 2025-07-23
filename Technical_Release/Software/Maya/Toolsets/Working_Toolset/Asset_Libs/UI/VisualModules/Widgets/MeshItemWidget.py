"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - UI cho mỗi item asset trong danh sách
    - Hiển thị tên asset, thumbnail (nếu có), và cho phép người dùng click để chọn asset
    - Cho phép người dùng click chuột phải để mở menu với các tùy chọn như Rename, Properties, Delete
"""




#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

import os
from Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI import MeshItem_UI

import importlib

#-------- config thông tin ----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)

#--------- UI/Vísual Modules/Dialog ( PropertiesDialog: right-click UI) -----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Dialogs.PropertiesDialog as PropertiesDialog
importlib.reload(PropertiesDialog)

#--------- UI/Vísual Modules/Dialog (RenameAssetDialog :rename asset) -----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.UI.VisualModules.Dialogs.RenameAssetDialog as RenameAssetDialog
importlib.reload(RenameAssetDialog)

#--------- Logic Modules/Asset Spawn -----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.AssetSpawn as spawn_asset
importlib.reload(spawn_asset)

#--------- Logic Modules/Configuration -----------
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)


class MeshItemWidget(QtWidgets.QWidget):
    """
        Tín hiệu sẽ phát ra khi người dùng click vào asset
        Gửi đi đường dẫn file asset tương ứng
    """
    clicked = QtCore.Signal(str)    # Tín hiệu phát khi item được click trái

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)
        self.ui = MeshItem_UI.Ui_meshItem()
        self.ui.setupUi(self)

        # Lưu đường dẫn tới file asset (ví dụ: .fbx/.obj)
        self.file_path = file_path

        self.folder = os.path.dirname(file_path)

        # Lấy tên asset từ file (không bao gồm phần mở rộng)
        self.asset_name, self.ext = os.path.splitext(os.path.basename(file_path))
        # Hiển thị tên asset lên label trong UI
        self.ui.nameLabel.setText(self.asset_name)

        # Tìm đường dẫn thumbnail (ảnh preview) cùng tên với file asset
        thumbnail_path = os.path.splitext(file_path)[0] + ".png"
        # Nếu thumbnail tồn tại, hiển thị nó vào imageLabel
        if os.path.exists(thumbnail_path):
            pixmap = QtGui.QPixmap(thumbnail_path)
            self.ui.imageLabel.setPixmap(
                pixmap.scaled(160, 160, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            )

        # Khi người dùng click vào nút (thumbnail), phát tín hiệu clicked
        self.ui.pushButton.clicked.connect(self._on_click)
        # Kích hoạt menu chuột phải trên nút
        self.ui.pushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.pushButton.customContextMenuRequested.connect(self._show_context_menu)

    def _on_click(self):
        # Gửi tín hiệu đã click và truyền file_path ra ngoài
        self.clicked.emit(self.file_path)
        # Import asset bằng AssetSpawner
        spawn_asset.AssetSpawner.spawn_asset(self.file_path)

    def _show_context_menu(self, pos):
        # Hiển thị menu chuột phải tại vị trí global
        global_pos = self.ui.pushButton.mapToGlobal(pos)
        menu = QtWidgets.QMenu()
        rename_action = menu.addAction("Rename")        # Thêm tùy chọn đổi tên
        properties_action = menu.addAction("Properties") # Thêm tùy chọn xem thuộc tính
        menu.addSeparator()
        delete_action = menu.addAction("Delete")

        # Hiển thị menu và xử lý hành động người dùng chọn
        action = menu.exec_(global_pos)
        if action == delete_action:
            self._confirm_deletion()
        elif action == properties_action:
            self._open_properties()
        elif action == rename_action:
            self._rename_asset()

    def _confirm_deletion(self):
        # Hiển thị hộp thoại xác nhận xóa asset
        reply = QtWidgets.QMessageBox.question(
            self,
            "Delete Asset",
            f"Delete '{self.asset_name}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                # Xóa file asset chính
                if os.path.exists(self.file_path):
                    os.remove(self.file_path)
                # Xóa thumbnail nếu có
                thumbnail_path = os.path.splitext(self.file_path)[0] + ".png"
                if os.path.exists(thumbnail_path):
                    os.remove(thumbnail_path)

                # Xóa liên kết assignment nếu có
                assignments = config_module.Configuration.load_assignments()
                if self.asset_name in assignments:
                    del assignments[self.asset_name]
                    config_module.Configuration.save_assignments(assignments)

                # XÓA METADATA TRONG MESH_DATA.JSON
                # dùng đúng tên file (có extension) làm key
                asset_filename = os.path.basename(self.file_path)
                config_module.Configuration.remove_mesh_data(asset_filename)

                # Gỡ widget khỏi giao diện và tự hủy
                self.setParent(None)
                self.deleteLater()

            except Exception as e:
                # Báo lỗi nếu có vấn đề trong quá trình xóa
                QtWidgets.QMessageBox.warning(self, "Error", f"Failed to delete: {str(e)}")

    def _open_properties(self):
        # Mở hộp thoại thuộc tính của asset (PropertiesDialog)
        dialog = PropertiesDialog.PropertiesDialog(self.file_path, self)
        # Không còn kết nối signal đổi tên file nữa!
        dialog.exec_()


    #----- Rename Asset -----
    def _rename_asset(self):
        asset_filename = os.path.basename(self.file_path)
        mesh_data = config_module.Configuration.get_mesh_data(asset_filename)
        if not mesh_data:
            QtWidgets.QMessageBox.warning(self, "Error", "Không tìm thấy dữ liệu mesh_data cho asset này.")
            return

        # Hiện dialog nhập tên mới
        dialog = RenameAssetDialog.RenameAssetDialog(self.asset_name, self)
        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return
        new_name = dialog.get_new_name()
        if not new_name or new_name == self.asset_name:
            return

        # Kiểm tra trùng tên file
        new_asset_filename = new_name + self.ext
        new_path = os.path.join(self.folder, new_asset_filename)
        if os.path.exists(new_path):
            QtWidgets.QMessageBox.warning(self, "Error", "Tên file đã tồn tại.")
            return

        try:
            # Đổi tên file asset
            os.rename(self.file_path, new_path)
            # Đổi tên thumbnail nếu có
            old_thumb = os.path.splitext(self.file_path)[0] + ".png"
            new_thumb = os.path.splitext(new_path)[0] + ".png"
            if os.path.exists(old_thumb):
                os.rename(old_thumb, new_thumb)

            # Đổi key trong mesh_data.json
            config_module.Configuration.rename_mesh_data(asset_filename, new_asset_filename)
            # (Bạn cần cài đặt thêm hàm rename_mesh_data trong Configuration nếu chưa có)

            # Đổi tên trong assignment nếu có
            assignments = config_module.Configuration.load_assignments()
            if self.asset_name in assignments:
                assignments[new_name] = assignments[self.asset_name]
                del assignments[self.asset_name]
                config_module.Configuration.save_assignments(assignments)

            # Cập nhật lại widget
            self.file_path = new_path
            self.asset_name = new_name
            self.ui.nameLabel.setText(self.asset_name)
            QtWidgets.QMessageBox.information(self, "Done", "Đã đổi tên asset thành công.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Rename failed:\n{e}")
