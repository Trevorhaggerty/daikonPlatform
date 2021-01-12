#libraries
from enum import Enum
import time, random, os, sys
import numpy as np

#local imports

from mathTools import *
from camera import *


#global Variables, Objects, and Functions -------------------------------
#this is the boolean value to determine if the simulation should continue
simActive = True

#NAME OF THE MATERIAL = [mass, volume, "symbol to be represented by"]
class Material(Enum):
    AIR = [0.1, 5.0, " - "]
    SAND = [1.0, 1.5, "888"]



#the particle class is what the game world and al the objects with in it will be made from
class Particle():
    def __init__(self, x, y, material):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.yVelocity = 0
        self.material = material



#
class Simulation():
    def __init__(self, particleData):
        
        self.particles = [] 
        
        self.timeD = 0
        self.displayD = 0

        self.timeHolder = time.time()   
        self.frameRate = 0              
        self.timeScaling = 0.00001            # this is in seconds

        self.spaceScaling = 1.5           # 1 is a meter


        if particleData:
            for p in range(len(particleData)):
                for i in range(particleData[p]):
                    newparticle = {}
                    if p == 1 :
                        newparticle = Particle(random.randint(0,self.xmax), random.randint(0,self.ymax), Material.AIR)
                    elif p == 0:
                        newparticle = Particle(random.randint(0, self.xmax), random.randint(0,self.ymax), Material.SAND)
                                 
                    self.particles.append(newparticle)

    def update(self):
        #apply for gravity
        for p in self.particles:
            p.yVelocity += 9.9 * p.material.value[0] * self.timeScaling

        #move the particle
        for p in self.particles:
            p.y += p.yVelocity

def main():
    sim = Simulation()
    camera = Camera()
    sim.present()
    simActive = True
    while simActive:
        camera.present(sim.particles)
        sim.update()
main()