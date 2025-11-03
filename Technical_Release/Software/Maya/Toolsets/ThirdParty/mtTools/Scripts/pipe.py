#Create a pipe along selected edges
#Owner: Matt Taylor
import maya.cmds as cmds,maya.mel as mel
def makePipe():
	B=.3;C=8;D=.172;E=[];F=cmds.ls(sl=True);A=cmds.ls(cmds.filterExpand(sm=32))
	if not A:cmds.warning('Select an edge');return
	G=cmds.polyToCurve(f=0);print('A')
	try:mel.eval('sweepMeshMenuCallback')
	except:cmds.CreateSweepMesh()