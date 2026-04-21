"""
Author: Hoang Trong Phi -@HuangFei
Update 3/11/2024
Update 6/13/2025
"""
import os

def Make_dir(path):
    """
    Tạo thư mục tại đường dẫn được chỉ định nếu nó chưa tồn tại.
    """
    os.makedirs(path, exist_ok=True)

def Get_WD(path):
    """
    Lấy tên file và đường dẫn thư mục chứa file từ đường dẫn đầy đủ của file.
    """
    currPath = os.path.dirname(path)  # Lấy đường dẫn thư mục chứa file
    currName = os.path.basename(path)  # Lấy tên file kèm extension
    return [currName, currPath]


def Get_FileName(filePath):
    """
    Trả về tên file không có phần mở rộng từ một filePath bất kỳ.
     VD: C:/tempMaya/ExportFBX/Custom/myModel.fbx --> trả về 'myModel'
     Sử dụng os.path.splitext để tách phần mở rộng và os.path.basename để lấy tên file.
     Nếu filePath không hợp lệ hoặc không có tên file, sẽ trả về None.
    """
    return os.path.splitext(os.path.basename(filePath))[0]


def Get_FileNameExt(filePath):
    """ Trả về tên file có phần mở rộng từ một filePath bất kỳ."""
    return os.path.basename(filePath)


def find_files_with_extension(root_folder, extensions):
    """
    Duyệt toàn bộ thư mục con, trả về list path các file có đuôi extension (.fbx/.obj)
    """
    if isinstance(extensions, str):
        extensions = [extensions]

    extensions = [ext.lower() for ext in extensions]

    results = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in extensions):
                results.append(os.path.join(dirpath, filename))
    return results



