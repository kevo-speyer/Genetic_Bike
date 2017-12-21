import numpy as np

def score(bike):
	#Give the object bike a score bike.score, analizing bike.traj
	puntaje = np.zeros(4)
	for i in range(4):
	    puntaje[i] = np.amax(bike.traj[:,2*i+1], axis=0) 	# Get maximum  x coordinate of each wheel/head
#	    print puntaje[i]
	
	puntaje_f = np.amax(puntaje, axis=0)
	bike.score = puntaje_f #Set bike score
#	print puntaje_f 	

	#By Emir, obsolete now
	#loop=0
	#max_x=max(bike.traj[0,1],bike.traj[0,3],bike.traj[0,5],bike.traj[0,7])
	#MAX_X=[bike.traj[0,1],bike.traj[0,3],bike.traj[0,5],bike.traj[0,7]]
	#for t in bike.traj[:,0]:
	#	if max_x<max(bike.traj[loop,1],bike.traj[loop,3],bike.traj[loop,5],bike.traj[loop,7]):
	#		MAX_X=[bike.traj[loop,1],bike.traj[loop,3],bike.traj[loop,5],bike.traj[loop,7]]
	#	loop+=1
	#bike.score=sum(MAX_X)/4
