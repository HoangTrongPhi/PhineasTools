
_B=False
_A=True
import maya.OpenMaya as om,maya.OpenMayaUI as omui,maya.cmds as cmds
mySel=[]
ctx='myCtx'
processRunning=_B
def Start():
	global mySel,ctx;ctx='myCtx';mySel=cmds.ls(sl=_A)
	if not mySel:cmds.error('Select an object to raycast');return
	else:cmds.warning('Click on a mesh to snap the selected object')
	if cmds.draggerContext(ctx,exists=_A):cmds.deleteUI(ctx)
	cmds.draggerContext(ctx,pressCommand=rayCastObject,name=ctx,cursor='crossHair');cmds.setToolTo(ctx)
def rayCastObject():
	A=None;global processRunning
	if processRunning:return
	processRunning=_A;resetObject();I,J,P=cmds.draggerContext(ctx,query=_A,anchorPoint=_A);C=om.MPoint();dir=om.MVector();D=om.MFloatPoint();F=om.MScriptUtil().asIntPtr();omui.M3dView().active3dView().viewToWorld(int(I),int(J),C,dir);K=om.MFloatPoint(C.x,C.y,C.z)
	for E in cmds.ls(type='mesh'):
		if E==mySel[0]:continue
		G=om.MSelectionList();G.add(E);H=om.MDagPath();G.getDagPath(0,H);L=om.MFnMesh(H);M=L.closestIntersection(K,om.MFloatVector(dir),A,A,_B,om.MSpace.kWorld,99999,_B,A,D,A,F,A,A,A)
		if M:N=om.MScriptUtil(F).asInt();O=f"{E}.f[{N}]";B=cmds.polyPlane()[0];cmds.rotate(-90,0,0,B,absolute=_A);cmds.parent(mySel[0],B);cmds.move(D.x,D.y,D.z,B);cmds.normalConstraint(O,B,aimVector=(0,0,1),worldUpType=0);cmds.move(0,0,0,mySel[0],relative=_A);cmds.parent(mySel[0],w=_A);cmds.delete(B);cmds.select(mySel[0]);break
	processRunning=_B
def resetObject():
	if cmds.listRelatives(mySel[0],parent=_A):cmds.parent(mySel[0],w=_A)
	cmds.move(0,0,0,mySel[0],absolute=_A);cmds.rotate(0,0,0)