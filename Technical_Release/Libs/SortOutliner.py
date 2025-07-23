"""
    6/11/2024
    Edit by HOANG TRONG PHI   @HuangFei
"""

import maya.cmds as cmds, maya.mel as mel

#Định nghĩa một hàm nhận vào inGroup_fullPath, tức là đường dẫn đầy đủ (full path) tới một group (ví dụ: |group1|group2|MyGroup)
def sortChildrenOfAGroupByABC(inGroup_fullPath):
    tempGroupName = '|TempGrpSortOutliner'
    if not cmds.objExists(tempGroupName):
        cmds.group(empty=True, name=tempGroupName)

    #Lấy danh sách các con trực tiếp trong inGroup_fullPath
    #cmds.listRelatives(..., children=True) trả về danh sách tên các đối tượng con
    #Dùng sorted() để sắp xếp danh sách theo thứ tự alphabet.
    #Nếu không có con nào (None), dùng or [] để tránh lỗi.

    childrenGroups = sorted(cmds.listRelatives(inGroup_fullPath, children=True) or [])
    for grp in childrenGroups:
        cmds.parent(inGroup_fullPath + '|' + grp, tempGroupName, relative=True)
        cmds.parent(tempGroupName + '|' + grp, inGroup_fullPath, relative=True)

    # Xóa nhóm tạm sau khi đã hoàn thành việc sắp xếp
    cmds.delete(tempGroupName)


#Hàm dùng để thao tác từ selection của người dùng trong Maya.
def sortSelectedGroupByAlphabet():
    # Lấy danh sách đang được chọn, bao gồm cả transforms(thông tin vị trí của object đó)
    grpToSort = cmds.ls(sl=True, l=True, transforms=True)

    #Kiểm tra nếu chỉ chọn duy nhất một group.
    if len(grpToSort) == 1:
        #Gọi hàm sắp xếp với group được chọn
        sortChildrenOfAGroupByABC(grpToSort[0])
        # Sau đó chọn lại group ban đầu (giữ nguyên selection sau thao tác)
        cmds.select(grpToSort)
    else:
        cmds.confirmDialog(message='Chỉ được chọn 1 group')
