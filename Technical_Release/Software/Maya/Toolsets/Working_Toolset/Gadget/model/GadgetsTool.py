"""
3/11/2024
Create by HOANG TRONG PHI   @HuangFei
Done ,testing Maya 2022 -> 2024
"""

import maya.cmds as cmds, maya.mel as mel
import sys
import os
import importlib
def getDirectoryofModule(modulename):

    #Input: module as string
    #OUtput:
        #List: name as string and directory of module

    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = CommonPyFunction.Get_WD(module.__file__)
    return currWD
    pass

