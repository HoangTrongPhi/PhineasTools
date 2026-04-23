# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (Optimized)
    22/4/2026
    Maya 2026+ (Python 3)
"""
import maya.cmds as cmds

name = 'Have Namespace'
check = 1
fixAble = 1

def run(nodes, selectionMesh):
    """
    Check khoảng trống trong namespace
    """
    print(f'Running {__name__}')
    namespaces = []
    for node in nodes:
        mesh = node
        if cmds.objectType(node) != 'transform':
            parents = cmds.listRelatives(node, parent=True, fullPath=True)
            if parents:
                mesh = parents[0]
        if ':' in mesh:
            namespaces.append(mesh)

    return namespaces


def fix(*arg):
    print('Fixing...')
    renamed_nodes = []
    cmds.namespace(set=':')
    nodes = cmds.ls(selection=True, long=True, flatten=True)
    dep_nodes = cmds.ls(nodes, dependencyNodes=True, flatten=True)
    namespace_remove_list = []
    for node in dep_nodes:
        if cmds.objExists(node):
            if ':' in node:
                new_name = node.split(':')[1]
                namespace = node.split(':')[0]
                namespace_remove_list.append(namespace)
                try:
                    cmds.lockNode(node, lock=False)
                    cmds.rename(node, new_name)
                    renamed_nodes.append(node)
                except RuntimeError as e:
                    print(f"Error renaming {node}: {e}")

    namespace_remove_list = list(set(namespace_remove_list))
    for name in namespace_remove_list:
        try:
            cmds.namespace(removeNamespace=name, deleteNamespaceContent=True)
        except Exception as e:
            print(f"Error removing namespace {name}: {e}")

    return renamed_nodes


def doc(*arg):
    mess = 'Namespace: Ten mesh co them namespace\nCo the dung Cleanup Tool\n\n Please fix!'
    return mess


def report(*arg):
    return 1
