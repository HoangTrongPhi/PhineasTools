#Modeling scene cleanup
#Matt Taylor
#Suffix__________________________________________________________________
#Functions__________________________________________________________________
#General scene cleanup
#Find and delete nodes that were left behind  
#Return all materials in scene
#Fix material names with correct suffix
#Return match if string is found in array
#Try to rename object, skip if not.
#Find nested place2dTexture nodes
#Find Root Groups
#DisplayLayer Cleanup
#Material cleanup
#Check if objects have skin cluster or not.
#MAIN LOOP__________________________________________________________________
_K='camera'
_J='place2dTexture'
_I='hair_'
_H=None
_G='file'
_F='lambert1'
_E='transform'
_D='LOD0'
_C='_'
_B=False
_A=True
import maya.cmds as cmds,maya.mel as mel
mat_SUFFIX='_MAT'
matInfo_SUFFIX='_MATINFO'
shading_SUFFIX='_SG'
bump_SUFFIX='_BUMP'
texture_SUFFIX='_TEXTURE'
place2dTexture_SUFFIX='_2DTEXTURE'
displayLayer_SUFFIX='_DL'
hair_SUFFIX='_HAIR'
MESH_SUFFIX=['_MESH','_LOD0','_LOD1','_LOD2','_LOD3','_LOD4']
GROUP_SUFFIX=[_D,'LOD1','LOD2','LOD3','LOD4']
BAKE_SUFFIX=['_LOW','_LOD1','_HIGH']
def sceneCleanup():
	G='_GROUPID';F='TurtleDefaultBakeLayer';H=cmds.ls(type='mesh',g=_A,fl=_A);I=cmds.listRelatives(H,parent=_A);J=cmds.ls(I);K=skinClusterChecker(J)
	if K==_B:mel.eval('DeleteAllHistory')
	else:mel.eval('BakeAllNonDefHistory')
	mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");');L=cmds.ls('pasted__*')
	for C in L:
		if cmds.objExists(C):cmds.rename(C,C.replace('pasted__',''))
	emptyTransforms();M=cmds.ls(g=_B,dep=_B,dag=_B);B=[]
	for A in M:
		if'groupId'in str(A)or G in str(A):
			N=cmds.listConnections(str(A))
			try:cmds.rename(A,N[0]+G)
			except:B.append(A)
		elif'objectFilter'in str(A):B.append(A)
		elif'objectTypeFilter'in str(A):B.append(A)
		elif'polySurfaceShape'in str(A):
			O=cmds.polyEvaluate(str(A),t=_A)
			if O==0:B.append(A)
		elif _E in str(A):B.append(A)
	if cmds.objExists(F):cmds.lockNode(F,l=0);cmds.delete(F)
	P=cmds.listConnections(_F)
	for D in P:
		if _G in D:E=cmds.listConnections(D);E=retrieveMatch(_J,E);cmds.delete(D);cmds.delete(E[0])
	if len(B)>0:cmds.delete(B)
	emptyTransforms();mel.eval('layerEditorSelectUnused;layerEditorDeleteLayer "";')
def emptyTransforms():
	C=_A;B=cmds.ls(type=_E,fl=_A)
	while C is _A:
		D=[];E=[]
		for A in B:
			if cmds.nodeType(A)==_E:
				F=cmds.listRelatives(A,c=_A)
				if F==_H:
					try:G=cmds.listRelatives(str(A),p=_A);D.append(G[0])
					except Exception as H:print(H)
					E.append(A)
		cmds.delete(E);B=D
		if len(B)==0:C=_B
def findOrphanNodes():
	C=cmds.ls(g=_B,dep=_B,dag=_B);B=[]
	for A in C:
		if _G in A:B.append(A)
		elif _J in A:B.append(A)
	cmds.delete(B)
def getMaterials():
	A=[]
	for B in cmds.ls(type='shadingEngine'):
		if cmds.sets(B,q=_A):
			for C in cmds.ls(cmds.listConnections(B),materials=_A):
				if C!=_F:A.append(C)
	return A
