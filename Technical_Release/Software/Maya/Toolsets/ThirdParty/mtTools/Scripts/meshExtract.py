#Didn't like maya's extract so I made a new one
#Owner: Matt Taylor
_B='Select some faces to extract'
_A=True
import maya.cmds as cmds,maya.mel as mel
def extract():
	C=cmds.filterExpand(sm=34)
	if not C:cmds.warning(_B);return
	cmds.undoInfo(openChunk=_A);D=[];E={}
	for F in C:H=F.split('.')[0];E.setdefault(H,[]).append(F)
	for(A,G)in E.items():I=cmds.ls(f"{A}.f[:]",fl=_A);J=list(set(I)-set(G));B=cmds.duplicate(A,rr=_A)[0];K=[C.replace(A,B)for C in J];cmds.delete(B,ch=_A);cmds.select(K,r=_A);cmds.delete();cmds.select(G,r=_A);cmds.delete();D.append(B)
	cmds.select(D,r=_A);centerPiv();cmds.undoInfo(closeChunk=_A)
def dupExtract():
	C=cmds.filterExpand(sm=34)
	if not C:cmds.warning(_B);return
	cmds.undoInfo(openChunk=_A);D={}
	for E in C:A=E.split('.')[0];D.setdefault(A,[]).append(E)
	F=[]
	for(A,H)in D.items():
		I=cmds.ls(f"{A}.f[:]",fl=_A);J=list(set(I)-set(H));B=cmds.duplicate(A,name=f"{A}_extracted")[0];G=[C.replace(A,B)for C in J];cmds.delete(B,ch=_A)
		if G:cmds.delete(G)
		cmds.xform(B,centerPivots=_A);F.append(B)
	cmds.select(F,r=_A);cmds.undoInfo(closeChunk=_A)
def combine():mel.eval('polyPerformAction polyUnite o 0')
def centerPiv():cmds.xform(cp=_A)
def mirrorInstance(origin,x,y,z):
	B=cmds.ls(sl=1,long=_A,transforms=_A)
	if not B:cmds.warning('Select an object to make an instance of');return
	else:
		cmds.undoInfo(openChunk=_A)
		if origin:
			for C in B:
				D=checkScale(C);cmds.makeIdentity(C,a=_A,t=_A,r=_A,s=_A);A=cmds.instance(C);cmds.xform(A,ws=_A,piv=(0,0,0));cmds.scale(x,y,z,A,relative=_A)
				if D:cmds.polyNormal(A,normalMode=0,userNormalMode=0,ch=False)
		else:A=cmds.instance();cmds.scale(x,y,z,A,relative=_A)
		cmds.select(B);cmds.undoInfo(closeChunk=_A)
def rotateInstance(numberOfInstances,origin,axis):
	F=numberOfInstances;B=axis;E=cmds.ls(sl=1,long=_A,transforms=_A)
	if not E:cmds.warning('Select one object to create radial instances of');return
	else:
		cmds.undoInfo(openChunk=_A);H=36e1/F;cmds.refresh(force=_A);G=cmds.xform(E[0],query=_A,worldSpace=_A,rotatePivot=_A);I=cmds.xform(E[0],query=_A,worldSpace=_A,translation=_A);J=[I[A]-G[A]for A in range(3)];K=[]
		for L in range(1,F):
			cmds.select(E[0]);A=mel.eval('instance;')[0];K.append(A);C=L*H
			if origin:
				D=cmds.group(empty=_A,world=_A);cmds.xform(D,worldSpace=_A,translation=(0,0,0));cmds.parent(A,D)
				if B==0:cmds.rotate(C,0,0,D,relative=_A,worldSpace=_A)
				elif B==1:cmds.rotate(0,C,0,D,relative=_A,worldSpace=_A)
				elif B==2:cmds.rotate(0,0,C,D,relative=_A,worldSpace=_A)
				cmds.parent(A,world=_A);cmds.delete(D)
			else:
				cmds.xform(A,worldSpace=_A,translation=G)
				if B==0:cmds.rotate(C,0,0,A,relative=_A,objectSpace=_A)
				elif B==1:cmds.rotate(0,C,0,A,relative=_A,objectSpace=_A)
				elif B==2:cmds.rotate(0,0,C,A,relative=_A,objectSpace=_A)
				M=cmds.xform(A,query=_A,worldSpace=_A,translation=_A);N=[M[A]+J[A]for A in range(3)];cmds.xform(A,worldSpace=_A,translation=N)
		cmds.select(E);cmds.undoInfo(closeChunk=_A)
def checkScale(obj):
	A=False;B=cmds.getAttr(f"{obj}.scale")[0]
	if any(A<0 for A in B):A=_A
	return A