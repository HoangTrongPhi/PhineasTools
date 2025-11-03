#Json manager
#Owner Matt Taylor
import json,os
def save(key,value,jsonFile):
	D='utf-8';C=jsonFile;B={}
	with open(C,'r',encoding=D)as A:B=json.load(A)
	A.close();B[key]=value
	with open(C,'w',encoding=D)as A:json.dump(B,A,indent=4)
	A.close()
def load(key,jsonFile):
	with open(jsonFile,'r')as A:B=json.load(A);A.close();return B.get(key,None)
def toggle(key,jsonFile):
	C=jsonFile
	with open(C,'r')as A:B=json.load(A)
	B[key]=not B[key]
	with open(C,'w')as A:json.dump(B,A,indent=4)