#Select edges along the spine of where you would like to create a new hair plane.
#Probably redoing this at some point
#Owner: Matt Taylor
#Add Referenced hair mesh
#Duplicate and Extract       
#Straighten UV magic
#Find distance between two objects
##Find correct edges to seelct after we change point order 
#Transfer UV coordinates to XY coordinates   
#Attach our hair mesh to our dupObj then move our dupObj back to newObj on our hair   
#Transfer UVs   
#Point Check
#Custom Invert cause maya is shit
#Shape the hairplanes ( Taper / Offset from the base mesh )
#MAIN_________________________________________________________________________________________________________________
_I='dR_DoCmd("convertSelectionToEdge")'
_H='performPolyStraightenUVs 0;'
_G='dR_DoCmd("convertSelectionToFace")'
_F='DeleteHistory;'
_E='Reference_HairPlane'
_D=None
_C='hair'
_B=False
_A=True
import maya.cmds as cmds,math,operator,maya.mel as mel,maya.api.OpenMaya as om
def addRefHair():
	if cmds.objExists(_E)==_B:ref=cmds.polyPlane(n=_E,sx=4,sy=4,w=10,h=10);cmds.rotate(90,0,0,ref,r=_A);cmds.move(5,5,0,ref);cmds.makeIdentity(apply=_A,t=1,r=1,s=1,n=0);cmds.polyUVSet(rename=_A,newUVSet=_C,uvSet='map1');mel.eval(_F);return ref
def duplicateExtract():
	def nameCleaner(rawName):cleanName=str(rawName).split("[u'",1)[1];cleanName=cleanName.split("']",1)[0];return cleanName
	faceSel=cmds.filterExpand(sm=34);shapeNode=cmds.listRelatives(faceSel[0],p=_A,pa=_A);objSel=cmds.listRelatives(shapeNode,p=_A,pa=_A);objSelName=nameCleaner(objSel);cmds.select(objSelName+'.f[:]',tgl=_A);invertedSel=cmds.ls(sl=1);newObjSel=cmds.duplicate(objSel);newObjSelName=nameCleaner(newObjSel)
	for x in range(len(invertedSel)):invertedSel[x]=invertedSel[x].replace(objSelName,newObjSelName)
	cmds.delete(newObjSel,ch=1);cmds.delete(invertedSel);cmds.select(newObjSel);return newObjSel
