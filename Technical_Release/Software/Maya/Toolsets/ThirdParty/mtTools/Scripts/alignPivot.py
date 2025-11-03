#Align pivot to face
#Owner: Matt Taylor
import maya.cmds as cmds,math,maya.mel as mel
def alignPivot():
	A=True;N=cmds.ls(sl=A);B=N[0].split('.')[0];cmds.delete(B,ch=A);cmds.makeIdentity(B,a=A,t=A,r=A,s=A);D=[];V=[];W=False;X=cmds.filterExpand(sm=31);Y=cmds.filterExpand(sm=32);D=cmds.polyListComponentConversion(N,tv=A);cmds.select(D);F=cmds.polyNormalPerVertex(q=A,xyz=A);G=[];H=[];I=[];G.extend(F[0::3]);H.extend(F[1::3]);I.extend(F[2::3]);Z=sum(G)/len(G);a=sum(H)/len(H);b=sum(I)/len(I);E=[]
	for O in D:E.extend(cmds.xform(O,q=A,worldSpace=A,t=A))
	J=[];K=[];L=[];J.extend(E[0::3]);K.extend(E[1::3]);L.extend(E[2::3]);P=sum(J)/len(J);Q=sum(K)/len(K);R=sum(L)/len(L);C=cmds.plane();cmds.move(P,Q,R,C);S=cmds.normalConstraint(D[0],C,aimVector=(0,0,1),worldUpType=0);c=cmds.xform(C,q=A,ws=A,rotatePivot=A);T=cmds.getAttr(C+'.worldMatrix');U=cmds.getAttr(C+'.worldInverseMatrix');cmds.xform(B,ws=A,m=U);cmds.makeIdentity(B,a=A,t=A,r=A,s=A);cmds.xform(B,ws=A,m=T);M=cmds.objectCenter(C,gl=A);cmds.xform(B,ws=A,a=A,piv=(round(M[0]),round(M[1]),round(M[2])));cmds.delete(S);cmds.delete(C);cmds.select(B)