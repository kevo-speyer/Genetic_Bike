#!/usr/bin/env python
import numpy as np

#from dist_fl_bk import get_gr_bk_dist 
from floor import Floor   	    
from bike  import Bike
from solver import RuKu4

def main():
    ground = Floor() # Create the ground   
    ground.gen_coor() # Generate coordinates of the ground
    fl_coor = ground.coor  # fl_coor are the coordinates of the ground (numpy array)
#    print fl_coor
    
    ground.gen_versors() # Generate local versors in all the ground segments
    par_ver = ground.par_ver #par_ver has all the parallel versos of the segments
    nor_ver = ground.nor_ver #par_ver has all the parallel versos of the segments
   
#    print par_ver
    
    bike_test = Bike() # Initiate Bike object
    bike_test.gen_rand_bike() # Random parameters

    #EXAMPLE
#    l0_ww = bike_test.l0_ww #  
#    print l0_ww

# Test Distance routine
#    res = bk_gd_int(bike_test,ground)
#    print res
#    print w1_pos[0],w1_pos[1]
    RuKu4(bike_test,ground)
    bike_new = Bike()
    bike_new.gen_sp_bike(bike_positions,bike_mass,k_sp)

if __name__ == '__main__':
    main()