def straightenUV(startEdges,edges):
	faceSel=cmds.polyListComponentConversion(startEdges,fe=_A,tf=_A);faceSel=cmds.ls(faceSel,fl=_A);borderEdges=cmds.polyListComponentConversion(faceSel,ff=_A,te=_A,border=_A);borderEdges=cmds.ls(borderEdges,fl=_A);straightObj=faceSel[0].split('.')[0]
	if faceSel==_D:mel.eval('SelectFacetMask;');mel.eval('SelectAll;');faceSel=cmds.filterExpand(ex=_A,sm=34)
	faceSel=cmds.ls(faceSel,fl=_A)
	def projectUV():
		for face in faceSel:
			cmds.select(face);mel.eval('texNormalProjection 1 1 "" ;');UVs=cmds.polyListComponentConversion(face,ff=_A,tuv=_A);UVs=cmds.ls(UVs,fl=_A);count=0;cord=[[0,0],[0,1],[1,1],[1,0]]
			for uv in UVs:u,v=cmds.polyEditUV(uv,r=_B,q=_A);u=cord[count][0];v=cord[count][1];cmds.polyEditUV(uv,r=_B,u=u,v=v);count=count+1
	def findEdges():
		myEdges=cmds.polyListComponentConversion(faceSel,ff=_A,te=_A);myEdges=cmds.ls(myEdges,fl=_A);straightEdges=[]
		for edge in myEdges:
			if edge not in borderEdges:straightEdges.append(edge)
		return straightEdges
	def mergeEdges(edgeList):cmds.select(edgeList);mel.eval('performPolyMapSewMove 0;')
	def orientUV():
		edgeVtxs=cmds.polyListComponentConversion(startEdges[0],fe=_A,tv=_A);edgeVtxs=cmds.ls(edgeVtxs,fl=_A);borderVtx=cmds.polyListComponentConversion(borderEdges,fe=_A,tv=_A);borderVtx=cmds.ls(borderVtx,fl=_A);edgeUVs=[]
		for vtx in edgeVtxs:
			if vtx in borderVtx:uv=cmds.polyListComponentConversion(vtx,fv=_A,tuv=_A);edgeUVs.append(uv)
		for vtx in edgeVtxs:
			uv=cmds.polyListComponentConversion(vtx,fv=_A,tuv=_A)
			if uv not in edgeUVs:edgeUVs.append(uv)
		UV1=cmds.polyEditUV(edgeUVs[0],r=_B,q=_A);UV2=cmds.polyEditUV(edgeUVs[1],r=_B,q=_A);allUVs=cmds.polyListComponentConversion(faceSel,ff=_A,tuv=_A);allUVs=cmds.ls(allUVs,fl=_A)
		if round(UV1[0],1)<round(UV2[0],1):cmds.polyEditUV(allUVs,rot=_A,angle=90)
		elif round(UV1[0],1)>round(UV2[0],1):cmds.polyEditUV(allUVs,rot=_A,angle=-90)
		elif round(UV1[1],1)>round(UV2[1],1):cmds.polyEditUV(allUVs,rot=_A,angle=180)
	def backFaceCheck():
		UVs=cmds.polyListComponentConversion(faceSel,ff=_A,tuv=_A);UVs=cmds.ls(UVs,fl=_A);cmds.select(UVs);mel.eval('selectUVFaceOrientationComponents {} 0 2 1;');uvCount=cmds.polyEvaluate(uv=_A)
		if uvCount>0:cmds.select(UVs);mel.eval('polyForceUV -flipHorizontal -local')
	projectUV();InteriorfoundEdges=findEdges();mergeEdges(InteriorfoundEdges);orientUV();backFaceCheck();cmds.select(straightObj);cmds.polyMultiLayoutUV(scale=2,layout=2);mel.eval(_H)
def distanceFinder(a,b):
	firstValue=math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2+(b[2]-a[2])**2);secondValue=math.sqrt((b[3]-a[3])**2+(b[4]-a[4])**2+(b[5]-a[5])**2)
	if firstValue<1e-21 and secondValue<1e-21:return _A
	else:return _B
def findSelAfterOrderChange(edges):
	newEdges=cmds.filterExpand(sm=32);cmds.select(cl=_A);foundEdges=[]
	for edge in edges:
		ogPos=cmds.xform(edge,q=_A,ws=_A,t=_A)
		for newEdge in newEdges:
			newPos=cmds.xform(newEdge,q=_A,ws=_A,t=_A);found=distanceFinder(ogPos,newPos)
			if found==_A:foundEdges.append(newEdge)
	return foundEdges
def blendShape(obj):
	dupObject=cmds.duplicate(obj);mel.eval(_G);dupFaces=cmds.ls(sl=_A,fl=_A);mel.eval('dR_DoCmd("convertSelectionToVertex")');dupVerts=cmds.ls(sl=_A,fl=_A)
	for vtx in dupVerts:uv=cmds.polyListComponentConversion(vtx,fv=_A,tuv=_A);u,v=cmds.polyEditUV(uv,r=_B,q=_A);cmds.xform(vtx,ws=_A,t=(u*10,v*10,0),a=_A)
	dupObject=cmds.ls(dupObject,fl=_A);return dupObject[0]
