from enum import Enum
import numpy as np



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

