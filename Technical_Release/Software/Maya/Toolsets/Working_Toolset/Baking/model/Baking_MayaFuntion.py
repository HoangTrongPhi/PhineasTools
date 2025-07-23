"""
    Created by Hoang Trong Phi - @HuangFei
    Update 8:54 PM - 3/11/2024
    Update 11:58 PM - 16/6/2025

    -Tự động gán màu, đặt tên, chia group rõ ràng
    -Chạy an toàn trên Maya 2024, 2025, 2026.

"""
import os

import maya.mel as mel
import maya.cmds as cmds
import random
import json

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Libs.SortOutliner as SortOutliner
importlib.reload(SortOutliner)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

import Libs.setupMesh as setupMesh
importlib.reload(setupMesh)


BakeSet_Info = "C:/tempMaya/BakeSet_Info/"
#####----------#######

# setup Mesh trước khi tạo BakeSet
def setupMesh():
    return 1
####-------------######



def sortLowHigh(list):
    """
    input: list of 2 mesh
    output: list with:
            lowpoly in index 0
            highpoly in index 1
    """
    sortedList = []
    mesh1 = list[0]
    mesh2 = list[1]
    trisCount1 = cmds.polyEvaluate(mesh1, triangle=True)
    trisCount2 = cmds.polyEvaluate(mesh2, triangle=True)
    if trisCount1 < trisCount2:
        sortedList.append(mesh1)
        sortedList.append(mesh2)
    else:
        sortedList.append(mesh2)
        sortedList.append(mesh1)
    return sortedList

###################################################################
#                   CREATE BAKE SET
###################################################################

# ------------------------- HÀM PHỤ -------------------------

def unparentToWorld(obj):
    try:
        return cmds.parent(obj, world=True)
    except RuntimeError as e:
        print("Unparent failed:", e)
        return obj

def renameBakeset(lowParented, highParented, prefixBakeset):
    meshLowList = cmds.listRelatives('|Low', children=True, fullPath=True) or []
    name = '{}_temp'.format(prefixBakeset)

    for i in range(1, len(meshLowList) + 1):
        name = '{}_{:02d}'.format(prefixBakeset, i)
        tempCheck = '|Low|{}_Low'.format(name)
        if '|Low|{}'.format(lowParented[0]) != tempCheck:
            if tempCheck in meshLowList:
                continue
            else:
                break
        else:
            break

    meshLow = cmds.rename(lowParented, name)
    meshHigh = cmds.rename(highParented, meshLow)
    newMeshLow = cmds.rename('|Low|{}'.format(meshLow), '{}_Low'.format(meshLow))
    newMeshHigh = cmds.rename('|High|{}'.format(meshLow), '{}_High'.format(meshLow))
    return newMeshLow, newMeshHigh

def assignRandomColor(obj, color, isHigh=False):
    offset = -0.2 if isHigh else 0
    r = max(0, min(1, color[0] + offset))
    g = max(0, min(1, color[1] + offset))
    b = max(0, min(1, color[2] + offset))

    cmds.setAttr('{}.useOutlinerColor'.format(obj), True)
    cmds.setAttr('{}.outlinerColor'.format(obj), r, g, b)
    cmds.setAttr('{}.overrideEnabled'.format(obj), True)
    cmds.setAttr('{}.overrideRGBColors'.format(obj), True)
    cmds.setAttr('{}.overrideColorR'.format(obj), r)
    cmds.setAttr('{}.overrideColorG'.format(obj), g)
    cmds.setAttr('{}.overrideColorB'.format(obj), b)

def ensureDisplayLayer(name, obj):
    if not cmds.objExists(name):
        cmds.select(obj)
        cmds.createDisplayLayer(noRecurse=True, name=name)
    else:
        cmds.editDisplayLayerMembers(name, obj, noRecurse=True)

# ------------------------- HÀM CHÍNH -------------------------
# unparentToWorld(obj)
def unparentToWorld(obj):
    if cmds.listRelatives(obj, parent=True): # Nếu object có parent
        try:
            result = cmds.parent(obj, world=True) # Gỡ khỏi parent, đưa lên world
            return result[0] if result else obj
        except RuntimeError as e:
            print("Unparent failed:", e)
    return obj


