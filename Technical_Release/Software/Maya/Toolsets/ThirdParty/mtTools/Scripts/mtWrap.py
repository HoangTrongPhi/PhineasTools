#Unwrap object along UVs. Create a blend shape. Attach things to it and wrap it back
#Owner: Matt Taylor
_B='mtWeight'
_A=True
import maya.cmds as cmds,maya.mel as mel
def mtUnwrap():
	F='SelectAll';E='dR_DoCmd("convertSelectionToUV")';C=cmds.ls(sl=1)
	def A():
		A=[];cmds.select(C[0]);mel.eval(E);mel.eval(F);mel.eval('polySelectBorderShell 1;');B=cmds.polyListComponentConversion(internal=_A,te=_A);B=cmds.ls(B,fl=_A)
		for G in B:
			D=cmds.polyListComponentConversion(G,tuv=_A);D=cmds.ls(D,fl=_A)
			if len(D)>2:A.append(G)
		if len(A)==0:H=cmds.polyListComponentConversion(B,fe=_A,tf=_A);A=cmds.polyListComponentConversion(H,te=_A,border=_A)
		cmds.select(A)
	def B():B=C[0].split('.')[0];A=cmds.duplicate(B);cmds.select(A);mel.eval('SelectEdgeMask;');cmds.polySplitVertex();return A
	def D(obj):
		A=obj;cmds.select(A);B=cmds.duplicate(A);mel.eval(E);mel.eval(F);C=cmds.polyListComponentConversion(tuv=_A);C=cmds.ls(C,fl=_A)
		for G in C:H=cmds.polyEditUV(G,q=_A,u=_A,v=_A);D=cmds.polyListComponentConversion(G,toVertex=_A);D=cmds.ls(D,fl=_A);cmds.move(H[0]*100,H[1]*100,D,a=_A,ws=_A)
		J=cmds.listRelatives(A,f=_A,s=_A,ni=_A);I=cmds.listRelatives(B,f=_A,s=_A,ni=_A);cmds.select(A);K=cmds.blendShape(A,I,n='mtWrap')[0];cmds.delete(A);B=cmds.rename(B,'mtWrap_Final');cmds.select(B);cmds.aliasAttr(_B,'mtWrap.envelope');cmds.setAttr('mtWrap.mtWeight',0);cmds.aliasAttr('mtShape','mtWrap.w[0]');cmds.setAttr('mtWrap.mtShape',1.)
	if not C:cmds.warning('Select an object to unwrap. Must have UVs')
	else:cmds.undoInfo(openChunk=_A);A();G=B();D(G);cmds.undoInfo(closeChunk=_A)
def mtWrap():
	A=cmds.ls(sl=1)
	if len(A)<=1:cmds.warning('Select a target and source object.')
	else:mel.eval('CreateWrap;')
def mtWrapToggle():
	B=cmds.ls(sl=1,long=False)
	if not B:print('No object selected.');return
	E=B[0];F=cmds.listHistory(E)or[]
	for C in F:
		if cmds.attributeQuery(_B,node=C,exists=_A):A=f"{C}.mtWeight";D=1-cmds.getAttr(A);cmds.setAttr(A,D);print(f"Toggled {A} to {D}");return