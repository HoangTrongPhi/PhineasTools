#Rename renamer 
#Owner: Matt Taylor
#NAME  
##SELECT
_A=True
import maya.cmds as cmds,maya.mel as mel,random
def rename(type,r,g,b):
	C=cmds.ls(sl=_A)
	if not C:cmds.warning('Select an object before pressing the button')
	for B in C:
		A=cleanName(str(B).lower())
		if cmds.objExists(A+str(type))and B!=A+str(type):A=A+str(random.randrange(1,10000))
		A=A+str(type);cmds.rename(B,A);colorName(A,r,g,b)
def cleanName(name):
	B='_';A=name
	if A.endswith(B):A=A[:-1]
	if A.startswith(B):A=A[1:]
	A=A.split(B,1);A=A[0];return A
def selectMesh(type):
	cmds.select(clear=_A);B=cmds.ls(tr=1,fl=_A)
	for A in B:
		if type in A:cmds.select(A,add=_A)
def colorName(obj,r,g,b):cmds.setAttr(obj+'.useOutlinerColor',_A);cmds.setAttr(obj+'.outlinerColor',r,g,b);mel.eval('AEdagNodeCommonRefreshOutliners();')
def colorWF(obj,r,g,b):A=obj;cmds.setAttr(A+'.overrideEnabled',1);cmds.setAttr(A+'.overrideRGBColors',1);cmds.setAttr(A+'.overrideColorR',r);cmds.setAttr(A+'.overrideColorG',g);cmds.setAttr(A+'.overrideColorB',b)
def colorSelectedObjects(outliner,r,g,b):
	B=cmds.ls(sl=_A)
	if outliner:
		for A in B:colorName(A,r,g,b)
	else:
		for A in B:colorWF(A,r,g,b)
def replace(all,old,new):
	if all:B=cmds.ls(dag=1,long=False)
	else:B=cmds.ls(sl=1)
	for A in B:
		if str(old)in A:
			C=A.replace(str(old),str(new))
			try:cmds.rename(A,C)
			except:pass