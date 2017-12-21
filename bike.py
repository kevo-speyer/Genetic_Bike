import numpy as np

class Bike(object):
    """
    Bike has the properties of all its components: Wheels, Masses, positions, vel, Rad, k_spring
    bike.bike_mass np array from 0 to 3, index is for object  
    bike.bike_rad  np array from 0 to 3, index is for object
    bike.bike_pos np array with 2 indices, first index is object, second index is direction
    bike.bike_pos  np array with 2 indices, first index is object, second index is direction
    bike.bike_vel   np array with 2 indices, first index is object, second index is direction
    bike.bike_l0 is a np matrix indices are for objects (wheel or mass)
    bike.k_sp spring constant
    NEW : Bike now has a matrix for positions, velocities and acceleration and l0
          For masses and radius there are arrays.
    IMPORTANT : FOLLOW THE INDEX CONVENTION.    0 is mass1
						1 is mass2
						2 is wheel1
						3 is wheel2
    """

    def __init__(self):
	# Define Cinematic magnitudes
  	self.m1_pos = np.zeros(2) 
	self.m2_pos = np.zeros(2)	
  	self.w1_pos = np.zeros(2)
	self.w2_pos = np.zeros(2)

  	self.m1_vel = np.zeros(2) 
	self.m2_vel = np.zeros(2)	
  	self.w1_vel = np.zeros(2)
	self.w2_vel = np.zeros(2)
	#NEW: all velocities in one matrix
	self.bike_vel = np.array([self.m1_vel, self.m2_vel, self.w1_vel, self.w2_vel])

 	self.m1_acc = np.zeros(2)
	self.m2_acc = np.zeros(2)	
  	self.w1_acc = np.zeros(2)
	self.w2_acc = np.zeros(2)
	#NEW: all accelerations  in one matrix
	self.bike_acc = np.array([self.m1_acc, self.m2_acc, self.w1_acc, self.w2_acc])

	#Dinamic properties
   	self.m1_mass = 0. 
	self.m2_mass = 0.	
  	self.w1_mass = 0.
	self.w2_mass = 0.

	self.k_sp = 0. # Spring constant
	
	self.l0_mm   = 0.
	self.l0_ww   = 0.
	self.l0_w1m1 = 0.  
	self.l0_w1m2 = 0.
	self.l0_w2m1 = 0.
	self.l0_w2m2 = 0.
 	
	# Geometric Properties
 	self.w1_rad = 0. 
	self.w2_rad = 0. 
  	self.m1_rad = 0.
	self.m2_rad = 0.
	
	

    def gen_rand_bike(self):
	#This method should generate a random bike
	box_size = 5. 
	y_skin = 5.
  	x_skin = 10.
	mass_handicap = 0.1
	sprng_hdcp = 250. #ORI 50.
	#sprng_hdcp = 0.
	mass_mag = 5.
	sprng_mag = 50.
	w_den = 0.5
	m_den = 1.0
			
	#Set random intial positions
	self.m1_pos[0] = x_skin + box_size*np.random.random()  	
        self.m2_pos[0] = x_skin + box_size*np.random.random() 
        self.w1_pos[0] = x_skin + box_size*np.random.random() 
        self.w2_pos[0] = x_skin + box_size*np.random.random() 
	
	self.m1_pos[1] = y_skin + box_size*np.random.random()  	
        self.m2_pos[1] = y_skin + box_size*np.random.random() 
        self.w1_pos[1] = y_skin + box_size*np.random.random() 
        self.w2_pos[1] = y_skin + box_size*np.random.random()
	#NEW: all positions in one matrix
	self.bike_pos = np.array([self.m1_pos, self.m2_pos, self.w1_pos, self.w2_pos])
	#SAVE INITIAL POSITIONS
        self.init_pos = self.bike_pos


	#Set spring's natural length from the initial positions
	self.l0_mm = np.linalg.norm(self.m1_pos-self.m2_pos)
        self.l0_ww = np.linalg.norm(self.w1_pos-self.w2_pos)
        self.l0_w1m1 = np.linalg.norm(self.w1_pos-self.m1_pos)
        self.l0_w1m2 = np.linalg.norm(self.w1_pos-self.m2_pos)
        self.l0_w2m1 = np.linalg.norm(self.w2_pos-self.m1_pos) 
        self.l0_w2m2 = np.linalg.norm(self.w2_pos-self.m2_pos)
        #NEW: all l0 in one matrix
        self.bike_l0 = np.matrix([ [0., self.l0_mm, self.l0_w1m1, self.l0_w2m1], [self.l0_mm, 0., self.l0_w1m2, self.l0_w2m2], [self.l0_w1m1, self.l0_w1m2, 0., self.l0_ww], [self.l0_w2m1, self.l0_w2m2, self.l0_ww, 0.] ])

	#Set random intial masses
	self.m1_mass = mass_handicap + mass_mag*np.random.random()  
        self.m2_mass = mass_handicap + mass_mag*np.random.random() 
        self.w1_mass = mass_handicap + mass_mag*np.random.random() 
        self.w2_mass = mass_handicap + mass_mag*np.random.random()
	#NEW: all masses in one matrix
	self.bike_mass = np.array([self.m1_mass, self.m2_mass, self.w1_mass, self.w2_mass])

	
	#Set intial Radius, from masses and densities
	self.m1_rad =  np.sqrt(	self.m1_mass / ( 3.1415926 * m_den) ) 
        self.m2_rad =  np.sqrt( self.m2_mass / ( 3.1415926 * m_den) )
        self.w1_rad =  np.sqrt( self.w1_mass / ( 3.1415926 * w_den) )
        self.w2_rad =  np.sqrt( self.w2_mass / ( 3.1415926 * w_den) )
	#NEW: all radius in one matrix
	self.bike_rad = np.array([self.m1_rad, self.m2_rad, self.w1_rad, self.w2_rad])

	#Set spring constant
	self.k_sp = sprng_hdcp + sprng_mag * np.random.random()
        
    def gen_sp_bike(self,new_bike_pos,new_bike_mass,new_k_sp):
	#This method should generate a specific bike, given by the genetic algorithm 
	self.k_sp = k_sp
  	self.bike_vel = np.array([np.zeros(2),np.zeros(2),np.zeros(2),np.zeros(2)])
   	self.bike_acc = np.array([np.zeros(2),np.zeros(2),np.zeros(2),np.zeros(2)])
        self.bike_pos = new_bike_pos
	#SAVE INITIAL POSITIONS
        self.init_pos = new_bike_pos
	w_den = 0.2
	m_den = 0.8
		
	self.bike_mass = new_bike_mass
	self.k_sp = new_k_sp     	

	#Set intial Radius, from masses and densities
	self.m1_rad =  np.sqrt(	self.m1_mass / ( 3.1415926 * m_den) ) 
        self.m2_rad =  np.sqrt( self.m2_mass / ( 3.1415926 * m_den) )
        self.w1_rad =  np.sqrt( self.w1_mass / ( 3.1415926 * w_den) )
        self.w2_rad =  np.sqrt( self.w2_mass / ( 3.1415926 * w_den) )
	#NEW: all radius in one matrix
	self.bike_rad = np.array([self.m1_rad, self.m2_rad, self.w1_rad, self.w2_rad])

	#Set spring's natural length from the initial positions
	self.l0_mm = np.linalg.norm(self.m1_pos-self.m2_pos)
        self.l0_ww = np.linalg.norm(self.w1_pos-self.w2_pos)
        self.l0_w1m1 = np.linalg.norm(self.w1_pos-self.m1_pos)
        self.l0_w1m2 = np.linalg.norm(self.w1_pos-self.m2_pos)
        self.l0_w2m1 = np.linalg.norm(self.w2_pos-self.m1_pos) 
        self.l0_w2m2 = np.linalg.norm(self.w2_pos-self.m2_pos)
        #NEW: all l0 in one matrix
        self.bike_l0 = np.matrix([ [0., self.l0_mm, self.l0_w1m1, self.l0_w2m1], [self.l0_mm, 0., self.l0_w1m2, self.l0_w2m2], [self.l0_w1m1, self.l0_w1m2, 0., self.l0_ww], [self.l0_w2m1, self.l0_w2m2, self.l0_ww, 0.] ])

