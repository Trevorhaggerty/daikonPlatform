
import time, random, os, sys
import numpy as np

#local imports
from particles import *


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
                        newparticle = Particle(random.randint(0, 10), random.randint(0, 10), Material.AIR)
                    elif p == 0:
                        newparticle = Particle(random.randint(0, 10), random.randint(0, 10), Material.SAND)
                                 
                    self.particles.append(newparticle)

    def update(self):
        #apply for gravity
        for p in self.particles:
            p.yVelocity += 9.9 * p.material.value[0] * self.timeScaling

        #move the particle
        for p in self.particles:
            p.y += p.yVelocity