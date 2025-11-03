#Assorted UV scripts
#Owner: Matt Taylor
#Applies a UV texture material to selected objects
_E='.repeatV'
_D='.repeatU'
_C=False
_B='UVChecker_File'
_A=True
import maya.cmds as cmds,maya.mel as mel,math,os
def toggleView():
	J='UVToolkitDockControl';G='MayaWindow';F='polyTexturePlacementPanel1Window';H=-1610;B=0;C=2560;D=1440;I=1600;E=1200;A=300
	if cmds.window(F,q=_A,ex=_A):
		if cmds.window(G,q=_A,le=_A)<-10:cmds.window(F,edit=_A,le=H,te=B,w=I-A+10,h=E);cmds.window(G,edit=_A,le=0,te=0,w=C,h=D);cmds.window(J,edit=_A,le=-A,te=B,w=A,h=E)
		else:cmds.window(F,edit=_A,le=0,te=0,t='Matts UV Editor',w=C-A,h=D);cmds.window(G,edit=_A,le=H,te=B,w=I,h=E);cmds.window(J,edit=_A,le=C-A,te=0,w=A,h=D)
def symStraighten():
	cmds.undoInfo(openChunk=_A);B=cmds.ls(sl=1,fl=_A);A=cmds.filterExpand(ex=_A,sm=34)
	if A==None:mel.eval('SelectFacetMask;');mel.eval('SelectAll;');A=cmds.filterExpand(ex=_A,sm=34)
	A=cmds.ls(A,fl=_A)
	def C():
		for D in A:
			cmds.select(D);mel.eval('texNormalProjection 1 1 "" ;');C=cmds.polyListComponentConversion(D,ff=_A,tuv=_A);C=cmds.ls(C,fl=_A);B=0;E=[[0,0],[0,1],[1,1],[1,0]]
			for F in C:G,H=cmds.polyEditUV(F,r=_C,q=_A);G=E[B][0];H=E[B][1];cmds.polyEditUV(F,r=_C,u=G,v=H);B=B+1
	def D():
		B=cmds.polyListComponentConversion(A,ff=_A,te=_A);B=cmds.ls(B,fl=_A);C=cmds.polyListComponentConversion(A,ff=_A,te=_A,border=_A);C=cmds.ls(C,fl=_A);D=[]
		for E in B:
			if E not in C:D.append(E)
		return D
	def E(edgeList):
		A=edgeList;cmds.select(A)
		for B in A:mel.eval('performPolyMapSewMove 0;')
	C();F=D();E(F);mel.eval('polyMultiLayoutUV -lm 1 -sc 1 -rbf 0 -fr 1 -ps 0.4851 -l 2 -gu 1 -gv 1 -psc 0 -su 1 -sv 1 -ou 0 -ov 0;');mel.eval('performPolyStraightenUVs 0;');cmds.select(B);cmds.undoInfo(closeChunk=_A)
def Offset():
	E='ConvertSelectionToUVs';cmds.undoInfo(openChunk=_A);B=cmds.ls(sl=_A);C=int(round(math.sqrt(len(B))));A=1;D=0
	for F in B:
		cmds.select(F);mel.eval(E);cmds.polyEditUV(relative=_A,uValue=A,vValue=D);cmds.select(cl=_A)
		if A==C:A=1;D+=1
		elif A<C:A+=1
	cmds.select(B);mel.eval(E);cmds.undoInfo(closeChunk=_A)
def Compress():
	A=2048.;D=cmds.filterExpand(sm=35)
	if D:
		cmds.undoInfo(openChunk=_A)
		for E in D:B,C=cmds.polyEditUV(E,r=_C,q=_A);B=round(B*A)/A;C=round(C*A)/A;cmds.polyEditUV(E,r=_C,u=B,v=C)
		cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Please select UVs')
def Move(uOffset,vOffset):
	A=cmds.filterExpand(sm=35)
	if A:
		cmds.undoInfo(openChunk=_A)
		for B in A:cmds.polyEditUV(B,r=_A,u=uOffset,v=vOffset)
		cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Please select UVs to Move')
