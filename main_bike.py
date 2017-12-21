#!/usr/bin/env python
###### MAIN BIKE PROGRAM ###########
import numpy as np
from bike_gr_int import bk_gd_int 
from floor import Floor   	    
from bike  import Bike
from solver import *
from grav_force import grav_force
from animation import *
from score import score
from evol import new_bike

VISUALIZATION = True 

def main():
    gen_nr = 4 #NUMBER OF GENERATIONS
    #First generate the Ground
    ground = Floor() # Create the ground   
    ground.gen_coor() # Generate coordinates of the ground
    ground.gen_versors() # Generate local versors in all the ground segments
    

    #BEGIN loop to create bikes    
    bike_list = []
    nbike = 3
    i = 0
    while (i<nbike):
        i=i+1
        bike1 = Bike()
        bike1.gen_rand_bike()
#        RuKu4(bike1,ground)
        Euler(bike1,ground)
        score(bike1)
        bike_list.append(bike1)
        #print bike_list[i].bike_mass
    	if VISUALIZATION:
#	    print bike_test.traj
            render = Render(ground, bike1, 1)
            ani = animation.FuncAnimation(render.fig, render.animate, init_func = render.init_line, frames = render.nframes, interval = 5.0, repeat = False, blit = True)
	    plt.show() 
#        ...ani.save('bike_motion.mp4', writer = 'mencoder', fps = 15)


   #sort the bikes according to the distance passed by each one
    bike_list = sorted(bike_list, key=lambda bike1: bike1.score)

    new_list = new_bike(bike_list) 
    #END bike loop
    for generation in range(gen_nr):
        bike_list = []
        
        for bike1 in new_list:
            Euler(bike1,ground)
            score(bike1)
            bike_list.append(bike1)
            #print bike_list[i].bike_mass
            if VISUALIZATION:
    #           print bike_test.traj
                render = Render(ground, bike1, 1)
                ani = animation.FuncAnimation(render.fig, render.animate, init_func = render.init_line, frames = render.nframes, interval = 1.0, repeat = False, blit = True)
                plt.show()
    #        ...ani.save('bike_motion.mp4', writer = 'mencoder', fps = 15)
    
    
       #sort the bikes according to the distance passed by each one
        bike_list = sorted(bike_list, key=lambda bike1: bike1.score)
        
        new_bike(bike_list)

     
    

if __name__ == '__main__':
    main()



