#Edge border select
#In Maya 2018, Autodesk changed how edge loop selection works. The old one is better so this is an attempt to recreate that. It's better as a hotkey.
#By Matt Taylor
#Functions
#Add Collected Edges if they are valid border edges
#########################Main################################
_C='deadEnd'
_B=False
_A=True
import maya.cmds as cmds,maya.mel as mel
def vtxCheck(vtx):
	A=_A;C=cmds.ls(cmds.polyListComponentConversion(vtx,fv=_A,te=_A),fl=_A);B=faceCheck(vtx)
	if len(C)==3 and B==_B:A=_B
	elif B==_B:A=_B
	return A
def faceCheck(vtx):
	B=cmds.ls(cmds.polyListComponentConversion(vtx,fv=_A,tf=_A),fl=_A);A=_A
	if len(B)==1:A=_B
	return A
def edgeCheck(edge):
	D=cmds.ls(cmds.polyListComponentConversion(edge,fe=_A,tv=_A),fl=_A);A=vtxCheck(D[0]);B=vtxCheck(D[1])
	if A==_A and B==_A:C='Both'
	elif A==_B and B==_A:C='V2'
	elif A==_A and B==_B:C='V1'
	elif A==_B and B==_B:C=_C
	return C
def addEdges(edges,sourceEdge,edgeSearch,edgeFinal,edgeTotal):
	F=edgeTotal;E=edgeFinal;D=edges;B=edgeSearch;A=sourceEdge;D[:]=[B for B in D if B!=A];E.append(A);F.remove(A);B.remove(A);G=[]
	for C in D:
		if C in F:
			if C not in B:
				if C not in E:B.append(C)
	return B,E,F
def edgeSelect():
	I=cmds.ls(sl=1);H=cmds.ls(cmds.filterExpand(sm=32));A=H;B=[];C=[];J=0;G=_A
	if not H:cmds.warning('Select an edge');return
	mel.eval('SelectEdgeLoop');C=cmds.ls(sl=_A,fl=_A)
	while G==_A:
		try:
			E=edgeCheck(A[0]);F=cmds.ls(cmds.polyListComponentConversion(A[0],fe=_A,tv=_A),fl=_A)
			if E is'Both':D=cmds.ls(cmds.polyListComponentConversion(F[0],F[1],fv=_A,te=_A),fl=_A);A,B,C=addEdges(D,A[0],A,B,C)
			elif E is'V1':D=cmds.ls(cmds.polyListComponentConversion(F[0],fv=_A,te=_A),fl=_A);A,B,C=addEdges(D,A[0],A,B,C)
			elif E is'V2':D=cmds.ls(cmds.polyListComponentConversion(F[1],fv=_A,te=_A),fl=_A);A,B,C=addEdges(D,A[0],A,B,C)
			elif E is _C and len(A==1):B.append(C);A.remove(A[0]);G=_B
			else:G=_B;A.remove(A[0])
			if J>=2 or len(A)<=0:break
		except:break
	if len(B)>=1:cmds.select(B)
	else:cmds.select(I)