#EdgeAverage - Averages selected edges
#Owner: Matt Taylor
import maya.cmds as cmds,math
def edgeAverage(useTarget):
	O='Select atleast two edges';N=False;A=True;C=cmds.ls(os=1,fl=A);K=N
	if len(C)<2:cmds.warning(O)
	elif len(C)>=2 and'.e['in C[0]:K=A
	else:cmds.warning(O)
	L=[];D=[]
	if K==A:
		cmds.undoInfo(openChunk=A)
		class P:
			def __init__(A,x1Cord,y1Cord,z1Cord,x2Cord,y2Cord,z2Cord):A.x1Cord=x1Cord;A.y1Cord=y1Cord;A.z1Cord=z1Cord;A.x2Cord=x2Cord;A.y2Cord=y2Cord;A.z2Cord=z2Cord
		def Q(x):B=[];C=cmds.xform(x[0],q=A,worldSpace=A,t=A);D=cmds.xform(x[1],q=A,worldSpace=A,t=A);B.extend(C);B.extend(D);L.append(B)
		for B in C:cmds.select(B);H=cmds.polyListComponentConversion(tv=A);H=cmds.ls(H,fl=A);Q(H)
		for B in L:D.append(P(B[0],B[1],B[2],B[3],B[4],B[5]))
		def M(a):return math.sqrt((a.x2Cord-a.x1Cord)**2+(a.y2Cord-a.y1Cord)**2+(a.z2Cord-a.z1Cord)**2)
		E=[]
		for I in D:R=M(I);E.append(R)
		if useTarget==N:J=sum(E)/len(E)
		else:J=M(D[0]);print(J);print(D[0])
		F=[]
		for S in E:T=J/S;F.append(T)
		G=0
		for I in C:cmds.polyMoveEdge(I,ls=(F[G],F[G],F[G]));G+=1
		cmds.select(C);cmds.undoInfo(closeChunk=A)