# parentSafe(child, parent)
def parentSafe(child, parent):
    if not cmds.objExists(child) or not cmds.objExists(parent):
        return child
    try:
        result = cmds.parent(child, parent)     # Parent vào group mới
        return result[0] if result else child
    except RuntimeError as e:
        print("Parent failed:", e)
        return child

# Lấy danh sách con trong group |Low, và đặt tên tạm cho bakeset.
def renameBakeset(lowObj, highObj, prefixBakeset):
    meshLowList = cmds.listRelatives('|Low', children=True, fullPath=True) or []
    name = '{}_temp'.format(prefixBakeset)

    #Vòng lặp tìm index tên bakeset chưa trùng để đặt tên mới, tránh đụng hàng.
    for i in range(1, len(meshLowList) + 1):
        name = '{}_{:02d}'.format(prefixBakeset, i)
        tempCheck = '|Low|{}_Low'.format(name)
        if '|Low|{}'.format(lowObj) != tempCheck:
            if tempCheck in meshLowList:
                continue
            else:
                break
        else:
            break

    #Rename lần lượt low, high với hậu tố _Low và _High, gắn đúng group.
    meshLow = cmds.rename(lowObj, name)
    meshHigh = cmds.rename(highObj, meshLow)
    newMeshLow = cmds.rename('|Low|{}'.format(meshLow), '{}_Low'.format(meshLow))
    newMeshHigh = cmds.rename('|High|{}'.format(meshLow), '{}_High'.format(meshLow))
    return newMeshLow, newMeshHigh

#Tính toán màu RGB với độ lệch nếu là mesh high.
def assignRandomColor(obj, color, isHigh=False):
    offset = -0.2 if isHigh else 0
    r = max(0, min(1, color[0] + offset))
    g = max(0, min(1, color[1] + offset))
    b = max(0, min(1, color[2] + offset))

    #Đặt màu hiển thị trong Outliner và Viewport override màu RGB
    cmds.setAttr('{}.useOutlinerColor'.format(obj), True)
    cmds.setAttr('{}.outlinerColor'.format(obj), r, g, b)
    cmds.setAttr('{}.overrideEnabled'.format(obj), True)
    cmds.setAttr('{}.overrideRGBColors'.format(obj), True)
    cmds.setAttr('{}.overrideColorR'.format(obj), r)
    cmds.setAttr('{}.overrideColorG'.format(obj), g)
    cmds.setAttr('{}.overrideColorB'.format(obj), b)

#Đảm bảo Display Layer tồn tại, nếu chưa thì tạo mới, nếu có thì thêm object vào.
def ensureDisplayLayer(name, obj):
    if not cmds.objExists(name):
        cmds.select(obj)
        cmds.createDisplayLayer(noRecurse=True, name=name)
    else:
        cmds.editDisplayLayerMembers(name, obj, noRecurse=True)