def wrapDef(a,b,c):cmds.select(a,b);mel.eval('CreateWrap;');cmds.transferAttributes(c,b,pos=_A,sampleSpace=5,searchMethod=3);cmds.transferAttributes(b,c,transferUVs=2,sourceUvSet=_C,targetUvSet=_C,sampleSpace=5,searchMethod=3);cmds.select(a,b,c);mel.eval(_F)
def transferUVs(a,b):
	try:a=str(a).split("'")[1]
	except:pass
	try:b=str(b).split("'")[1]
	except:pass
	cmds.select(a,b);cmds.transferAttributes(a,b,transferUVs=1,sourceUvSet=_C,targetUvSet=_C,sampleSpace=0,searchMethod=3);mel.eval('transferAttributes -transferPositions 0 -transferNormals 0 -transferUVs 1 -sourceUvSet "hair" -targetUvSet "hair" -transferColors 0 -sampleSpace 0 -sourceUvSpace "hair" -targetUvSpace "hair" -searchMethod 3-flipUVs 0 -colorBorders 1 ;')
def pointChecker(edge):
	point=_B;faceCheck=cmds.polyListComponentConversion(edge,fe=_A,tf=_A);vtxCheck=cmds.polyListComponentConversion(faceCheck,ff=_A,tv=_A);vtxCheck=cmds.ls(vtxCheck,fl=_A);cmds.select(vtxCheck);vtxCount=cmds.polyEvaluate(vc=_A)
	if vtxCount==4:point=_A
	return point
def invertSel(edgeSel):
	invObjSel=edgeSel[0].split('.')[0];edgeSel=cmds.ls(cmds.filterExpand(sm=32),fl=_A);cmds.select(invObjSel);mel.eval(_I);newSel=cmds.ls(cmds.filterExpand(sm=32),fl=_A)
	for item in edgeSel:
		if item in newSel:index=newSel.index(item);newSel.pop(index)
	cmds.select(newSel)
def shapeHairPlane(startEdges):
	cmds.select(startEdges);mel.eval(_G);tBorder=cmds.polyListComponentConversion(ff=_A,te=_A,border=_A);tBorder=cmds.ls(tBorder,fl=_A);cmds.select(tBorder);cmds.select(startEdges,add=_A);e=cmds.ls(tBorder,fl=_A);edgesToScale=invertSel(e);edgesToScale=cmds.ls(sl=_A,fl=_A);sortedEdges=[];tracker=[];triFix=_D;count=0
	for edge in startEdges:
		count=count+1;cmds.select(edge);mel.eval('evalEcho("select `ls -sl`;PolySelectTraverse 1;select `ls -sl`;")');edgeToCheck=cmds.ls(sl=_A,fl=_A);edgeGroup=[];valid=_A
		if count==1:
			if pointChecker(edge):valid=_B
		if count==len(startEdges):
			if pointChecker(edge):triFix=edge;valid=_B
		if valid:
			for check in edgeToCheck:
				if check in edgesToScale and check not in tracker:edgeGroup.append(check);tracker.append(check)
				elif count==len(startEdges)and check not in tracker and check not in startEdges:edgeGroup.append(check);tracker.append(check)
		if len(edgeGroup)>0:sortedEdges.append(edgeGroup)
	startVtx=cmds.polyListComponentConversion(startEdges,fe=_A,tv=_A);startVtx=cmds.ls(startVtx,fl=_A);increment=1./len(sortedEdges);scaleIndex=0;offsetIndex=0;count=0;startScaling=len(sortedEdges)/3;scaleEdge=_B
	for edgeGroup in sortedEdges:
		offsetIndex=offsetIndex+1
		if count>=startScaling:scaleEdge=_A
		if scaleEdge==_A:
			scaleAmount=1.-increment*scaleIndex;translateAmount=increment*(offsetIndex+1)
			if offsetIndex>=len(sortedEdges):scaleAmount=-.5
			try:
				cmds.polyMoveEdge(sortedEdges[count],ls=(scaleAmount,scaleAmount,scaleAmount),ltz=translateAmount);midVtx=cmds.polyListComponentConversion(sortedEdges[count],fe=_A,tv=_A);midVtx=cmds.ls(midVtx,fl=_A)
				for vtx in midVtx:
					if vtx in startVtx:cmds.polyMoveVertex(vtx,ltz=.5)
			except:pass
			scaleIndex=scaleIndex+2
		else:
			translateAmount=increment*(offsetIndex+1)
			try:
				cmds.polyMoveEdge(sortedEdges[count],ltz=translateAmount);midVtx=cmds.polyListComponentConversion(sortedEdges[count],fe=_A,tv=_A);midVtx=cmds.ls(midVtx,fl=_A)
				for vtx in midVtx:
					if vtx in startVtx:cmds.polyMoveVertex(vtx,ltz=.5)
			except:pass
		count=count+1
	if triFix!=_D:
		borderVtx=cmds.polyListComponentConversion(tBorder,fe=_A,tv=_A,border=_A);borderVtx=cmds.ls(borderVtx,fl=_A);triVtx=cmds.polyListComponentConversion(triFix,fe=_A,tv=_A);triVtx=cmds.ls(triVtx,fl=_A);count=0;tipVtx=_D
		for vtx in triVtx:
			if vtx in borderVtx:tipVtx=vtx
		translateAmount=increment*(offsetIndex+1);cmds.polyMoveVertex(tipVtx,ltz=translateAmount)
