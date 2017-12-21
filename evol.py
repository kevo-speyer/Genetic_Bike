#!/usr/bin/env python
import math
import numpy as np
from bike import Bike

bike1 = Bike()

def new_bike(bike_list):

     #sorting the scores: 
     #for x in xrange(0,len(bike_list)):
     #    for i in xrange(x+1,len(bike_list)):
     #        if bike_list[i].score > bike_list[x].score:
     #            bike_list[i],bike_list[x] = bike_list[x],bike_list[i] 
     #bike_list = sorted(bike_list, key=lambda bike1: bike1.score)

     #select %20 of all the bikes:
     nselect = int(len(bike_list)*0.20)
     
     new_bike_list = []
     for ibike in range(0,nselect-1):
        for jbike in range(ibike+1,nselect):
             crossover(bike_list[ibike],bike_list[jbike],bike_new)
             new_bike_list.append(bike1.bike_new)
     return new_bike_list 

def crossover(bike1,bike2,bike3):
    for i in range(4):
        new_bike_mass[i] = (bike1.bike_mass[i]+bike2.bike_mass[i])/2.0
        new_bike_pos[i][0] = bike1.init_pos[i][0]+(bike2.init_pos[i][0]-bike1.init_pos[i][0])*np.random.random()
        new_bike_pos[i][1] = bike1.init_pos[i][1]+(bike2.init_pos[i][1]-bike1.init_pos[i][1])*np.random.random()
    new_k_sp = (bike1.k_sp+bik2.k_sp)/2.0
    gen_sp_bike(new_bike_pos,new_bike_mass,new_k_sp)
    return bike3
