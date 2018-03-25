#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:58:51 2018

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
else:
    print('Connection unsuccessful')
    sys.exit('Could not Connect')