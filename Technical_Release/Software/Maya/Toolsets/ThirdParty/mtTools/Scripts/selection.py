#Selection
#By Matt Taylor
#Select Hard Edges
_A=True
import maya.cmds as cmds,maya.mel as mel
def hardEdgeSelect():A=cmds.ls(sl=1);cmds.polySelectConstraint(m=3,t=32768,sm=1);B=cmds.ls(cmds.filterExpand(sm=32));cmds.polySelectConstraint(m=0)
def hardEdgeToCrease():
	B=cmds.ls(sl=_A);cmds.polyCrease(op=2);hardEdgeSelect();A=cmds.ls(sl=_A,fl=_A)
	if A:cmds.polyCrease(value=2)
def hardEdgeSubdivide():
	A=cmds.ls(sl=_A);cmds.polyCrease(op=2);hardEdgeSelect();B=cmds.ls(sl=_A,fl=_A)
	if B:cmds.polyCrease(value=2)
	cmds.select(A);cmds.polySmooth(khe=0,ksb=1,kb=0,c=1,dv=2);cmds.polySmooth(khe=0,ksb=0,kb=0,c=1,dv=1)
def InvertSel():
	G=cmds.ls(sl=1,fl=_A);I=cmds.ls(hl=_A,fl=_A);B=cmds.ls(cmds.filterExpand(sm=31));C=cmds.ls(cmds.filterExpand(sm=34));D=cmds.ls(cmds.filterExpand(sm=32));E=cmds.ls(cmds.filterExpand(sm=35));A=[]
	if len(B)>0 or len(C)>0 or len(D)>0 or len(E)>0:
		mel.eval('SelectAll;')
		if len(B)>0:A.extend(cmds.ls(cmds.filterExpand(sm=31)))
		if len(C)>0:A.extend(cmds.ls(cmds.filterExpand(sm=34)))
		if len(D)>0:A.extend(cmds.ls(cmds.filterExpand(sm=32)))
		if len(E)>0:A.extend(cmds.ls(cmds.filterExpand(sm=35)))
		for F in G:
			if F in A:H=A.index(F);A.pop(H)
		cmds.select(A)