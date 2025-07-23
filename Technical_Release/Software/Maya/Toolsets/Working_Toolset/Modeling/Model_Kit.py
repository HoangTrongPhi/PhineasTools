"""

Hoang Trong Phi 6/11/2025

3h39'

Đã test trên Maya 2026

"""


# Khối try-except này dùng để xác định phiên bản PySide nào có sẵn (PySide2 hoặc PySide6)
# và nhập các module cần thiết từ phiên bản đó.
# Điều này đảm bảo tính tương thích với các phiên bản Maya khác nhau.
try:
    # shiboken2 và PySide2 thường được sử dụng với các phiên bản Maya cũ hơn.
    from shiboken2 import wrapInstance
    from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QIODevice
    from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    # shiboken6 và PySide6 thường được sử dụng với các phiên bản Maya mới hơn (Maya 2022 trở lên).
    from shiboken6 import wrapInstance
    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt

# Nhập các module cần thiết từ Maya.
import maya.OpenMayaUI as omui # Giao diện người dùng Maya (để lấy cửa sổ chính của Maya)
import maya.OpenMaya as om     # Các hàm cấp thấp của Maya (không sử dụng trực tiếp nhiều trong đoạn này)

import maya.cmds as cmds # Lệnh Maya (phổ biến nhất để tương tác với Maya)
import os                # Module hệ điều hành (để làm việc với đường dẫn file, thư mục)

def maya_main_window():
    # Hàm này trả về đối tượng cửa sổ chính của Maya dưới dạng QWidget.
    # Điều này cho phép các cửa sổ tùy chỉnh được tạo ra làm cửa sổ con của Maya,
    # giúp chúng tích hợp tốt hơn vào giao diện người dùng Maya.
    main_window_ptr = omui.MQtUtil.mainWindow() # Lấy con trỏ đến cửa sổ chính của Maya
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    # wrapInstance chuyển đổi con trỏ C++ thành đối tượng Python Qt.
    # Thay 'long' bằng 'int' vì các phiên bản Maya 2022 trở đi không sử dụng 'long'.

class OverwriteDialog(QtWidgets.QDialog):
    # Lớp OverwriteDialog kế thừa từ QDialog, tạo một hộp thoại cảnh báo khi một đối tượng đã tồn tại
    # và hỏi người dùng có muốn ghi đè hay không.

    def __init__(self, parent=maya_main_window()):
        # Constructor của lớp OverwriteDialog.
        # parent được đặt mặc định là cửa sổ chính của Maya.
        super(OverwriteDialog, self).__init__(parent)

        self.setWindowTitle("Overwrite Warning") # Đặt tiêu đề cho hộp thoại.
        # Xóa nút trợ giúp ngữ cảnh trên thanh tiêu đề của hộp thoại.
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()    # Gọi hàm để tạo các widget (nhãn, nút).
        self.create_layout()     # Gọi hàm để sắp xếp các widget.
        self.create_connections() # Gọi hàm để kết nối các tín hiệu/khe cắm.

    def create_widgets(self):
        # Tạo các widget cho hộp thoại cảnh báo.
        self.warning_label = QtWidgets.QLabel("Object name already exists! Do you want to overwrite?")
        self.okay_btn = QtWidgets.QPushButton("Overwrite") # Nút "Ghi đè".
        self.cancel_btn = QtWidgets.QPushButton("Cancel") # Nút "Hủy bỏ".

    def create_layout(self):
        # Sắp xếp các widget bằng QLayouts.
        label_layout = QtWidgets.QHBoxLayout() # Layout ngang cho nhãn cảnh báo.
        label_layout.addWidget(self.warning_label)

        button_layout = QtWidgets.QHBoxLayout() # Layout ngang cho các nút.
        button_layout.addSpacing(2) # Thêm khoảng cách nhỏ.
        button_layout.addWidget(self.okay_btn)
        button_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self) # Layout dọc chính cho toàn bộ hộp thoại.
        main_layout.addLayout(label_layout)   # Thêm layout nhãn.
        main_layout.addLayout(button_layout)  # Thêm layout nút.

    def create_connections(self):
        # Kết nối các tín hiệu từ các nút đến các khe cắm tương ứng.
        self.okay_btn.clicked.connect(self.accept) # Khi nút "Overwrite" được click, hộp thoại chấp nhận (trả về QDialog.Accepted).
        self.cancel_btn.clicked.connect(self.close) # Khi nút "Cancel" được click, hộp thoại đóng.