def nameMaterials(materials):
	C=[]
	for B in materials:
		if B!=_F:
			A=str(B).lower();A=nameCleanup(A)
			try:A=A.replace('_Mat',mat_SUFFIX).replace('_mat',mat_SUFFIX)
			except:pass
			if mat_SUFFIX not in A:A=A+mat_SUFFIX
			cmds.rename(str(B),A);C.append(A)
	return C
def retrieveMatch(string,list):
	try:A=[A for A in list if string in A];return A
	except:pass
def renameOBJ(objName,newName):
	try:cmds.rename(objName,newName)
	except:pass
def find2dTextures(obj):
	B=obj;C=cmds.listConnections(B);D=retrieveMatch(_J,C);A=''
	try:A=cmds.getAttr(str(B)+'.fileTextureName')
	except:pass
	try:A=A.rsplit('/',1)[1].split('.')[0]
	except:pass
	if A!='':cmds.rename(str(D[0]),A+place2dTexture_SUFFIX);cmds.rename(str(B),A+texture_SUFFIX)
def find_root_groups():
	'Find all root level transforms in scene that have immediate nurbs or polygon children.';A=[]
	for B in cmds.ls(ap=_A):
		for D in cmds.listRelatives(B,type=_E,children=_A)or[]:
			C=B.replace(_C,'')
			if C in GROUP_SUFFIX and C not in A:A.append(B)
	return A
def displayLayerCleanup():
	D=cmds.ls(type='displayLayer')
	for C in D:
		for A in GROUP_SUFFIX:
			if A in str(C):
				B=str(C).replace(displayLayer_SUFFIX,'').replace(_C+A+_C,'').replace(_C+A,'').replace(A+_C,'').replace(A,'')
				if B!='':B=B+_C
				B=B+A+displayLayer_SUFFIX;cmds.rename(C,B)
def materialCleanup(materials):
	for C in materials:
		if C!=_F:
			B=str(C);B=nameCleanup(B);B=B.replace(mat_SUFFIX,'');F=cmds.listConnections(str(C))
			for A in F:
				if'materialInfo'in A or matInfo_SUFFIX in A:renameOBJ(str(A),B+matInfo_SUFFIX)
				elif'SG'in A or shading_SUFFIX in A:renameOBJ(str(A),B+shading_SUFFIX)
				elif'bump'in A or bump_SUFFIX in A:
					E=cmds.listConnections(A);D=retrieveMatch(_G,E)
					if len(D)==0:D=retrieveMatch(texture_SUFFIX,E)
					find2dTextures(D);cmds.rename(str(A),B+bump_SUFFIX)
				elif _G in A:find2dTextures(A)
def skinClusterChecker(shapeList):
	for A in shapeList:
		if not A.endswith('Orig'):
			try:
				B=cmds.listHistory(A)
				if B:
					for C in B:
						if cmds.objectType(C)=='skinCluster':return _A
			except:return-1
	return _B
def cameraCleanup():
	G='.visibility';D='.v';E=cmds.ls(type=_K,l=_A);F=[A for A in E if cmds.camera(cmds.listRelatives(A,parent=_A)[0],startupCamera=_A,q=_A)];H=list(set(E)-set(F))
	for B in H:
		mel.eval('camera -e -startupCamera false '+str(B)+';');C=cmds.listRelatives(B,parent=_A);A=str(C).split("'")[1]
		if'FP'not in A:cmds.delete(C)
		else:cmds.setAttr(A+D,lock=_B);cmds.setAttr(A+G,0);cmds.setAttr(A+D,lock=_A)
	for B in F:C=cmds.listRelatives(B,parent=_A);A=str(C).split("'")[1];cmds.setAttr(A+D,lock=_B);cmds.setAttr(A+G,0);cmds.setAttr(A+D,lock=_A)
