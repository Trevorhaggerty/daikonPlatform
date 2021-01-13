#libraries


#local imports

from mathTools import *
from camera import *
from simulation import *


#global Variables, Objects, and Functions -------------------------------
#this is the boolean value to determine if the simulation should continue
simActive = True

def main():
    sim = Simulation([2,2])
    camera = Camera(10,10,0.1)
    simActive = True
    while simActive:
        camera.present(sim.particles)
        sim.update()
main()