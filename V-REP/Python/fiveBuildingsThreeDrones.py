#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:37:43 2018

@author: aditya
"""
import vrep
import vrepConst
import sys
import time
import numpy as np
def setRobotPosition(clientID,robotHandle,position):
    return vrep.simxSetObjectPosition(clientID,robotHandle,-1,position,vrepConst.simx_opmode_oneshot)

def ComputePath(clientID,target,goal,targetbody):
    inInts=[]
    inFloats=[]
    inStrings=[]
    inBuffer=bytearray()
    ret,Quadricopter_target=vrep.simxGetObjectHandle(clientID,target,vrep.simx_opmode_oneshot_wait)
    ret,targetpos=vrep.simxGetObjectPosition(clientID,Quadricopter_target,-1,vrep.simx_opmode_oneshot_wait)
    #print targetpos
    targetpos=(targetpos[0],targetpos[1]+0.3,targetpos[2])
    #print targetpos
    ret = setRobotPosition(clientID,Quadricopter_target,targetpos)
    inStrings.extend([target,goal,targetbody])
    #print(inStrings)
    ret,retInts,retfloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'init_statespaces',inInts,inFloats,inStrings,inBuffer,vrep.simx_opmode_oneshot_wait)
    inStrings=[]
    if(len(retInts)< 1):
        print('Error in return')
    else:
        if(retInts[0] == 1):
            #print(retfloats)
            return True,retfloats
        else:
            print('Path could not be computed')
    return False,[]

def attackerGame(clientID,robotHandle):
    inInts=[]
    inFloats=[]
    inStrings=[]
    inBuffer=bytearray()
    inStrings.append(robotHandle)
    print(robotHandle)
    print(inStrings)
    ret,retInts,retfloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'attackerChoice_function',inInts,inFloats,inStrings,inBuffer,vrep.simx_opmode_oneshot_wait)
    
    

def traversePath(clientID,path,robotHandle,signalname,signalval):
    ret = vrep.simxSetStringSignal(clientID,signalname,'change',vrepConst.simx_opmode_oneshot)
    #ret = True
    startTime=time.time()
    while time.time()-startTime < 4:   
        x=True
    ret,robotHandle = vrep.simxGetObjectHandle(clientID,robotHandle,vrep.simx_opmode_oneshot_wait)
    if(ret ==0):
        for i in range(0,len(path),3):
           # print("dinchak")
            pos=(path[i],path[i+1],path[i+2])
            ret = setRobotPosition(clientID,robotHandle,pos)
            startTime=time.time()
            while time.time()-startTime < 6:   
                x=True
    ret = vrep.simxSetStringSignal(clientID,signalname,signalval,vrepConst.simx_opmode_oneshot)
    return ret

def vrepEpisodes(no, droneval, attackerval):
    gamedict = {0:'buildingA',1:'buildingB',2:'buildingC',3:'buildingD',4:'buildingO'}
    gamevaldict = {0:(-2.0251, 1.7687,0.4701),1:(1.1778,1.5797,0.71000),2:(1.1778,-2.0713,0.71),3:(-2.025,-1.8813,0.47),4:(0.29062,0.97000,1.3100)}
    vrep.simxFinish(-1)
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)    
    if clientID!=-1:
        print ('Connected to remote API server')
        startTime=time.time()
        ret,dghandle,uhandle=vrep.simxDisplayDialog(clientID,"Random Play","Round "+str(no+1)+" Begins", vrepConst.sim_dlgstyle_message, "",None,None,vrep.simx_opmode_blocking)
        while time.time()-startTime < 3:
            x=True
        ret = vrep.simxEndDialog(clientID,dghandle,vrepConst.simx_opmode_oneshot)
        #print(ret)
        
        #vrep.simxClearIntegerSignal(clientID,'Drone01', vrepConst.simx_opmode_oneshot)
        QUAD ="Quadricopter"
        QUAD_0="Quadricopter#0"
        QUAD_1="Quadricopter#1"
        QUAD_TARGET ='Quadricopter_target'
        QUAD_GOAL ='Quadricopter_goal'
        QUAD_BODY = 'Quadricopter_targetbody'
        QUAD_TARGET0 ='Quadricopter_target#0'
        QUAD_GOAL0 ='Quadricopter_goal0'
        QUAD_BODY0 = 'Quadricopter_target_0body'
        QUAD_TARGET1 ='Quadricopter_target#1'
        QUAD_GOAL1 ='Quadricopter_goal1'
        QUAD_BODY1 = 'Quadricopter_target_1body'

        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD_TARGET,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter,(-1.85,0.10,0.7550))
        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD_TARGET1,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter,(-1.85,-1.9220,0.7550))
        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD_TARGET0,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter,(-1.85,2.0687,0.7550))
        
#        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD,vrep.simx_opmode_oneshot_wait)
#        ret=setRobotPosition(clientID,Quadricopter,(-1.85,0.10,0.7550))
#        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD_1,vrep.simx_opmode_oneshot_wait)
#        ret=setRobotPosition(clientID,Quadricopter,(-1.85,-1.9220,0.7550))
#        ret,Quadricopter=vrep.simxGetObjectHandle(clientID,QUAD_0,vrep.simx_opmode_oneshot_wait)
#        ret=setRobotPosition(clientID,Quadricopter,(-1.85,2.0687,0.7550))
        
        ret,Quadricopter_goal=vrep.simxGetObjectHandle(clientID,QUAD_GOAL,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter_goal,gamevaldict[droneval[0]])
        ret,Quadricopter_goal=vrep.simxGetObjectHandle(clientID,QUAD_GOAL0,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter_goal,gamevaldict[droneval[1]])
        ret,Quadricopter_goal=vrep.simxGetObjectHandle(clientID,QUAD_GOAL1,vrep.simx_opmode_oneshot_wait)
        ret=setRobotPosition(clientID,Quadricopter_goal,gamevaldict[droneval[2]])
        print("Computing path for Drone 1")
        ret,path1= ComputePath(clientID,QUAD_TARGET,QUAD_GOAL, QUAD_BODY)
        if(ret==0 or ret==1 or ret == True):
            print("Path Computed fot Drone 1")
            print ("Traversing path for Drone 1")
            ret = traversePath(clientID,path1,QUAD_TARGET,'Drone01',gamedict[droneval[0]])
            
#        if (ret==0 or ret==1 or ret==True):
#            print("Path Traversed Successfully")
#            print("Computing path for Drone 2")
#            ret,path2= ComputePath(clientID,QUAD_TARGET0,QUAD_GOAL0,QUAD_BODY0)
#            #print path2
#            print("Path Computed fot Drone 2")
#            print ("Traversing path for Drone 2")
#            if (ret):
#                ret = traversePath(clientID,path2,QUAD_TARGET0,'Drone02',gamedict[droneval[1]])
#                
#        if (ret==0 or ret==1 or ret==True):
#            print("Path Traversed Successfully")
#            print("Computing path for Drone 3")
#            ret,path3= ComputePath(clientID,QUAD_TARGET1,QUAD_GOAL1,QUAD_BODY1)
#            print("Path Computed fot Drone 3")
#            print ("Traversing path for Drone 3")
#            if (ret):
#                ret = traversePath(clientID,path3,QUAD_TARGET1,'Drone03',gamedict[droneval[2]])
    #    for i in range(3):
    #        if(i ==0):
    #            
        if(ret==0 or ret==1 or ret == True):
            attackerGame(clientID,gamedict[attackerval[0]])
        print ret
        
    #        if(i ==0):
    #            
                
        
        
        
    #    emptyBuff = bytearray()
    #    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'displayText_function',[],[],['Hello world!'],emptyBuff,vrep.simx_opmode_blocking)
    #    if res==vrep.simx_return_ok:
    #        print ('Return string: ',retStrings[0]) # display the reply from V-REP (in this case, just a string)
    #    else:
    #        print ('Remote function call failed')
    #        
    #     # 2. Now create a dummy object at coordinate 0.1,0.2,0.3 with name 'MyDummyName':
    #    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'createDummy_function',[],[0.1,0.2,0.3],['MyDummyName1'],emptyBuff,vrep.simx_opmode_blocking)
    #    if res==vrep.simx_return_ok:
    #        print ('Dummy handle: ',retInts[0]) # display the reply from V-REP (in this case, the handle of the created dummy)
    #    else:
    #        print ('Remote function call failed')
    #    
    #    # 3. Now send a code string to execute some random functions:
    #    code="local octreeHandle=simCreateOctree(0.5,0,1)\n" \
    #    "simInsertVoxelsIntoOctree(octreeHandle,0,{0.1,0.1,0.1},{255,0,255})\n" \
    #    "return 'done'"
    #    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,"remoteApiCommandServer",vrep.sim_scripttype_childscript,'executeCode_function',[],[],[code],emptyBuff,vrep.simx_opmode_blocking)
    #    if res==vrep.simx_return_ok:
    #        print ('Code execution returned: ',retStrings[0])
    #    else:
    #        print ('Remote function call failed')
        vrep.simxFinish(clientID)
    else:
        print('Connection unsuccessful')
    #sys.exit('Could not Connect')

#vrepEpisodes(1)