def groupCleanup(group):
	M='hair';B=group;N=str(B.replace(_C,''));O=find_root_groups();G=[]
	for K in O:
		if K not in G:G.append(K)
	for E in G:
		L=str(E).replace(_C,'')
		if N in L:
			F=cmds.listRelatives(E,c=_A,f=_A);P=cmds.listRelatives(E,c=_A)
			if B==MESH_SUFFIX[1]:B=MESH_SUFFIX[0]
			C=0
			for A in P:
				Q=cmds.listRelatives(F[C],shapes=_A)
				if Q:
					H=A.lower();H=nameCleanup(H);A=cmds.rename(F[C],H)
					if B.lower()not in A:D=A+B.upper();cmds.rename(A,D)
					else:D=A.replace(B.lower(),B.upper());cmds.rename(A,D)
				elif'_hair'in A or _I in A or'_HAIR'in A or M in A:
					I=str(A.lower()).replace(hair_SUFFIX.lower(),'').replace(_I,'').replace(M,'')
					for R in MESH_SUFFIX:I=I.replace(R.lower(),'')
					S=cmds.listRelatives(F[C],p=_A);J=str(S[0])
					if GROUP_SUFFIX[0]in J:J=MESH_SUFFIX[0]
					D=I.lower()+hair_SUFFIX+J;cmds.rename(F[C],D)
				C+=1
		cmds.rename(E,L)
def nameCleanup(string):
	A=string
	if A.endswith(_C):A=A[:-1]
	if A.startswith(_C):A=A[1:]
	B=[A[::-1]for A in A[::-1].split(_C,1)][::-1];A=str(B[0]);A=A.replace('_cpso','').replace('__',_C);return A
def modelCleanup():
	K='UNCATEGORISED';G=_B
	for C in MESH_SUFFIX:groupCleanup(C)
	N=cmds.ls(type='mesh',g=_A,fl=_A);M=cmds.listRelatives(N,parent=_A);O=cmds.ls(M);E=cmds.ls(M,l=_A);D=0
	for L in O:
		B=_H;A=str(L).lower();A=A.replace('_cpso','').replace('_sort_hair','');H=str(cmds.listRelatives(L,p=_A))
		if hair_SUFFIX.lower()in A or _I in A:
			I=A.replace(hair_SUFFIX.lower(),'').replace(_I,'')
			for C in MESH_SUFFIX:
				if C.lower()in I:I=I.replace(C.lower(),'')
			F=cmds.listRelatives(E[D],p=_A);F=str(F[0]);Q=F[0];J=''
			if hair_SUFFIX in F:
				P=cmds.listRelatives(F,p=_A)
				for C in GROUP_SUFFIX:
					if C in str(P):
						J=_C+C
						if J==MESH_SUFFIX[1]:J=MESH_SUFFIX[0]
			A=I.lower()+hair_SUFFIX+J;B=_H
		elif MESH_SUFFIX[0].lower()in A:A=A.replace(MESH_SUFFIX[0].lower(),MESH_SUFFIX[0].upper());B=GROUP_SUFFIX[0]
		elif MESH_SUFFIX[1].lower()in A:A=A.replace(MESH_SUFFIX[0].lower(),MESH_SUFFIX[0].upper());B=GROUP_SUFFIX[0]
		elif MESH_SUFFIX[2].lower()in A:A=A.replace(MESH_SUFFIX[2].lower(),MESH_SUFFIX[2].upper());B=GROUP_SUFFIX[1]
		elif MESH_SUFFIX[3].lower()in A:A=A.replace(MESH_SUFFIX[3].lower(),MESH_SUFFIX[3].upper());B=GROUP_SUFFIX[2]
		elif MESH_SUFFIX[4].lower()in A:A=A.replace(MESH_SUFFIX[4].lower(),MESH_SUFFIX[4].upper());B=GROUP_SUFFIX[3]
		elif MESH_SUFFIX[5].lower()in A:A=A.replace(MESH_SUFFIX[5].lower(),MESH_SUFFIX[5].upper());B=GROUP_SUFFIX[4]
		if B!=_H:
			if cmds.objExists(B)==_A:
				H=str(cmds.listRelatives(E[D],p=_A))
				try:H=H.split("'")[1]
				except:pass
				if H!=B:cmds.parent(str(E[D]),B)
			else:cmds.group(em=_A,name=B)
		elif cmds.objExists(_D)==_B:cmds.group(em=_A,name=_D);cmds.parent(str(E[D]),_D);A=A+MESH_SUFFIX[0].upper();G=_A
		elif G:cmds.parent(str(E[D]),_D);A=A+MESH_SUFFIX[0].upper()
		elif G==_B and cmds.objExists(K)==_B:cmds.group(em=_A,name=K)
		elif G==_B and cmds.objExists(K)==_A:cmds.parent(str(E[D]),K)
		cmds.rename(L,A);D+=1