#Lấy danh sách object đang được chọn.
def createBakeset(prefixBakeset='BakeSet'):
    currSel = cmds.ls(selection=True, long=True)

    #Kiểm tra chỉ được chọn đúng 2 object (low & high), nếu không thì hiện dialog cảnh báo.
    if len(currSel) != 2:
        mess = f'Chọn cặp mesh Low/ High để tạo BakeSet ! Bạn đang chọn {len(currSel)} mesh(es)'
        cmds.confirmDialog(message=mess)
        return 0

    #Hàm sortLowHigh() dùng để phân biệt đâu là low, đâu là high mesh.
    sortedList = sortLowHigh(currSel)

    #Tạo group Low và High nếu chưa tồn tại.
    if not cmds.objExists('|Low'):
        cmds.group(empty=True, name='Low')
    if not cmds.objExists('|High'):
        cmds.group(empty=True, name='High')

    # Đảm bảo 2 mesh được đưa ra khỏi các group hiện tại về world.
    sortedList[0] = unparentToWorld(sortedList[0])
    sortedList[1] = unparentToWorld(sortedList[1])

    # Gắn lại object vào group |Low và |High.
    lowObj = parentSafe(sortedList[0], '|Low')
    highObj = parentSafe(sortedList[1], '|High')

    # Chọn cả 2 object để gọi hàm setupMesh() (giả định đã định nghĩa trước để chuẩn hóa mesh).
    cmds.select(lowObj, highObj)
    setupMesh()

    # Tự động rename low/high mesh đúng chuẩn theo tên prefix và đánh số.
    newMeshLow, newMeshHigh = renameBakeset(lowObj, highObj, prefixBakeset)

    # Tắt hiển thị hai mesh sau khi setup bakeset.
    cmds.setAttr(f'{newMeshLow}.visibility', False)
    cmds.setAttr(f'{newMeshHigh}.visibility', False)

    # Gán màu ngẫu nhiên cho Low và High, màu High sẽ tối hơn.
    color = [random.uniform(0.5, 1) for _ in range(3)]
    assignRandomColor(newMeshLow, color, isHigh=False)
    assignRandomColor(newMeshHigh, color, isHigh=True)

    # Gán Low/High group vào display layer chung, và từng bakeset riêng vào layer riêng.
    ensureDisplayLayer('Low_layer', '|Low')
    ensureDisplayLayer('High_layer', '|High')
    ensureDisplayLayer(f'{prefixBakeset}_L', newMeshLow)
    ensureDisplayLayer(f'{prefixBakeset}_H', newMeshHigh)

    # Nếu tool có hỗ trợ SortOutliner, thì sắp xếp con theo thứ tự ABC trong Outliner cho đẹp.
    if hasattr(SortOutliner, 'sortSelectedGroupByAlphabet'):
        cmds.select('|Low')
        SortOutliner.sortSelectedGroupByAlphabet()
        cmds.select('|High')
        SortOutliner.sortSelectedGroupByAlphabet()


    ## In BakeSet ra thành File JSON để kiểm tra
    if not os.path.exists(BakeSet_Info):
        os.makedirs(BakeSet_Info)

    # Xóa toàn bộ file .json cũ trong thư mục BakeSet_Info
    for file in os.listdir(BakeSet_Info):
        if file.endswith(".json"):
            os.remove(os.path.join(BakeSet_Info, file))

    # Ghi file JSON mới
    bake_info = {
        "bakeset_name": prefixBakeset,
        "mesh_low": newMeshLow,
        "mesh_high": newMeshHigh,
        "color_low": color,
        "color_high": [max(0, min(1, c - 0.2)) for c in color]
    }

    json_path = os.path.join(BakeSet_Info, f"{prefixBakeset}.json")
    with open(json_path, 'w') as f:
        json.dump(bake_info, f, indent=4)

    cmds.select(clear=True)
    return 1


###################################################################
#                  ******************
###################################################################

def toggleGroup(group='|High'):
    """
    Toggle visibility of direct children under a group node in Maya.
    Args:
        group (str): Full path to the group node.
    Returns:
        list: List of children processed.
    """
    meshList = []
    if cmds.objExists(group):
        children = cmds.listRelatives(group, children=True, fullPath=True) or []
        for child in children:
            if cmds.attributeQuery('visibility', node=child, exists=True):
                current = cmds.getAttr(f'{child}.visibility')
                cmds.setAttr(f'{child}.visibility', not current)
                meshList.append(child)
    else:
        cmds.warning(f"Thiếu group {group}! Không thể Show/Hide.")
    return meshList


def toggleAll(status=True):
    groupList = ['|High', '|Low']
    for grp in groupList:
        if cmds.objExists(grp):
            meshList = cmds.listRelatives(grp, children=True) or []
            for mesh in meshList:
                cmds.setAttr(('{}.visibility').format(mesh), status)
                showHighLowLayer(status)

        else:
            mel.eval(('warning "Thieu group {}! Khong the Show/Hide"').format(grp))
    pass

def showHighLowLayer(status):
    if cmds.objExists('Low_layer') and cmds.objExists('High_layer'):
        cmds.setAttr('Low_layer.visibility', status)
        cmds.setAttr('High_layer.visibility', status)


