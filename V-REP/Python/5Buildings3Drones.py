#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:37:43 2018

@author: aditya
"""
import vrep
import vrepConst
import sys
import numpy as np


vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Connected to remote API server')
    emptyBuff = bytearray()
    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'displayText_function',[],[],['Hello world!'],emptyBuff,vrep.simx_opmode_blocking)
    if res==vrep.simx_return_ok:
        print ('Return string: ',retStrings[0]) # display the reply from V-REP (in this case, just a string)
    else:
        print ('Remote function call failed')
        
     # 2. Now create a dummy object at coordinate 0.1,0.2,0.3 with name 'MyDummyName':
    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,'remoteApiCommandServer',vrep.sim_scripttype_childscript,'createDummy_function',[],[0.1,0.2,0.3],['MyDummyName1'],emptyBuff,vrep.simx_opmode_blocking)
    if res==vrep.simx_return_ok:
        print ('Dummy handle: ',retInts[0]) # display the reply from V-REP (in this case, the handle of the created dummy)
    else:
        print ('Remote function call failed')
    
    # 3. Now send a code string to execute some random functions:
    code="local octreeHandle=simCreateOctree(0.5,0,1)\n" \
    "simInsertVoxelsIntoOctree(octreeHandle,0,{0.1,0.1,0.1},{255,0,255})\n" \
    "return 'done'"
    res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(clientID,"remoteApiCommandServer",vrep.sim_scripttype_childscript,'executeCode_function',[],[],[code],emptyBuff,vrep.simx_opmode_blocking)
    if res==vrep.simx_return_ok:
        print ('Code execution returned: ',retStrings[0])
    else:
        print ('Remote function call failed')

else:
    print('Connection unsuccessful')
    #sys.exit('Could not Connect')
