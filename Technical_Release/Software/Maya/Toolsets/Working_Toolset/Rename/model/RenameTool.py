
#from Qt import QtCore, QtWidgets, QtGui
import sys, os, json
import importlib
import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

try:
    from shiboken2 import wrapInstance
    import maya.cmds as cmds, maya.mel as mel, maya.OpenMayaUI as omui, maya.api.OpenMaya as om
    print ('Import success Maya Module, shiboken2')
except:
    from shiboken6 import wrapInstance
    import maya.cmds as cmds, maya.mel as mel, maya.OpenMayaUI as omui, maya.api.OpenMaya as om
    print('Import success Maya Module, shiboken6')
else:
    pass

def getDirectoryofModule(modulename):
    """
    Input: module as string
    OUtput:
        List: name as string and directory of module
    """
    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = CommonPyFunction.Get_WD(module.__file__)
    return currWD


def rename_objects(mode, prefix="", suffix="", rename_base="", start=None, padding=None):
    """
    Đổi tên các đối tượng đang được chọn trong Maya theo các chế độ khác nhau.
    """
    objs = cmds.ls(sl=True, long=True)
    if not objs:
        cmds.warning("No objects selected!")
        return []

    # Kiểm tra dữ liệu đầu vào theo mode
    if mode == 1 and not prefix:
        cmds.warning("Prefix is empty!")
        return []
    elif mode == 2 and not suffix:
        cmds.warning("Suffix is empty!")
        return []
    elif mode == 3:
        if not rename_base:
            cmds.warning("Rename base is empty!")
            return []
        # Ép kiểu an toàn
        try:
            start = int(start)
            padding = int(padding)
        except (TypeError, ValueError):
            cmds.warning("Start and padding must be integers.")
            return []

    renamed_objs = []

    for i, obj in enumerate(objs):
        short_name = obj.split('|')[-1]
        new_name = short_name  # Mặc định giữ tên cũ
        if mode == 1:
            # Tránh thêm prefix nếu đã có
            if not short_name.startswith(prefix):
                new_name = f"{prefix}{short_name}"
        elif mode == 2:
            # Tránh thêm suffix nếu đã có
            if not short_name.endswith(suffix):
                new_name = f"{short_name}{suffix}"
        elif mode == 3:
            number = start + i
            new_name = f"{rename_base}{str(number).zfill(padding)}"
        else:
            cmds.warning("Invalid mode!")
            return []
        try:
            renamed = cmds.rename(obj, new_name)
            renamed_objs.append(renamed)
        except RuntimeError as e:
            cmds.warning(f"Failed to rename {obj}: {e}")

    if renamed_objs:
        cmds.select(renamed_objs)
    return renamed_objs



def quick_suffix(suffix=""):
    """
    Nhanh chóng thêm hậu tố vào các đối tượng đang chọn.

    Parameters:
        suffix (str): Hậu tố cần thêm vào tên đối tượng.
    """
    objs = cmds.ls(sl=True, long=True)
    if not objs:
        cmds.warning("No objects selected!")
        return

    for obj in objs:
        short_name = obj.split('|')[-1]
        try:
            cmds.rename(obj, short_name + suffix)
        except RuntimeError as e:
            cmds.warning(f"Failed to rename {obj}: {e}")


def remove_first_char_from_selection():
    """Xoá ký tự đầu tiên của tên các object đang được chọn."""
    for obj in cmds.ls(sl=True, long=True):
        short_name = obj.split('|')[-1]
        if len(short_name) > 1:
            new_name = short_name[1:]
            cmds.rename(obj, new_name)

def remove_last_char_from_selection():
    """Xoá ký tự cuối cùng của tên các object đang được chọn."""
    for obj in cmds.ls(sl=True, long=True):
        short_name = obj.split('|')[-1]
        if len(short_name) > 1:
            new_name = short_name[:-1]
            cmds.rename(obj, new_name)

def hashRename(pattern):
    objs = cmds.ls(sl=True)
    if not objs:
        cmds.warning("No objects selected!")
        return
    if '#' not in pattern:      # Kiểm tra xem pattern có chứa ký tự '#' hay không
        cmds.warning("Cần ít nhất 1 ký tự  '#' ")
        return
    # Đếm số lượng ký tự '#' để xác định padding số
    hash_count = pattern.count('#')
    # Duyệt qua từng đối tượng được chọn, kèm theo chỉ số bắt đầu từ 1
    for i, obj in enumerate(objs, 1):
        number = str(i).zfill(hash_count)   # Tạo số thứ tự, padding bằng 0 cho đủ số lượng '#'
        new_name = pattern.replace('#' * hash_count, number)         # Thay thế đoạn chứa đúng số '#' trong pattern bằng số đã format
        new_name = cmds.rename(obj, new_name)
        print(f"Renamed: {obj} --> {new_name}")
    # Sau khi đổi tên xong, chọn lại các object ban đầu



def search_and_replace(search, replace, mode=1):
    """
    Tìm và thay thế chuỗi trong tên object trong Maya.

    Parameters:
        search (str): Chuỗi cần tìm trong tên object.
        replace (str): Chuỗi dùng để thay thế.
        mode (int):
            1 = Trong hierarchy của object đang chọn (bao gồm cả con)
            2 = Chỉ object được chọn
            3 = Toàn cảnh scene

    Returns:
        list[str]: Danh sách object đã được đổi tên.
    """
    if not search:
        cmds.warning("Search string is empty!")
        return []

    if mode == 1:
        objs = cmds.ls(sl=True, dag=True, long=True)  # toàn bộ hierarchy
    elif mode == 2:
        objs = cmds.ls(sl=True, long=True)            # chỉ các object đang chọn
    else:
        objs = cmds.ls(long=True)                     # tất cả object trong scene
    renamed_objs = []

    for obj in objs:
        short_name = obj.split('|')[-1]
        if search in short_name:
            new_short_name = short_name.replace(search, replace)
            try:
                new_name = cmds.rename(obj, new_short_name)
                renamed_objs.append(new_name)
            except Exception as e:
                cmds.warning(f"Failed to rename {obj}: {e}")

    return renamed_objs