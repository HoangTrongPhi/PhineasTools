"""
Author: Hoang Trong Phi -@HuangFei
Update 3/11/2024
Update 6/13/2025
"""
import os

def Make_dir(path):
    """
        input a path to check if it exists, if not, it creates all the path
        :return: path string
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def Get_WD(path):
    """
    Tách tên file và đường dẫn cha của một file.
    Trả về [tên file (kèm extension), thư mục chứa file]
    """
    currPath = os.path.dirname(path)  # Lấy đường dẫn thư mục chứa file
    currName = os.path.basename(path)  # Lấy tên file kèm extension
    return [currName, currPath]


def Get_FileName(filePath):
    """
    Lấy tên file KHÔNG kèm phần mở rộng từ đường dẫn file đầu vào.

    Ví dụ:
        filePath = C:/folder/data/myfileFBX.txt
        → return myfileFBX
    """
    currWD = Get_WD(filePath)  # Lấy danh sách [tên file, thư mục]
    nameFileExt = os.path.basename(currWD[0])  # currWD[0] là tên file kèm extension
    nameFile = os.path.splitext(nameFileExt)[0]  # Tách phần tên khỏi phần extension
    return nameFile  # Trả lại tên file không có phần mở rộng


# Trả về tên file kèm phần mở rộng từ một filePath bất kỳ
# Nhận filePath làm đối số → dùng được cho nhiều file khác nhau, tổng quát hơn.
# Trả về cả tên file và phần mở rộng, không tách riêng.
def Get_FileNameExt(filePath):
    """Get File Name with extension from File Path"""
    currWD = Get_WD(filePath)
    nameFileExt = os.path.basename(currWD[0])
    return nameFileExt


def find_files_with_extension(root_folder, extension):
    """
    Duyệt toàn bộ thư mục con, trả về list path các file có đuôi extension (.fbx/.obj)
    """
    results = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                results.append(os.path.join(dirpath, filename))
    return results
