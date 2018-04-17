#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:48:18 2018

@author: aditya
"""
import vrep
import vrepConst
import sys
import time
import numpy as np
import random
import fiveBuildingsThreeDrones as fiver

for i in range(1):
    droneval = random.sample(range(5), 3)
    print(droneval)
    attackerval = random.sample(range(5), 1)
    print(attackerval)
    fiver.vrepEpisodes(i,droneval,attackerval)
