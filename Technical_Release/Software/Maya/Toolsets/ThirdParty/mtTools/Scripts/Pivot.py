#Assorted Pivot scripts. Select source object and then select your targets. Probably need selection order setting on.
#Owner: Matt Taylor
#Align pivot to selected component
_C=False
_B='performPolyNormal 0 -1 0'
_A=True
import maya.cmds as cmds,maya.mel as mel
def movePiv(origin):
	E='origin_loc';D=origin;B=cmds.ls(sl=_A)
	if len(B)>=1:
		cmds.undoInfo(openChunk=_A)
		for F in B:
			if checkScale(F):cmds.select(F);mel.eval(_B)
		cmds.select(B);cmds.makeIdentity(apply=_A);cmds.makeIdentity(apply=_A,t=1,r=1,s=1,n=0);cmds.spaceLocator(p=(0,0,0),n=E);C=cmds.xform(E,piv=_A,q=_A,ws=_A)
		if D=='Origin':
			for A in B:cmds.xform(A,ws=_A,piv=(C[0],C[1],C[2]))
		elif D=='X':
			for A in B:G=cmds.xform(A,piv=_A,q=_A,ws=_A);cmds.xform(A,ws=_A,piv=(C[0],G[1],G[2]))
		elif D=='Y':
			for A in B:H=cmds.xform(A,piv=_A,q=_A,ws=_A);cmds.xform(A,ws=_A,piv=(H[0],C[1],H[2]))
		elif D=='Z':
			for A in B:I=cmds.xform(A,piv=_A,q=_A,ws=_A);cmds.xform(A,ws=_A,piv=(I[0],I[1],C[2]))
		cmds.delete(E);cmds.select(B);cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Select atleast one object')
def transferPiv():
	A=cmds.ls(sl=1,objectsOnly=_A)
	if not A or len(A)<2:cmds.warning('Select at least two objects.');return
	cmds.undoInfo(openChunk=_A);C=0
	for F in A:
		if C>0:cmds.select(F);movePiv('origin')
		C+=1
	D=A[0];G=checkScale(A[0]);H=cmds.getAttr(f"{D}.worldMatrix");I=cmds.getAttr(f"{D}.worldInverseMatrix");E=0
	for B in A:
		if E>0:
			if checkScale(B)!=G:cmds.select(B);mel.eval(_B)
			cmds.xform(B,worldSpace=_A,matrix=I);cmds.makeIdentity(B,apply=_A,translate=_A,rotate=_A,scale=_A,normal=_C);cmds.xform(B,worldSpace=_A,matrix=H);cmds.select(B);centerPiv()
		E+=1
	cmds.select(A);cmds.undoInfo(closeChunk=_A)
def alignPiv():
	E=cmds.ls(sl=_A);N=cmds.filterExpand(sm=[31,32,34])
	if N:
		cmds.undoInfo(openChunk=_A);A=E[0].split('.')[0];O=cmds.getAttr(f"{A}.scale")[0]
		if any(A<0 for A in O):cmds.select(A);mel.eval(_B);cmds.select(E)
		cmds.delete(A,ch=_A);cmds.makeIdentity(A,a=_A,t=_A,r=_A,s=_A);C=[];W=[];X=_C;C=cmds.polyListComponentConversion(E,tv=_A);cmds.select(C);F=cmds.polyNormalPerVertex(q=_A,xyz=_A);G=[];H=[];I=[];G.extend(F[0::3]);H.extend(F[1::3]);I.extend(F[2::3]);Y=sum(G)/len(G);Z=sum(H)/len(H);a=sum(I)/len(I);D=[]
		for P in C:D.extend(cmds.xform(P,q=_A,worldSpace=_A,t=_A))
		J=[];K=[];L=[];J.extend(D[0::3]);K.extend(D[1::3]);L.extend(D[2::3]);Q=sum(J)/len(J);R=sum(K)/len(K);S=sum(L)/len(L);B=cmds.plane();cmds.move(Q,R,S,B);T=cmds.normalConstraint(C,B,aimVector=(0,0,1),worldUpType=0);b=cmds.xform(B,q=_A,ws=_A,rotatePivot=_A);U=cmds.getAttr(B+'.worldMatrix');V=cmds.getAttr(B+'.worldInverseMatrix');cmds.xform(A,ws=_A,m=V);cmds.makeIdentity(A,a=_A,t=_A,r=_A,s=_A);cmds.xform(A,ws=_A,m=U);M=cmds.objectCenter(B,gl=_A);cmds.xform(A,ws=_A,a=_A,piv=(round(M[0]),round(M[1]),round(M[2])));cmds.delete(T);cmds.delete(B);cmds.select(A);cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Select a component to align the pivot to')
def centerPiv():cmds.xform(cp=_A)
def checkScale(obj):
	A=_C;B=cmds.getAttr(f"{obj}.scale")[0]
	if any(A<0 for A in B):A=_A
	return A