
#libraries
import numpy as np
import time, random, sys, os
#local imports
from mathTools import *    

#global string that acts like an array of characters with the index as the value
#grayscalewtb goes from the most space filling characters to the least
grayscalewtb = "$@B%8&WM#oahkbdpqwmZO0QLYXCJUzcvunxrjft/\|()1}{[]?<>i!lI;:+~,.- "
#grayscalebtw goes from the least space filling characters to the most
grayscalebtw = ''.join(reversed(grayscalewtb))

#----------------------------------------------------------------------------------------------
#Camera is an object with location and properties used to hold printing functions and variables
#
class Camera():   
    #when the camera is created this function is called
    def __init__(self, xmax, ymax, desiredFramerate):
        #set the x dimensions of the screen
        self.xmax = xmax
        #set the y dimensions of the screen
        self.ymax = ymax
        #set the x location of the camera
        self.centerx = 0
        #set the y location of the camera
        self.centery = 0
        #set the desiredFramerate
        self.desiredFramerate = desiredFramerate
        #set timeD (the time between displays) to 0
        self.timeD = 0
        #set the times displayed to 0
        self.displayD = 0
        #set the timeholder variable to the current time
        self.timeHolder = time.time() 
        #set the initial frame rate to 0
        self.frameRate = 0         
        #set the spaceScaling
        self.spaceScaling = 1.5           # 1 is a meter

    #frameHandler manages a wait function to maintain a consistent framerate
    def frameHandler(self):
        #determine the current frame rate
        self.frameRate = time.time() - self.timeHolder
        #determine how far off the framerate is from the desired result
        frameRateAdjust =  self.desiredFramerate - self.frameRate
        #if the frame rate is lower than 0 set the adjustment timer to 0
        if frameRateAdjust < 0:
            #set the adjustment time to 0
            frameRateAdjust = 0
        #wait for the given amount of adjustment time
        time.sleep(frameRateAdjust)
        #set the time holder to the current time for later refrence
        self.timeHolder = time.time()

    #function that sacns the cameras vision space and prints it
    def present(self, particleData):
        #itterate the display count
        self.displayD += 1
        #activat the frameHandler to manage print speeds
        self.frameHandler()
        #clear the screen
        os.system('clear')
        #clear the scan list
        ScanList = []
        #print printing values
        print("in-sim time passed = "+ str(self.timeD)+ " | sim 'presented' "+ str(self.displayD)+" times | the frame rate is " + str(self.frameRate))
        #itterate through the range of the y dimension
        for i in range(int(self.ymax)):
            #if this is the top of the screen print a frame across the x dimension
            if i == 0:
                #print a horizontal border
                print("===" * (self.xmax + 2))
            #print verticle border
            print(" ||", end="")
            #itterate through the range of the x dimension
            for j in range(int(self.xmax)):
                #fill the scan list with particles that are within the distance
                #   of the given itterated location on the scan of the grid
                ScanList = [p for p in particleData if (vDistance(np.array([p.x, p.y]), np.array([j * self.spaceScaling, i * self.spaceScaling])) <= p.material.value[1] )]
                #if the Scanlist is filled with any information print
                if ScanList:
                    #print the symbol for the given material at the begining
                    #   of the scanlist (higher priority)
                    print(ScanList[0].material.value[-1], end= "")
                #if there is no objects within the grid distance print a space
                else:
                    #print empty space
                    print("   ", end="")
            #print a verticle border
            print("|| ")
        #print a horizontal border for the bottom
        print("===" * (self.xmax + 2))
        #itterate through the list of particles and print their properties
        for p in particleData:
            #print the properties
            print(p.__dict__)
            #print function for place holding
            #print('',end='')
        ##----------------------------------------------------------------