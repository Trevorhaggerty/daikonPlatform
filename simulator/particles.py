from enum import Enum
import numpy as np




#Material enums are used to hold the properties of a particle based on
#   the material.
#NAME OF THE MATERIAL = [mass, volume, "symbol to be represented by"]
class Material(Enum):
    AIR = [0.1, 5.0, " - "] #air should have low mass and high volume
    SAND = [1.0, 1.5, "888"] #sand should have mid mass and low volume

#the particle class is what the game world and al the objects with in it will be made from
class Particle():
    
    def __init__(self, x, y, material):
        #set the x location from the given information
        self.x = x
        #set the y location from the given information
        self.y = y
        #set the velocity of the object in the x dimension
        self.xVelocity = 0 #the initial is set to 0
        #set the velocity of the object in the y dimension
        self.yVelocity = 0 #the initial is set to 0
        #set the from materials properties with the given information
        self.material = material