def bakeModelCleanUp():A=cmds.ls(tr=1,fl=_A);E=0;B=selectMesh(BAKE_SUFFIX[0],A);C=selectMesh(BAKE_SUFFIX[1],A);D=selectMesh(BAKE_SUFFIX[2],A);parentToGroup(B,'LOW');parentToGroup(C,'LOD');parentToGroup(D,'HIGH')
def parentToGroup(obj,targetGroup):
	B=obj;A=targetGroup
	if len(B)>0:
		if cmds.objExists(A)==_B:cmds.group(em=_A,name=A);cmds.parent(B,A)
		else:cmds.parent(B,A)
def selectMesh(type,objList):
	A=[]
	for B in objList:
		if type in B:A.append(B)
	return A
def removeTextureEditorIsolate():
	B=cmds.ls()
	for A in B:
		if'textureEditorIsolateSelectSet'in A:cmds.delete(A)
def cameraReset():
	E='.rotate';D='.translate';C='double3';G=cmds.ls(type=_K)
	for B in G:
		F=cmds.listRelatives(B,parent=_A)
		if F:
			A=F[0]
			if B=='perspShape':cmds.setAttr(A+'.focalLength',200);cmds.setAttr(A+D,2400,1700,2400,type=C);cmds.setAttr(A+E,-25,45,0,type=C)
			elif B=='frontShape':cmds.setAttr(A+D,0,130,2200,type=C);cmds.setAttr(A+E,0,0,0,type=C)
			elif B=='sideShape':cmds.setAttr(A+D,-2200,130,0,type=C);cmds.setAttr(A+E,0,-90,0,type=C)
			elif B=='topShape':cmds.setAttr(A+D,0,3300,0,type=C);cmds.setAttr(A+E,-90,0,0,type=C)
			cmds.setAttr(A+'.scale',1,1,1,type=C);cmds.xform(A,rotatePivot=(0,0,0),worldSpace=_A);cmds.setAttr(B+'.centerOfInterest',100);cmds.setAttr(B+'.nearClipPlane',5);cmds.setAttr(B+'.farClipPlane',1e6)
		try:cmds.viewLookAt(B)
		except:pass
def removeInstances():
	cmds.undoInfo(openChunk=_A);A=cmds.ls(dag=1,long=_B)
	for B in A:
		try:cmds.select(B);mel.eval('ConvertInstanceToObject;')
		except:pass
	cmds.select(clear=_A);cmds.undoInfo(closeChunk=_A)
def Main(fileType):
	D=fileType;import maya.cmds as A,maya.mel as E;A.undoInfo(openChunk=_A);A.lockNode('defaultTextureList1',l=_B,lockUnpublished=_B)
	if D=='Mesh':sceneCleanup();B=getMaterials();C=nameMaterials(B);materialCleanup(C);cameraCleanup();displayLayerCleanup();modelCleanup();removeTextureEditorIsolate();emptyTransforms();findOrphanNodes();sceneCleanup()
	elif D=='Bake':sceneCleanup();B=getMaterials();C=nameMaterials(B);materialCleanup(C);cameraCleanup();bakeModelCleanUp();emptyTransforms();findOrphanNodes();sceneCleanup();removeTextureEditorIsolate()
	A.undoInfo(closeChunk=_A);A.headsUpMessage('Cleanup Complete!',time=2.)