#Select just two edges to define selection pattern. Eventually I want to make this work with faces and vertices.
#Owner: Matt Taylor
#Edge Pattern
#Face Pattern		
_E='Select just two edges to define the pattern'
_D='polySelectEdges edgeLoopOrBorder;'
_C=False
_B='polySelectEdges edgeRing;'
_A=True
import maya.cmds as cmds,maya.mel as mel
def pattern():
	A=cmds.filterExpand(sm=32);B=cmds.filterExpand(sm=34)
	if not A and not B or A and B:cmds.warning('Select either faces or edges to define a pattern')
	elif A:edgePattern()
	elif B:facePattern()
def edgePattern():
	cmds.undoInfo(openChunk=_A);A=cmds.filterExpand(sm=32);cmds.select(A[0]);mel.eval(_D);B=cmds.filterExpand(sm=32);cmds.select(A[0]);mel.eval(_B);C=cmds.filterExpand(sm=32)
	if A[1]in B:cmds.select(A);loopPattern()
	elif A[1]in C:cmds.select(A);ringPattern()
	else:cmds.select(A);cmds.warning('Select two edges on ring or loop')
	cmds.undoInfo(closeChunk=_A)
def loopPattern(*F):
	A=cmds.ls(sl=1);C=A[0].split('.')[0];B=[]
	if len(A)==2:
		for D in A:E=D.split('.e[')[1];B.append(E.split(']')[0])
		cmds.polySelect(C,edgeLoopPattern=(int(B[0]),int(B[1])))
	elif len(A)==1:mel.eval(_D)
	else:cmds.warning(_E)
def ringPattern(*F):
	A=cmds.ls(sl=1);C=A[0].split('.')[0];B=[]
	if len(A)==2:
		for D in A:E=D.split('.e[')[1];B.append(E.split(']')[0])
		cmds.polySelect(C,edgeRingPattern=(int(B[0]),int(B[1])))
	elif len(A)==1:mel.eval(_B)
	else:cmds.warning(_E)
def findSharedEdges(allEdges,borderEdges):return[A for A in allEdges if A not in borderEdges]
def findLeadEdge(newEdges,currentEdges):
	A=[];D=cmds.ls(cmds.polyListComponentConversion(currentEdges,fe=_A,tv=_A),fl=_A)
	for B in newEdges:
		E=cmds.ls(cmds.polyListComponentConversion(B,fe=_A,tv=_A),fl=_A);C=_A
		for F in E:
			if F in D:C=_C
		if C:A.append(B)
	return A[0]
def buildSortedList(startingFaces,ringFaces,leadEdge,tailEdge):
	B=leadEdge;A=[];A.extend(startingFaces)
	while len(A)<len(ringFaces):
		D=cmds.ls(cmds.polyListComponentConversion(B,fe=_A,tf=_A),fl=_A)
		if len(D)==2:
			for C in D:
				if C not in A:E=cmds.ls(cmds.polyListComponentConversion(C,ff=_A,te=_A),fl=_A);B=findLeadEdge(E,B);A.append(C)
		else:B=tailEdge
	return A
def facePattern():
	C=cmds.ls(sl=_A,fl=_A,type='float3')
	if not patchCheck(C):cmds.warning('Selected faces must be one connected patch.');P=_C
	else:
		cmds.undoInfo(openChunk=_A);D=len(C);L=cmds.ls(cmds.polyListComponentConversion(C,ff=_A,te=_A),fl=_A);F=cmds.ls(cmds.polyListComponentConversion(te=_A,border=_A),fl=_A);E=findSharedEdges(L,F);I=findLeadEdge(F,E);J=E;J.append(I);M=findLeadEdge(F,J)
		if not E:cmds.warning("Couldn't find shared edge between selected faces.");return
		cmds.select(E);mel.eval(_B);N=cmds.ls(cmds.polyListComponentConversion(fe=_A,tf=_A),fl=_A);G=buildSortedList(C,N,I,M);O=next((A for(A,B)in enumerate(G)if B in C),0);H=[];A=O;B=len(G);B=B//D*D;K=0
		while K<B:
			H.extend(G[A:A+D]);A+=D*2;K+=D*2
			if A>=B:A=A%B
			if len(H)>=B:break
		cmds.select(H,r=_A);cmds.undoInfo(closeChunk=_A)
def getNeighborFaces(face):A=cmds.polyListComponentConversion(face,ff=_A,te=_A);A=cmds.ls(A,fl=_A);B=cmds.polyListComponentConversion(A,fe=_A,tf=_A);B=cmds.ls(B,fl=_A);return[A for A in B if A!=face]
def patchCheck(faceSel):
	B=faceSel
	if not B:return _C
	F=set(B);A=set();C=[B[0]]
	while C:
		D=C.pop()
		if D in A:continue
		A.add(D);G=getNeighborFaces(D)
		for E in G:
			if E in F and E not in A:C.append(E)
	return A==F