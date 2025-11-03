#Billboard object usually a plane. Make sure selected object is oriented facing forward on Z. Follows persp camera
#Owner: Matt Taylor
_B='aimConstraint'
_A='performPolyNormal 0 -1 0'
import maya.cmds as cmds,maya.mel as mel
def applyConstraint(obj):cmds.aimConstraint('persp',obj,offset=(0,0,0),weight=1,aimVector=(0,0,-1),upVector=(0,1,0),worldUpType='vector',worldUpVector=(0,1,0),skip='none');mel.eval(_A)
def removeConstraint(obj):
	A=cmds.listRelatives(obj,type=_B)or[]
	if A:cmds.delete(A);cmds.setAttr(f"{obj}.rotate",0,0,0);mel.eval(_A)
def billboard():
	A=cmds.ls(sl=1)
	if not A:cmds.warning('Please select an object. Oriented forward on Z with pivot centered');return
	for B in A:
		C=cmds.listRelatives(B,type=_B)or[]
		if C:removeConstraint(B)
		else:applyConstraint(B)
	cmds.select(A)