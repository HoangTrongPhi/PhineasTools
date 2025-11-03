#Transfer vert position from one mesh to another. Both meshes must have the same topology, this can be useful if vert order is important.
#Owner: Matt Taylor
#Functions
#########################Main################################
_A=True
import maya.cmds as cmds,maya.mel as mel
from collections import OrderedDict
def mover(vtx1,vtx2):A=cmds.xform(vtx1,q=_A,ws=_A,t=_A);B=cmds.xform(vtx2,ws=_A,t=[A[0],A[1],A[2]])
def collector(vtxs1,vtxs2,obj1Sel):
	mel.eval('select `ls -sl`;PolySelectTraverse 1;select `ls -sl`;');B=cmds.ls(sl=_A,fl=_A)
	for A in B:
		C=A.split('.')[0]
		if C==obj1Sel:vtxs1.append(A)
		else:vtxs2.append(A)
	return len(B)
def doTransfer():
	G='Select just one vert on each mesh (Source then the Target)';H=cmds.ls(sl=_A);D=cmds.ls(cmds.filterExpand(sm=31));I=_A;J=D[0].split('.')[0];A=[];K=D[1].split('.')[0];B=[]
	if len(D)==2:
		C=len(H)
		if C==2:
			F=0
			while I==_A:
				try:
					C=collector(A,B,J)
					if C==F:break
					F=C
				except:break
			A=list(OrderedDict.fromkeys(A));B=list(OrderedDict.fromkeys(B));E=0
			for L in A:mover(A[E],B[E]);E+=1
		else:cmds.warning(G)
	else:cmds.warning(G)