def UnfoldUVs():
	cmds.undoInfo(openChunk=_A);B=cmds.ls(sl=_A,fl=_A)
	if not B:cmds.warning('Select objects or edges to unwrap');return
	for A in B:
		C=cmds.filterExpand(A,ex=_A,sm=32)
		if C:cmds.polyMapCut(C)
		cmds.u3dUnfold(A,ite=2);cmds.u3dOptimize(A);cmds.polyLayoutUV(A,scale=0,worldSpace=_C,lm=1)
	mel.eval('polyMultiLayoutUV -lm 1 -sc 0 -rbf 0 -fr 1 -ps 0.4851 -l 2 -gu 1 -gv 1 -psc 0 -su 1 -sv 1 -ou 0 -ov 0;');cmds.select(B,r=_A);cmds.undoInfo(closeChunk=_A)
def Snapshot(x,y):
	B=cmds.ls(sl=1)
	if B:A='c:/mtSnap.iff';cmds.uvSnapshot(o=_A,n=A,xr=ConvertIndexToRes(x),yr=ConvertIndexToRes(y),aa=_A);os.startfile(A)
	else:cmds.warning('Select an object to UVsnapshot')
def ConvertIndexToRes(x):
	A=0
	if x==0:A=128
	elif x==1:A=256
	elif x==2:A=512
	elif x==3:A=1024
	elif x==4:A=2048
	elif x==5:A=4096
	elif x==6:A=8192
	return A
def DensityGet():mel.eval('uvTkDoGetTexelDensity')
def DensitySet():mel.eval('uvTkDoSetTexelDensity')
def Scale(pu,pv,su,sv):cmds.polyEditUV(pivotU=pu,pivotV=pv,scaleU=su,scaleV=sv)
def Backfaces():mel.eval('selectUVFaceOrientationComponents {} 0 2 1;')
def Orient():mel.eval('texStackShells {};texOrientShells;')
def create_shader(name,node_type='blinn'):A=cmds.shadingNode(node_type,name=name,asShader=_A);B=cmds.sets(name='%sSG'%name,empty=_A,renderable=_A,noSurfaceShader=_A);cmds.connectAttr('%s.outColor'%A,'%s.surfaceShader'%B);return A,B
def applyUVMaterial(path):
	A='UVChecker';D=cmds.ls(A);E=cmds.ls(sl=_A,dag=_A,type='mesh',noIntermediate=_A)
	if len(D)==0:B,F=create_shader(A);G=path+'/checker.jpg';C=cmds.createNode('file',name=_B);cmds.setAttr(C+'.fileTextureName',G,type='string');cmds.setAttr(B+'.specularColor',0,0,0,type='double3');cmds.connectAttr(str(C)+'.outColor',B+'.color');cmds.sets(E,forceElement=F)
	else:cmds.hyperShade(a=A)
def checkerScaleUp():
	A=cmds.getAttr(_B+_D);B=cmds.getAttr(_B+_E)
	if A>1:cmds.setAttr(_B+_D,A-1);cmds.setAttr(_B+_E,A-1)
def checkerScaleDown():A=cmds.getAttr(_B+_D);B=cmds.getAttr(_B+_E);cmds.setAttr(_B+_D,A+1);cmds.setAttr(_B+_E,A+1)
def hardenUVShellBorders():
	D=cmds.ls(sl=_A,o=_A);E=[]
	for A in D:
		cmds.select(A,r=_A);cmds.polyNormalPerVertex(ufn=_A);cmds.polySoftEdge(A,a=180,ch=1);cmds.select(A+'.map[*]',r=_A);B=cmds.polyListComponentConversion(te=_A,internal=_A);B=cmds.ls(B,fl=_A)
		for F in B:
			C=cmds.polyListComponentConversion(F,tuv=_A);C=cmds.ls(C,fl=_A)
			if len(C)>2:E.append(F)
		cmds.polySoftEdge(E,a=0,ch=1)
	cmds.select(D)
def mergeUVs():
	I=cmds.ls(sl=1);A=cmds.filterExpand(sm=35);B=[];C=[]
	if A:
		cmds.undoInfo(openChunk=_A)
		for D in A:E,F=cmds.polyEditUV(D,r=_C,q=_A);B.append(E);C.append(F)
		G=sum(B)/len(B);H=sum(C)/len(C)
		for D in A:cmds.polyEditUV(D,r=_C,u=G,v=H)
		cmds.undoInfo(closeChunk=_A)
	else:cmds.warning('Please select UVs to Merge')