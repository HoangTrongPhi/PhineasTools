#Clean names in scene
#Owner: Matt Taylor
_B='pasted__*'
_A='pasted__'
import maya.cmds as cmds,re,sys,maya.mel
def pastedPlus():
	G='0123456789';D=False;A=True;H=D;maya.mel.eval('BakeNonDefHistory;');B=cmds.ls(g=A,l=A);I=[];F=[];C=[];P=D
	def J(sel):
		B=[]
		if len(sel)!=0:
			for C in sel:B.append(cmds.listRelatives(C,ap=A,f=A))
			return B
		else:return B
	def K():
		F=D
		for C in B:
			if len(cmds.listRelatives(C,s=1))>=1:0
			else:cmds.Warning('duplicate shadernode found ');F=A
		if not F:
			B.sort(key=len,reverse=A)
			for(H,C)in enumerate(B):
				G=cmds.listRelatives(C,ap=A)
				try:
					if _A in G[0]or'group'in G[0]:E=cmds.parent(C,w=A)
					else:E=C
				except:E=C
				B[H]=E
			for I in B:cmds.select(I,add=A)
			J=cmds.ls(sl=1,s=1,dag=1)
		return J
	def L():
		A=[]
		for object in I:
			B=0;C=cmds.listConnections(object,type='shadingEngine')
			for E in C:
				D=cmds.listConnections(C[B]+'.surfaceShader');B+=1
				if D not in A:A.append(D)
		return A
	def M():
		D=[];H=0
		for B in F:
			H+=1
			if _A in B:
				C=B.replace(_A,'',B.count(_A));N(C,B)
				if cmds.objExists(C):E(B,C);D.append(C)
				else:
					I=C.strip(G)
					if cmds.objExists(I):E(B,I)
		maya.mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
		if H>=len(F):return A,D
	def N(input,obj):
		F=D
		for B in C:
			try:input.index(B);E(obj,B);F=A
			except:pass
		if F==D:
			H=input.strip(G)
			for B in C:
				try:I=B.strip(G);H.index(I);E(obj,B)
				except:pass
	def E(badMat,goodMat):cmds.select(badMat);cmds.hyperShade(objects='');cmds.hyperShade(assign=goodMat)
	def O():
		E='transform'
		if H is A:
			F=cmds.ls(_B)
			for B in F:
				if cmds.objExists(B):cmds.rename(B,B.replace(_A,''))
			G=cmds.ls(type=E);C=[]
			for D in G:
				if cmds.nodeType(D)==E:
					I=cmds.listRelatives(D,c=A)
					if I==None:C.append(D)
			if len(C)>0:cmds.delete(C)
	B=J(B)
	if len(B)!=0:I=K();F=L();H,C=M();O()
def pasted():
	B=cmds.ls(_B)
	for A in B:
		if cmds.objExists(A):cmds.rename(A,A.replace(_A,''))