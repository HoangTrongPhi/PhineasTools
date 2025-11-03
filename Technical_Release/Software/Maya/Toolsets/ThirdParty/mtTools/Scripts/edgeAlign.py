#Select edges in a line, this will straighten them out.
#Owner: Matt Taylor
_A='Select some edges to align'
import maya.cmds as cmds,maya.mel as mel
def edgeAlign():
	A=True;D=cmds.filterExpand(sm=32)
	if not D:cmds.warning(_A)
	else:
		cmds.undoInfo(openChunk=A);K=D[0].split('.')[0];G=cmds.ls(cmds.polyListComponentConversion(D,fe=A,tv=A),fl=A);H=[];N=[]
		for L in D:H.extend(cmds.ls(cmds.polyListComponentConversion(L,fe=A,tv=A),fl=A))
		E=[];I=0
		for M in G:
			if H.count(M)==1:E.append(G[I])
			I+=1
		F=cmds.polyPlane(n='helperPlane__',sx=2,sy=1);J=str(F[0].split('.')[0]);cmds.select(J+'.vtx[4]',J+'.vtx[1]');cmds.select(E[0],E[1],add=A);mel.eval('Snap2PointsTo2Points;');B=cmds.xform(F,q=A,ro=A,ws=A);C=cmds.xform(E[0],q=A,t=A,ws=A,a=A);cmds.delete(F);cmds.select(D);cmds.setToolTo('Scale');cmds.manipPivot(p=(C[0],C[1],C[2]),o=(B[0],B[1],B[2]));cmds.scale(0,0,1,r=A,p=(C[0],C[1],C[2]),oa=(B[0],B[1],B[2]));cmds.select(K);mel.eval('SelectEdgeMask;');cmds.undoInfo(closeChunk=A)
def edgeFlow():
	A=cmds.filterExpand(sm=32)
	if not A:cmds.warning(_A)
	elif A:cmds.polyEditEdgeFlow(A,adjustEdgeFlow=1.)
	else:0