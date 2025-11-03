#WinFix
#By Matt Taylor
import maya.cmds as cmds
def WinFix():
	A=True
	for B in cmds.lsUI(windows=A,panels=A):
		try:cmds.window(B,edit=A,topLeftCorner=(0,0))
		except:pass