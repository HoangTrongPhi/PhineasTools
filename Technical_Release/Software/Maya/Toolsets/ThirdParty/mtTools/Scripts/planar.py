# Planar
# Owner: Matt Taylor
_A=True
import maya.cmds as cmds
def planar():
	cmds.undoInfo(openChunk=_A);B=cmds.ls(sl=1)
	if not B:cmds.warning('Select some components to planar');return
	A=cmds.ls(cmds.polyListComponentConversion(B,tv=_A),fl=_A);J=A[0].split('.')[0];D=Vtx3DtoList(A);E=fitPlaneCovariance(A);G=average(D)
	for(H,F)in enumerate(D):I=dotProduct(subtract(F,G),E);C=subtract(F,scaleVector(E,I));cmds.move(C[0],C[1],C[2],A[H],absolute=_A)
	cmds.select(B);cmds.undoInfo(closeChunk=_A)
def Vtx3DtoList(S):return[cmds.xform(A,q=_A,ws=_A,t=_A)for A in S]
def fitPlaneCovariance(verts):
	C=.0;D=Vtx3DtoList(verts);E=average(D);F=[[C,C,C]for A in range(3)]
	for G in D:
		for A in range(3):
			for B in range(3):F[A][B]+=(G[A]-E[A])*(G[B]-E[B])
	return smallestEigenvector(F)
def smallestEigenvector(matrix):import numpy as A;B=A.array(matrix);C,D=A.linalg.eig(B);E=A.argmin(C);return D[:,E].tolist()
def normalizeVector(v):A=sum(A**2 for A in v)**.5;return[B/A for B in v]if A>0 else v
def average(M):A=len(M);return[sum(A[B]for A in M)/A for B in range(3)]
def subtract(a,b):return[a[A]-b[A]for A in range(3)]
def scaleVector(v,s):return[v[A]*s for A in range(3)]
def dotProduct(a,b):return sum(a[A]*b[A]for A in range(3))