import numpy as np
from numpy import linalg as LA
from floor import Floor
from bike  import Bike
g = 9.8

def grav_force(bike):
    """
    Get bike properties and compute the accelaration of each object and set back to acc properties of bike. 
    Take care the function don't have any history for the location and calling it may change value!
    """
    bike.bike_acc[:,1] = -g#Get wheel's position