def swapHighLow(status=True):
    groupList = ['|High', '|Low']
    for index, grp in enumerate(groupList):
        if cmds.objExists(grp):
            if index == 0:
                meshList = cmds.listRelatives(grp, children=True) or []
                for mesh in meshList:
                    cmds.setAttr(('{}.visibility').format(mesh), status)

            else:
                meshList = cmds.listRelatives(grp, children=True) or []
                for mesh in meshList:
                    cmds.setAttr(('{}.visibility').format(mesh), not status)

        else:
            mel.eval(('warning "Thieu group {}! Khong the Swap"').format(grp))

    return 1


def explode(number = 10):
    groupList = ['|High', '|Low']
    if cmds.objExists(groupList[0]):
        meshHighList = cmds.listRelatives(groupList[0], children=True) or []
        meshLowList = cmds.listRelatives(groupList[1], children=True) or []
        i = 0
        while i < len(meshHighList):
            numX = random.uniform(-number, number)
            numY = random.uniform(-number, number)
            numZ = random.uniform(-number, number)
            try:
                cmds.setAttr(('|High|{}.translateX').format(meshHighList[i]), numX)
                cmds.setAttr(('|High|{}.translateY').format(meshHighList[i]), numY)
                cmds.setAttr(('|High|{}.translateZ').format(meshHighList[i]), numZ)
                cmds.setAttr(('|Low|{}.translateX').format(meshLowList[i]), numX)
                cmds.setAttr(('|Low|{}.translateY').format(meshLowList[i]), numY)
                cmds.setAttr(('|Low|{}.translateZ').format(meshLowList[i]), numZ)
            except RuntimeError:
                print (RuntimeError)

            i = i + 1
    else:
        mel.eval(('warning "Thieu group {}! Khong the Explode"').format(groupList[0]))
    return 1


def resetExplode():
    groupList = [
     '|High', '|Low']
    if cmds.objExists('|High') and cmds.objExists('|Low'):
        for grp in groupList:
            meshList = cmds.listRelatives(grp, children=True) or []
            for mesh in meshList:
                cmds.setAttr(('{}.translateX').format(mesh), 0)
                cmds.setAttr(('{}.translateY').format(mesh), 0)
                cmds.setAttr(('{}.translateZ').format(mesh), 0)
    return 1

#---------- Select-------------
def selectHigh():
    if cmds.objExists('|High'):
        cmds.select('|High')
    return 1


def selectLow():
    if cmds.objExists('|Low'):
        cmds.select('|Low')
    return 1


def selectPair():
    currSel = cmds.ls(selection=True)
    if cmds.objExists('|High') and cmds.objExists('|Low'):
        selectMeshList = []
        for mesh in currSel:
            selectMesh = mesh
            if 'Low' in mesh:
                selectMesh = mesh.replace('Low', 'High')
            if 'High' in mesh:
                selectMesh = mesh.replace('High', 'Low')
            selectMeshList.append(selectMesh)

        cmds.select(selectMeshList, add=True)
    return 1


def select_bakeset_by_index(index=0):
    """
    Chọn mesh tại vị trí 'index' trong các group |High và |Low theo thứ tự alphabet.

    Parameters:
        index (int): Vị trí của mesh cần chọn (default = 0).

    Returns:
        list: Danh sách mesh đã được chọn từ mỗi group.
    """
    selected_meshes = []
    group_list = ['|High', '|Low']

    for group in group_list:
        if not cmds.objExists(group):
            continue

        # Sắp xếp con trong group theo alphabet
        cmds.select(group, replace=True)
        SortOutliner.sortSelectedGroupByAlphabet()

        # Lấy danh sách con của group
        mesh_list = cmds.listRelatives(group, children=True, fullPath=True) or []

        if 0 <= index < len(mesh_list):
            mesh = mesh_list[index]
            selected_meshes.append(mesh)

    if selected_meshes:
        cmds.select(selected_meshes, replace=True)

    return selected_meshes


