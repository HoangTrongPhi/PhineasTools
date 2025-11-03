#Create Generic lighting setup
#Owner: Matt Taylor
_A=True
import maya.cmds as cmds
def lightGroup():
	C='double3';F='lightGroup'
	if not cmds.objExists(F):E='persp';H=cmds.getAttr(f"{E}.rotate")[0];cmds.setAttr(f"{E}.rotate",0,0,0,type=C);D=cmds.group(em=_A,name=F);G=cmds.ambientLight(name='ambient_light');cmds.setAttr(f"{G}.intensity",.4);cmds.parent(G,D);B=cmds.directionalLight(name='main_Light');cmds.setAttr(f"{B}.color",.7,.9,1,type=C);cmds.setAttr(f"{B}.shadowColor",0,0,0,type=C);cmds.setAttr(f"{B}.useDepthMapShadows",1);cmds.setAttr(f"{B}.dmapResolution",8192);cmds.rotate(-11,-39,-60,B,absolute=_A);cmds.parent(B,D);A=cmds.directionalLight(name='rim_Light');cmds.setAttr(f"{A}.color",1,.7,.2,type=C);cmds.setAttr(f"{A}.intensity",2);cmds.setAttr(f"{A}.shadowColor",1,1,1,type=C);cmds.setAttr(f"{A}.useDepthMapShadows",1);cmds.setAttr(f"{A}.dmapResolution",8192);cmds.rotate(-143,-4,-60,A,absolute=_A);cmds.parent(A,D);cmds.orientConstraint(E,D,mo=_A);cmds.reorder(D,front=_A);cmds.setAttr(f"{E}.rotate",*H,type=C);setViewportLighting(_A)
	else:cmds.delete(F);setViewportLighting(False)
def setViewportLighting(state=_A):
	B=state;C=cmds.getPanel(vis=_A)
	for A in C:
		if cmds.getPanel(typeOf=A)=='modelPanel':cmds.modelEditor(A,edit=_A,displayLights='all'if B else'default');cmds.modelEditor(A,edit=_A,shadows=B);cmds.modelEditor(A,edit=_A,refresh=_A)