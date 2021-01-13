
#libraries
import numpy as np
import time, random, os, sys

#local imports
from mathTools import *    

class Camera():   
    def __init__(self, xmax, ymax, desiredFramerate):

        self.xmax = xmax
        self.ymax = ymax

        self.centerx = 0
        self.centery = 0

        self.desiredFramerate = desiredFramerate

        self.timeD = 0
        self.displayD = 0
        self.timeHolder = time.time() 
        self.frameRate = 0         

        self.timeScaling = 0.00001            # this is in seconds
        self.spaceScaling = 1.5           # 1 is a meter
    
    def frameHandler(self):
        self.frameRate = time.time() - self.timeHolder
        frameRateAdjust =  self.desiredFramerate - self.frameRate
        if frameRateAdjust < 0:
            frameRateAdjust = 0
        time.sleep(frameRateAdjust)
        self.timeHolder = time.time()

    def present(self, particleData):
        self.displayD += 1
        self.frameHandler()
        os.system('clear')
        ScanList = []
        print("in-sim time passed = "+ str(self.timeD)+ " | sim 'presented' "+ str(self.displayD)+" times | the frame rate is " + str(self.frameRate))
        for i in range(int(self.ymax)):
            if i == 0:
                print("===" * (self.xmax + 2))
            print(" ||", end="")
            for j in range(int(self.xmax)):
                ScanList = [p for p in particleData if (vDistance(np.array([p.x, p.y]), np.array([j * self.spaceScaling, i * self.spaceScaling])) <= p.material.value[1] )]
                if ScanList:
                    print(ScanList[0].material.value[-1], end= "")
                else:
                    print("   ", end="")
            print("|| ")
        print("===" * (self.xmax + 2))
        for p in particleData:
            print(p.__dict__)
            print('',end='')