class ModelKitDialog(QtWidgets.QDialog):
    # Lớp ModelKitDialog là giao diện chính của công cụ Model Kit.

    WINDOW_TITLE = "Model Kit" # Tiêu đề cửa sổ của công cụ.

    def __init__(self, parent=maya_main_window()):
        # Constructor của lớp ModelKitDialog.
        # parent được đặt mặc định là cửa sổ chính của Maya.
        super(ModelKitDialog, self).__init__(parent)

        # Khởi tạo các biến để lưu trữ đường dẫn thư mục, đường dẫn ảnh, tên camera, và tên file.
        self.folder_path = None
        self.img_path = None
        self.cameraName = None
        self.filename = None

        self.setWindowTitle(self.WINDOW_TITLE) # Đặt tiêu đề cửa sổ.
        # Xóa nút trợ giúp ngữ cảnh trên thanh tiêu đề.
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setMinimumWidth(625)  # Đặt chiều rộng tối thiểu.
        self.setMinimumHeight(220) # Đặt chiều cao tối thiểu.
        self.create_widgets()     # Tạo các widget.
        self.create_layout()      # Sắp xếp layout.
        self.create_connections() # Kết nối các tín hiệu.

    def create_widgets(self):
        # Tạo các widget được sử dụng trong giao diện ModelKitDialog.
        self.table_wdg = QtWidgets.QTableWidget() # Bảng để hiển thị các mô hình.
        self.table_wdg.setColumnCount(5)         # Đặt số cột là 5.
        for each in range(0, self.table_wdg.columnCount()):
            self.table_wdg.setColumnWidth(each, 120) # Đặt chiều rộng cho mỗi cột.
        self.table_wdg.setRowCount(1)             # Đặt số hàng ban đầu là 1.
        self.table_wdg.setRowHeight(0, 120)       # Đặt chiều cao hàng đầu tiên.
        
        self.libraryload_lable = QtWidgets.QLabel("Library Folder") # Nhãn cho đường dẫn thư mục thư viện.
        self.libraryload_le = QtWidgets.QLineEdit()                 # Line edit để hiển thị/nhập đường dẫn.
        self.select_lib_path_btn = QtWidgets.QPushButton("")        # Nút để chọn thư mục.
        # Đặt biểu tượng cho nút chọn thư mục (biểu tượng fileOpen của Qt).
        self.select_lib_path_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        self.load_library_btn = QtWidgets.QPushButton("Load Existing") # Nút để tải thư viện hiện có.

        self.add_btn = QtWidgets.QPushButton("Add Object")   # Nút để thêm đối tượng.
        self.close_btn = QtWidgets.QPushButton("Close")     # Nút để đóng cửa sổ.

    def create_layout(self):
        # Sắp xếp các widget bằng QLayouts.
        lib_loader_layout = QtWidgets.QHBoxLayout() # Layout cho phần tải thư viện.
        lib_loader_layout.addWidget(self.libraryload_lable)
        lib_loader_layout.addWidget(self.libraryload_le)
        lib_loader_layout.addWidget(self.select_lib_path_btn)
        lib_loader_layout.addWidget(self.load_library_btn)

        button_layout = QtWidgets.QHBoxLayout() # Layout cho các nút hành động chính.
        button_layout.addSpacing(2)
        button_layout.addStretch() # Đẩy các nút sang phải.
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self) # Layout dọc chính của cửa sổ.
        main_layout.setContentsMargins(2,2,2,2) # Đặt lề cho layout.
        main_layout.addSpacing(2)
        main_layout.addLayout(lib_loader_layout) # Thêm layout tải thư viện.
        main_layout.addWidget(self.table_wdg)    # Thêm bảng.
        main_layout.addLayout(button_layout)     # Thêm layout nút.

    def create_connections(self):
        # Kết nối các tín hiệu từ các widget đến các hàm xử lý.
        self.select_lib_path_btn.clicked.connect(self.show_folder_select_dialog) # Mở hộp thoại chọn thư mục.
        self.load_library_btn.clicked.connect(self.load_existing_library)       # Tải thư viện hiện có.

        self.add_btn.clicked.connect(self.export_geo) # Xuất đối tượng.
        self.close_btn.clicked.connect(self.close)   # Đóng cửa sổ.
        self.table_wdg.cellClicked.connect(self.table_cell_clicked) # Xử lý khi một ô trong bảng được click.

    def show_folder_select_dialog(self):
        # Hiển thị hộp thoại chọn thư mục và tạo thư mục 'images' nếu chưa có.
        self.launch_libfolder_sel_window() # Mở hộp thoại chọn thư mục.
        # Tạo đường dẫn đến thư mục 'images' bên trong thư mục thư viện đã chọn.
        self.img_path = os.path.join(self.folder_path, "images")
        self.img_path = os.path.normpath(self.img_path) # Chuẩn hóa đường dẫn.
        isDir = os.path.isdir(self.img_path)            # Kiểm tra xem thư mục 'images' có tồn tại không.
        if not isDir:
            os.makedirs(self.img_path) # Nếu không, tạo thư mục.

    def load_existing_library(self):
        # Tải các mô hình .obj hiện có từ thư mục thư viện đã chọn vào bảng.
        file_type = "obj"
        libfolder_le_text = self.libraryload_le.text() # Lấy đường dẫn thư mục từ line edit.

        if not libfolder_le_text:
            self.show_folder_select_dialog() # Nếu chưa có đường dẫn, yêu cầu người dùng chọn.
        else:
            # Lấy danh sách các file .obj trong thư mục.
            files = cmds.getFileList(folder=libfolder_le_text, filespec='*.%s' % file_type)

            if len(files) == 0:          
                cmds.warning("No Files to Import") # Cảnh báo nếu không có file nào.
            else:
                for f in files:
                    obj_name = os.path.splitext(f)[0] # Lấy tên đối tượng từ tên file (không có phần mở rộng).
                    self.create_filepath(obj_name) # Tạo đường dẫn file đầy đủ cho đối tượng.
                    obj_exists = self.check_obj_exists(self.filename)[0] # Kiểm tra xem đối tượng đã có trong bảng chưa.
                    if not obj_exists:
                        emptyIndex = self.find_empty_cell() # Tìm một ô trống trong bảng.
                        # Tạo đường dẫn đến ảnh thumbnail của đối tượng.
                        obj_img_name = os.path.join(self.img_path, obj_name + ".jpg")
                        obj_img_name = os.path.normpath(obj_img_name)
                        img_exists = cmds.file(obj_img_name, q=True, ex=True) # Kiểm tra xem ảnh thumbnail có tồn tại không.
                        if img_exists:
                            cropImage = self.create_img(obj_img_name) # Tạo ảnh đã cắt.
                            self.add_cell(emptyIndex, cropImage, True) # Thêm ô với ảnh.
                        else:
                            self.add_cell(emptyIndex, None, False) # Thêm ô không có ảnh (sẽ có màu đỏ).
                    else:
                        print("{0} ".format(obj_name) + "already exists") # In ra nếu đối tượng đã tồn tại.

    def export_geo(self):
        # Xuất đối tượng đã chọn trong Maya vào thư mục thư viện và tạo ảnh thumbnail.
        # Nếu tên đối tượng đã tồn tại, hỏi người dùng có muốn ghi đè không.
        
        objSel = cmds.ls(sl=True) # Lấy danh sách đối tượng được chọn.
        sel = cmds.ls(sl=True, type='transform', dag=True, ni=True) # Lấy đối tượng transform được chọn (không phải instance).
        
        if sel: # Nếu có đối tượng được chọn.
            if self.folder_path == None:
                self.show_folder_select_dialog() # Yêu cầu chọn thư mục nếu chưa có.
                cmds.warning("Please select folder path!")
            else:
                self.create_filepath(sel[0]) # Tạo đường dẫn file cho đối tượng được xuất.
                obj_exists, index = self.check_obj_exists(self.filename) # Kiểm tra xem đối tượng đã tồn tại trong bảng chưa.
                if not obj_exists: # Nếu đối tượng chưa tồn tại.
                    # Đặt đối tượng về gốc tọa độ thế giới để xuất mà không bị bù trừ.
                    pos = self.center_obj(objSel[0])
                    
                    thumbnail_image = self.save_file_create_thumbnail(sel[0]) # Lưu file và tạo thumbnail.
                    emptyIndex = self.find_empty_cell() # Tìm ô trống trong bảng.
                    self.add_cell(emptyIndex, thumbnail_image, True) # Thêm ô mới với thumbnail.
                    print("Export of {0} successful in cell {1}".format(self.filename, emptyIndex))
                    
                    # Trả đối tượng về vị trí ban đầu.
                    self.return_obj(objSel[0],pos)
                else: # Nếu đối tượng đã tồn tại.
                    cmds.warning("Obj Exists: {0}".format(self.filename)) # Cảnh báo.
                    overwrite_dialog = OverwriteDialog() # Mở hộp thoại cảnh báo ghi đè.
                    result = overwrite_dialog.exec_()

                    if result == QtWidgets.QDialog.Accepted: # Nếu người dùng chọn "Overwrite".
                        pos = self.center_obj(objSel[0]) # Đặt đối tượng về gốc tọa độ.
                        thumbnail_image = self.save_file_create_thumbnail(sel[0]) # Lưu file và tạo thumbnail.
                        self.overwrite_cell(thumbnail_image, index) # Ghi đè ô trong bảng.
                        self.return_obj(objSel[0],pos) # Trả đối tượng về vị trí ban đầu.

        else: # Nếu không có đối tượng nào được chọn.
            cmds.warning("Select a mesh object to export!") # Cảnh báo yêu cầu chọn đối tượng.

    def launch_libfolder_sel_window(self):
        # Mở hộp thoại chọn thư mục và cập nhật đường dẫn vào line edit.
        self.folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Library Folder")
        self.libraryload_le.setText(self.folder_path)

    def overwrite_cell(self, pixmapImg, index):
        # Cập nhật một ô hiện có trong bảng với ảnh thumbnail mới.
        existing_cell = (self.table_wdg.item(index[0], index[1]))

        if existing_cell:
            self.set_tooltip_and_text(existing_cell) # Đặt tooltip và text cho ô.
            label = QtWidgets.QLabel()              # Tạo QLabel để hiển thị ảnh.
            label.setScaledContents(True)           # Cho phép ảnh tự điều chỉnh kích thước.
            label.setPixmap(pixmapImg)              # Đặt ảnh cho QLabel.
            self.table_wdg.setCellWidget(index[0], index[1], label) # Đặt QLabel vào ô.

            print("Overwrite of {0} successful at {1}".format(self.filename, index))

    def create_filepath(self, obj_name):
        # Tạo đường dẫn file đầy đủ cho đối tượng (bao gồm thư mục, tên đối tượng và phần mở rộng .obj).
        self.filename = os.path.join(self.libraryload_le.text(), obj_name + ".obj")
        self.filename = os.path.normpath(self.filename) # Chuẩn hóa đường dẫn.
        
    def check_obj_exists(self, filename):
        # Kiểm tra xem tên đối tượng (dựa trên filename) có tồn tại trong các ô của bảng không.
        # Trả về True/False và chỉ số của ô nếu tìm thấy.
        rowCount = self.table_wdg.rowCount()
        colCount = self.table_wdg.columnCount()
        for i in range(0, rowCount):
            for j in range(0, colCount):
                cellQuery = self.table_wdg.item(i,j) # Lấy item tại ô (i, j).
                if cellQuery and cellQuery.text() == filename: # Nếu item tồn tại và text trùng khớp.
                    exists = True
                    cellIndex = (i,j) # Lưu chỉ số của ô.
                    return exists, cellIndex # Trả về True và chỉ số.
        exists = False
        cellIndex = (0,0) # Nếu không tìm thấy, trả về False và chỉ số mặc định.
        return exists, cellIndex
    
    def center_obj(self, selection):
        # Di chuyển đối tượng đã chọn về gốc tọa độ thế giới (0,0,0) để xuất.
        # Lưu lại vị trí ban đầu của đối tượng.
        pos = cmds.xform(selection, query=True, worldSpace=True, translation=True) # Lấy vị trí hiện tại.
        # Tạo một transform tạm thời tại gốc tọa độ thế giới.
        temp_transform = cmds.createNode("transform")  
        cmds.matchTransform(selection, temp_transform, position=True) # Di chuyển đối tượng đến vị trí của transform tạm thời.
        cmds.delete(temp_transform) # Xóa transform tạm thời.
        cmds.select(selection) # Chọn lại đối tượng ban đầu.
        return pos # Trả về vị trí ban đầu.
    
    def return_obj(self, selection, pos):
        # Trả đối tượng về vị trí ban đầu của nó.
        cmds.xform(selection, worldSpace=True, translation=(pos[0],pos[1],pos[2]))    

    def save_file_create_thumbnail(self, selection):
        # Lưu đối tượng đã chọn dưới dạng .obj và tạo ảnh thumbnail.
        # Tham số: f=1 (force overwrite), pr=1 (preserve references), typ="OBJexport", es=1 (export selection), op (options for OBJ export).
        cmds.file(self.filename,f=1,pr=1,typ="OBJexport",es=1,op="groups=0; ptgroups=0; materials=0; smoothing=1; normals=1")
        imageSnapshot = self.save_snapshot(selection) # Chụp ảnh màn hình làm thumbnail.
        thumbnail_image = self.create_img(imageSnapshot) # Tạo ảnh đã cắt.
        return thumbnail_image

    def create_img_cam(self):
        # Tạo một camera mới với các thuộc tính cụ thể để chụp ảnh thumbnail.
        self.cameraName = cmds.camera(fl=75) # Tạo camera với tiêu cự 75mm.
        # Đặt vị trí và xoay của camera.
        cmds.xform(self.cameraName, r=True, t=(2.6, 2.35, 3), ro=(-30.0, 40.0, 0.0))

    def return_to_perspCam(self):
        # Trở lại camera phối cảnh mặc định của Maya ('persp').
        cmds.select('persp')
        perspCam = cmds.ls(sl=True)
        cmds.lookThru(perspCam) # Đặt chế độ xem qua camera 'persp'.

    def save_snapshot(self, geo):
        # Tạo camera mới, cô lập đối tượng đã chọn, căn khung hình và chụp ảnh.
        # Sau đó xóa camera và trở lại camera phối cảnh ban đầu.
        self.create_img_cam()       # Tạo camera mới.
        cmds.lookThru(self.cameraName) # Đặt chế độ xem qua camera mới.
        cmds.select(geo)            # Chọn đối tượng cần chụp.

        # Xử lý chế độ isolate select của panel 'modelPanel4'.
        # Nếu đang ở chế độ isolate, tắt và bật lại để cập nhật, sau đó thêm đối tượng vào isolate.
        # Nếu không, bật isolate và thêm đối tượng.
        if cmds.isolateSelect('modelPanel4', q=True, state=True):
            cmds.isolateSelect('modelPanel4', state=False)
            cmds.isolateSelect('modelPanel4', state=True)
            cmds.isolateSelect('modelPanel4', addSelected=True)
        else:
            cmds.isolateSelect('modelPanel4', state=True)
            cmds.isolateSelect('modelPanel4', addSelected=True)

        cmds.viewFit() # Căn khung hình để đối tượng vừa vặn trong khung nhìn.
        # Tạo đường dẫn file cho ảnh chụp màn hình.
        imageSnapshot = (os.path.join(self.img_path, geo)) + ".jpg"
        imageSnapshot = os.path.normpath(imageSnapshot)
        # Chụp ảnh màn hình và lưu dưới dạng JPG.
        cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
        cmds.isolateSelect('modelPanel4', state=False) # Tắt chế độ isolate select.
        self.return_to_perspCam() # Trở lại camera phối cảnh.
        if self.cameraName:
            cmds.delete(self.cameraName[0]) # Xóa camera đã tạo.

        return imageSnapshot # Trả về đường dẫn của ảnh chụp.

    def create_img(self, img_path):
        # Tạo đối tượng QPixmap từ đường dẫn ảnh và cắt ảnh thành hình vuông.
        pixmap = QtGui.QPixmap(img_path) # Tải ảnh vào QPixmap.
        img_size = pixmap.size()         # Lấy kích thước ảnh.
        img_width = img_size.width()
        img_height = img_size.height()

        # Tính toán vùng cắt để có hình vuông.
        if img_height > img_width:
            crop_height = (img_height-img_width)/2
            cropSize = QtCore.QRect(0, crop_height, img_width, img_width)
        else:
            crop_width = (img_width-img_height)/2
            cropSize = QtCore.QRect(crop_width, 0, img_height, img_height)
        
        croppedPixmap = QtGui.QPixmap.copy(pixmap, cropSize) # Cắt ảnh.
        return croppedPixmap # Trả về QPixmap đã cắt.

    def find_empty_cell(self):
        # Tìm một ô trống trong bảng QTableWidget.
        # Nếu không có ô trống, tự động thêm một hàng mới.
        rowCount = self.table_wdg.rowCount()
        colCount = self.table_wdg.columnCount()

        for i in range(0, rowCount):
            for j in range(0, colCount):
                cellQuery = self.table_wdg.item(i,j) # Kiểm tra item tại ô (i,j).
                if not cellQuery: # Nếu ô trống.
                    emptyIndex = (i,j)
                    return emptyIndex # Trả về chỉ số của ô trống.
                else:
                    # Nếu đang ở ô cuối cùng của bảng và không tìm thấy ô trống.
                    if i == (rowCount - 1) and j == (colCount - 1):
                        self.table_wdg.insertRow(rowCount) # Thêm một hàng mới.
                        self.table_wdg.setRowHeight(rowCount, 120) # Đặt chiều cao hàng mới.
                        emptyIndex = (rowCount, 0) # Ô trống đầu tiên của hàng mới.
                        return emptyIndex

    def set_tooltip_and_text(self, item):
        # Đặt tooltip và text cho một QTableWidgetItem.
        item.setToolTip(self.filename) # Tooltip sẽ là đường dẫn file đầy đủ.
        item.setText(self.filename)    # Text của ô cũng là đường dẫn file.

    def add_cell(self, emptyIndex, pixmapImg, isNew):
        # Thêm một ô mới vào bảng tại chỉ số emptyIndex.
        # Hiển thị ảnh thumbnail hoặc một màu nền đỏ nếu không có ảnh.
        cellItem = QtWidgets.QTableWidgetItem()
        # Đặt cờ để ô không thể chỉnh sửa được.
        cellItem.setFlags(cellItem.flags() & ~ QtCore.Qt.ItemIsEditable)
        self.set_tooltip_and_text(cellItem) # Đặt tooltip và text.
        label = QtWidgets.QLabel()           # Tạo QLabel để hiển thị ảnh.

        if not pixmapImg:
            # TODO - set a better label, option to pick image or take new one
            cellItem.setBackground(QtGui.QColor("red")) # Nếu không có ảnh, đặt nền đỏ.
        else:
            label.setScaledContents(True) # Cho phép ảnh tự điều chỉnh kích thước.
            label.setPixmap(pixmapImg)    # Đặt ảnh cho QLabel.
        self.table_wdg.setCellWidget(emptyIndex[0], emptyIndex[1], label) # Đặt QLabel vào ô.
        self.table_wdg.setItem(emptyIndex[0], emptyIndex[1], cellItem)    # Đặt QTableWidgetItem vào ô.

    def get_cell_text(self, row, col):
        # Lấy text (đường dẫn file) từ một ô cụ thể trong bảng.
        cellItem = self.table_wdg.item(row, col)
        if cellItem:
            cell_text = cellItem.text()
            return cell_text
        else:
            return None

    def import_object(self, obj_path):
    
        nameSpc = "ImportedObj" # Tên namespace sẽ được sử dụng khi import.

        #TODO - add ability to import aligned to face selection

        if cmds.file(obj_path, q=True, ex=True): # Kiểm tra xem file có tồn tại không.
            if not cmds.namespace( exists=nameSpc): # Nếu namespace chưa tồn tại, tạo mới.
                cmds.namespace(add=nameSpc)
            
            cmds.namespace(set=nameSpc) # Đặt namespace hiện tại là "ImportedObj".
            
            # Import file .obj vào Maya. rnn=True (return new nodes - trả về các node mới được tạo).
            imported_objects = cmds.file(obj_path, i=True, ns="Import", rnn=True)
            # Reset namespace về rỗng sau khi import.
            cmds.namespace(set=":")
            
            objName, ext = os.path.splitext(os.path.basename(obj_path)) # Lấy tên đối tượng từ đường dẫn file.
            
            transforms = cmds.ls(imported_objects, type='transform') # Lấy tất cả các node transform được import.

            cmds.select(transforms[0], r=True) # Chọn node transform đầu tiên.
            
            cmds.rename(transforms[0], objName) # Đổi tên node transform thành tên đối tượng.
      
        else:
            #TODO - turn into error pop-up
            cmds.warning("No files found?!?") # Cảnh báo nếu file không được tìm thấy.

    def table_cell_clicked(self, *args):
        # Xử lý sự kiện khi một ô trong bảng được click.
        row = args[0] # Hàng của ô được click.
        col = args[1] # Cột của ô được click.
        obj_path = self.get_cell_text(row, col) # Lấy đường dẫn file từ ô.
        if obj_path:
            self.import_object(obj_path) # Nếu có đường dẫn, import đối tượng.
        else:
            cmds.warning("Chosen cell is empty!") # Cảnh báo nếu ô trống.


if __name__ == "__main__":
    # Đây là phần mã sẽ chạy khi script được thực thi trực tiếp trong Maya.
    # Nó kiểm tra xem cửa sổ công cụ đã được mở chưa và đóng/xóa nó trước khi mở lại.
    try:
        open_import_dialog.close()      # Đóng cửa sổ nếu nó đã mở.
        open_import_dialog.deleteLater() # Xóa đối tượng cửa sổ khỏi bộ nhớ.
    except:
        pass # Bỏ qua nếu cửa sổ chưa tồn tại (ví dụ: lần chạy đầu tiên).

    open_import_dialog = ModelKitDialog() # Tạo một thể hiện mới của ModelKitDialog.
    open_import_dialog.show()             # Hiển thị cửa sổ công cụ.