def CreateHairPlane():
	edges=cmds.filterExpand(sm=32);edges=cmds.ls(edges,fl=_A,os=_A);mel.eval(_G);faces=cmds.filterExpand(sm=34);cmds.select(faces);object=edges[0].split('.')[0];cmds.select(object);uvIndex=cmds.polyUVSet(object,q=_A,uvn=_A)
	try:
		uvSet=cmds.getAttr(object+'.uvSet['+str(uvIndex[1])+'].uvSetName')
		if uvSet!=_C:cmds.polyUVSet(rename=_A,newUVSet=_C,uvSet=str(uvSet))
	except:cmds.polyUVSet(create=_A,uvSet=_C)
	cmds.polyUVSet(currentUVSet=_A,uvSet=_C)
	if cmds.objExists(_E)==_B:hairRef=addRefHair()
	else:hairRef=_E
	if hairRef!=_D:cmds.select(faces);newObj=duplicateExtract();cmds.select(newObj);mel.eval(_I);foundEdges=findSelAfterOrderChange(edges);straightenUV(foundEdges,edges);dupObject=blendShape(newObj);transferUVs(hairRef,dupObject);wrapDef(hairRef,dupObject,newObj);shapeHairPlane(foundEdges);cmds.select(newObj);mel.eval(_F);newObj=cmds.rename(newObj,'Hairplane_01');cmds.delete(hairRef,dupObject);cmds.select(newObj);mel.eval(_H)
	else:cmds.warning('Missing da reference file')
def snap_curve_to_surface_realtime(curve_name,surface_name):
	if not cmds.objExists(curve_name)or not cmds.objExists(surface_name):raise ValueError('Curve or surface does not exist.')
	def update_cvs():
		if not cmds.objExists(curve_name):return
		cvs=cmds.ls(curve_name+'.cv[*]',fl=_A)
		if not cvs:return
		sel=om.MSelectionList();sel.add(surface_name);dagPath=sel.getDagPath(0);mfnMesh=om.MFnMesh(dagPath)
		for cv in cvs:pos=cmds.pointPosition(cv,world=_A);point=om.MPoint(pos);closestPoint,normal,_=mfnMesh.getClosestPointAndNormal(point,om.MSpace.kWorld);cmds.xform(cv,ws=_A,t=(closestPoint.x,closestPoint.y,closestPoint.z))
	global snapJob
	if'snapJob'in globals():
		try:cmds.scriptJob(kill=snapJob,force=_A)
		except:pass
	snapJob=cmds.scriptJob(event=['idle',update_cvs])