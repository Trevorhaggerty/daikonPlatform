#libraries
import time, random, os, sys
import numpy as np

#local imports
from particles import *

#----------------------------------------------------------------------------------------
#Simulation is a class to hold all the information for the simulation
#   
#
#
#
class Simulation():
    #this function is called upon creation
    def __init__(self, timeScale, particleData):
        #create an empty list to hold all of the particles in the simulation
        self.particles = [] 
        #initialize the tick at 0
        self.tick = 0
        #set the time scale (dertimines the speed of the simulation)
        self.timeScaling = timeScale # this is in seconds
        #if there are particles present
        if particleData:
            #itterate through initial particleData (each type)
            for j in range(len(particleData)):
                #itterate a number of times based on the integer in the particleData list
                for i in range(particleData[ j ]):
                    #empty/initialize an empty object
                    newparticle = {}
                    #if the list is at the second number
                    if j == 1 :
                        #create an air particle at a random location
                        newparticle = Particle(random.randint(0, 10), random.randint(0, 10), Material.AIR)
                    #if the list is on the first number
                    elif j == 0:
                        #create a sand particle at a random location 
                        newparticle = Particle(random.randint(0, 10), random.randint(0, 10), Material.SAND)                         
                    #append the newly generated particle to the particle list
                    self.particles.append(newparticle)
    #this function is called to update the state of the simulation
    def update(self):

        #itterate through the list of particles and represent the particle as p
        for p in self.particles:
            #update the particles verticle velocity with an impulse to represent gravity
            p.yVelocity += 9.9 * p.material.value[0] * self.timeScaling

        #itterate through the list of particles and represent the particle as p
        for p in self.particles:
            #apply the velocities to the location of the particles
            p.y += p.yVelocity 