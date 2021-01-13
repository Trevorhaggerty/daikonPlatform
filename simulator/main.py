#libraries

#local imports
from mathTools import *
from camera import *
from simulation import *


#global Variables, Objects, and Functions -------------------------------
#this is the boolean value to determine if the simulation should continue
simActive = True
#define the main function
def main():
    #create the simulation object
    sim = Simulation(.5, [2, 2])
    #create the camera object
    camera = Camera(15, 30, 0.1)
    #start the simulations loop
    while simActive:
        #call the camera function to print to screen
        camera.present(sim.particles)
        #call the simulations update function
        sim.update()
#call the main function
main()