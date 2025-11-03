#Exports meshes for baking based on their suffixes.
#Owner: Matt Taylor
_C='translateZ'
_B='translateX'
_A=True
import os,maya.OpenMayaUI as OpenMayaUI,maya.cmds as cmds,math,itertools,heapq,maya.mel,random,maya.mel as mel
def explodeMesh(StpX,StpZ):
	B=StpZ;A=StpX;C=cmds.ls(sl=_A)
	if C:
		cmds.undoInfo(openChunk=_A);cmds.playbackOptions(minTime='0',maxTime='1');D=A;E=B;cmds.currentTime(0);cmds.cutKey(time=(0,2));cmds.makeIdentity(apply=_A,t=1,r=1,s=1,n=0);cmds.setKeyframe(t=0,at=_B);cmds.setKeyframe(t=0,at=_C)
		for F in C:cmds.move(A,0,B,F,relative=_A);cmds.setKeyframe(t=1,at=_B);cmds.setKeyframe(t=1,at=_C);A+=D;B+=E
		cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Select _HIGH meshes to explode')
def attachLow():
	Y='.tx';M='_LOD1';L='_LOW';I=False;E='_HIGH';J=_A;K=cmds.ls(sl=1,l=_A,o=_A);Q=[]
	if len(K)<2:cmds.warning('Select atleast two objects.');J=I
	R=0;S=0;N=0
	for A in K:
		if L in A:R+=1
		if E in A:S+=1
		if M in A:N+=1
		cmds.bakePartialHistory(A,preCache=_A);T=cmds.listRelatives(A,s=1)
		if T and len(T)>1:cmds.warning('Duplicate shape node found on '+A+'. Cleaning up.');mel.eval('OptimizeScene -deformers true -perform true;');Q.append(A)
		else:Q.append(A)
	if R==0:cmds.warning('You need atleast one LOW mesh selected');J=I
	if S==0:cmds.warning('You need atleast one HIGH mesh selected');J=I
	if J:
		cmds.undoInfo(openChunk=_A);K=cmds.ls(sl=_A);U=[];V=[];W=[];B=[];X=[];G=[]
		def Z(x):
			A=[]
			if E in x:B=str(x).split(E);B=B[0]+E;B=B+str(random.randrange(1,10000));cmds.rename(x,B);A.append(B);C=cmds.objectCenter(B,gl=_A);A.extend(C);A.append(E);V.append(A)
			elif L in x:A.append(x);C=cmds.objectCenter(x,gl=_A);A.extend(C);A.append(L);U.append(A);cmds.select(x);cmds.cutKey(time=(0,2));cmds.makeIdentity(x,apply=_A,t=1,r=1,s=1,n=0)
			elif M in x:A.append(x);C=cmds.objectCenter(x,gl=_A);A.extend(C);A.append(M);W.append(A);cmds.select(x);cmds.cutKey(time=(0,2));cmds.makeIdentity(x,apply=_A,t=1,r=1,s=1,n=0)
			else:cmds.warning(x+' is named incorrectly. Needs _HIGH, _LOW or _LOD1 suffix')
		for A in K:Z(A)
		for A in V:X.append(objOrgin(A[0],A[1],A[2],A[3],A[4]))
		for A in U:B.append(objOrgin(A[0],A[1],A[2],A[3],A[4]))
		for A in W:G.append(objOrgin(A[0],A[1],A[2],A[3],A[4]))
		for C in X:
			D=[]
			for a in B:D.append(distanceFinder(a,C))
			b=min(D);H=D.index(b)
			try:
				if cmds.keyframe(C.name+Y,q=_A)!=None:passXform(B[H],C)
			except:pass
			F=B[H].name.replace(L,E)
			if N>0:
				D=[]
				for c in G:D.append(distanceFinder(c,B[H]))
				d=min(D);O=D.index(d)
				try:
					if cmds.keyframe(B[H].name+Y,q=_A)!=None:passXform(G[O],B[H])
				except:pass
			def e(name):
				A=name;B=0;C=I
				while C==I and B<50:
					if cmds.objExists(A):A=name+str(B);B+=1
					else:C=_A
				return A
			F=e(F)
			if C.name!=F:cmds.rename(C.name,F);C.name=F
			if N>0:
				P=F.replace(E,M)
				if C.name!=P:cmds.rename(G[O].name,P);G[O].name=P
		cmds.undoInfo(closeChunk=_A)
class objOrgin:
	def __init__(A,name,xCord,yCord,zCord,type):A.name=name;A.xCord=xCord;A.yCord=yCord;A.zCord=zCord;A.type=type
def distanceFinder(a,b):A=math.sqrt((b.xCord-a.xCord)**2+(b.yCord-a.yCord)**2+(b.zCord-a.zCord)**2);return A
def passXform(a,b):
	if cmds.currentTime(query=_A)==0:cmds.currentTime(1);A=cmds.xform(b.name,query=_A,translation=_A,worldSpace=_A);cmds.currentTime(0);cmds.setKeyframe(a.name,t=0,at=_B);cmds.setKeyframe(a.name,t=0,at=_C);cmds.currentTime(1);cmds.move(A[0],0,A[2],a.name,relative=_A);cmds.setKeyframe(a.name,t=1,at=_B);cmds.setKeyframe(a.name,t=1,at=_C);cmds.currentTime(0)
	elif cmds.currentTime(query=_A)==1:A=cmds.xform(b.name,query=_A,translation=_A,worldSpace=_A);cmds.setKeyframe(a.name,t=1,at=_B);cmds.setKeyframe(a.name,t=1,at=_C);cmds.currentTime(0);cmds.move(-A[0],0,-A[2],a.name,relative=_A);cmds.setKeyframe(a.name,t=0,at=_B);cmds.setKeyframe(a.name,t=0,at=_C);cmds.currentTime(1)