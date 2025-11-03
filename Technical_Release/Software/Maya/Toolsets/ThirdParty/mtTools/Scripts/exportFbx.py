#Export fbx's and do the things that need to be done before that happens
#Owner: Matt Taylor
_A=True
import maya.cmds as cmds,maya.mel as mel,os,re,subprocess
def export(path,useBakeGroups,useSelected):
	L='_HIGH';K='Exporting ';J='Exporting';F='FBXExport -f "{}" -s';D=path;print(os.path.normpath(D))
	if not os.path.exists(os.path.dirname(os.path.normpath(D))):cmds.warning('Choose an valid file location and try again')
	else:
		if useSelected:C=cmds.ls(sl=_A)
		else:C=cmds.ls(tr=1,fl=_A)
		if useBakeGroups:
			G=os.path.splitext(D.rstrip('/'))[0];M=['_LOW','_LOD1'];cmds.progressWindow(title=J,pr=0,ii=_A)
			for E in M:
				A=0;B=selectMesh(E,C)
				if B:
					cmds.undoInfo(openChunk=_A);N=cmds.group(em=_A,name='null1');H=cmds.duplicate(B);cmds.parent(H,N);I=0
					for O in H:cmds.rename(O,B[I]);I+=1;A+=1;cmds.progressWindow(edit=_A,progress=A,status=K+E)
					cmds.polyNormalPerVertex(freezeNormal=_A);mel.eval('Triangulate;');mel.eval('FBXExportSmoothingGroups -v true');mel.eval('FBXExportHardEdges -v false');mel.eval('FBXExportTangents -v true');mel.eval('FBXExportSmoothMesh -v false');mel.eval('FBXExportInstances -v false');mel.eval('FBXExportReferencedAssetsContent -v false');mel.eval('FBXExportAnimationOnly -v false');mel.eval('FBXExportBakeComplexAnimation -v false');mel.eval('FBXExportBakeComplexStep -v 0');mel.eval('FBXExportUseSceneName -v false');mel.eval('FBXExportQuaternion -v euler');mel.eval('FBXExportShapes -v false');mel.eval('FBXExportSkins -v false');mel.eval('FBXExportConstraints -v false');mel.eval('FBXExportCameras -v false');mel.eval('FBXExportLights -v false');mel.eval('FBXExportEmbeddedTextures -v false');mel.eval('FBXExportInputConnections -v false');mel.eval('FBXExportUpAxis y');mel.eval('FBXExportFileVersion -v FBX201800');mel.eval('FBXExportInAscii -v true');mel.eval('FBXExportTriangulate -v true; ');mel.eval('FBXExportTangents -v true;');mel.eval(F.format(str(G)+str(E)));cmds.undoInfo(closeChunk=_A);cmds.undo()
				B=[];cmds.select(clear=_A)
			B=selectMesh(L,C)
			if B:A+=1;cmds.progressWindow(edit=_A,progress=A,status='Exporting _HIGH');cmds.undoInfo(openChunk=_A);mel.eval('DeleteUVs;');cmds.select(B);mel.eval('CreatePolyFromPreview;');mel.eval(F.format(str(G)+L));cmds.undoInfo(closeChunk=_A);cmds.undo();cmds.select(clear=_A)
		else:
			A=0;cmds.progressWindow(title=J,pr=A,ii=_A)
			for P in C:cmds.select(P);mel.eval(F.format(str(D)));A+=1;cmds.progressWindow(edit=_A,progress=A,status=K+E)
			cmds.select(C)
		cmds.progressWindow(endProgress=1)
def selectMesh(type,objList):
	cmds.select(clear=_A);B=[]
	for A in objList:
		if type in A:cmds.select(A,add=_A);B.append(A)
	return B
def exportBrowse():
	A='';B=cmds.fileDialog2(fileMode=0,caption='Save FBX As',fileFilter='FBX Files (*.fbx)')
	if B!=None and B!='':A=str(B[0])
	if A[-1]!='/'or A[-1]!='\\':A=A+'/'
	return A
def process_exists(process_name):A=process_name;B='TASKLIST','/FI','imagename eq %s'%A;C=subprocess.check_output(B).decode();D=C.strip().split('\r\n')[-1];return D.lower().startswith(A.lower())