"""
    Chức năng:
    - Kết hợp các mesh được chọn và giữ nguyên pivot, giữ nguyên parent nếu có.
    - Tách các face được chọn thành mesh mới, tự động xóa các face dư thừa.

"""

import maya.cmds as cmds

#--------- clean combine ---------#
def combine_clean():
    '''Kết hợp các mesh được chọn và giữ pivot, giữ nguyên parent nếu có'''
    selection = cmds.ls(sl=True, type='mesh', dag=True)
    if not selection or len(selection) < 2:
        return

    # Lấy transform cha của mesh đầu
    mesh_full = cmds.listRelatives(selection[0], parent=True, fullPath=True)
    mesh_parent = cmds.listRelatives(mesh_full, parent=True, fullPath=True)

    mesh_in_world = []
    if mesh_parent:
        mesh_in_world.append(cmds.parent(mesh_full, world=True)[0])
    else:
        mesh_in_world = mesh_full

    selection[0] = mesh_in_world[0]
    pivots = cmds.xform(mesh_in_world[0], query=True, ws=True, absolute=True, rotatePivot=True)
    new_mesh = cmds.polyUnite(selection, object=True)
    new_mesh_name = cmds.rename(new_mesh[0], mesh_in_world[0])
    cmds.xform(new_mesh_name, rotatePivot=pivots)
    if mesh_parent:
        new_mesh_name = cmds.parent(new_mesh_name, mesh_parent, absolute=True)
    cmds.delete(new_mesh_name, constructionHistory=True)


#--------- clean detach ---------#
def detach_clean():
    '''Tách các face được chọn thành mesh mới, tự động xóa các face dư thừa'''
    faces = get_all_selection()
    if not faces or len(faces) == 0:
        return
    temp = faces[0].split('.')
    if len(temp) == 1 or len(faces) == cmds.polyEvaluate(faces[0].split('.')[0], face=True):
        return
    mesh = temp[0]
    temp = cmds.duplicate(mesh, name=mesh, returnRootsOnly=True)
    new_mesh = temp[0]
    new_faces = cmds.ls(f"{new_mesh}.f[*]", flatten=True)
    cnt = len(new_faces)
    new_face_delete = []

    for ii, face in enumerate(new_faces):
        if face.replace(new_mesh, mesh) not in faces:
            new_face_delete.append(face)

    if new_face_delete:
        cmds.delete(new_face_delete)
    cmds.delete(faces)
    cmds.select(new_mesh)
    cmds.xform(centerPivots=True)


