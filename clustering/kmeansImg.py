import numpy 
from numpy import *
import time 
import matplotlib.pyplot as p

## NOT GENERIC CODE 

def euclideanDistance(p1,p2):
	distance = 0

	for i in range(p1.shape[1]):
		distance += abs(p1[0][i]-p2[0][i])

	return distance


def buildModel(data,k):
	points = {}
	for i in range(len(data)):
		points[i] = data[i]


	
	centres = data[0:k]




	while(1):
			# START WITH RANDOM CENTRES,COMPUTE SHORTEST CENTRE FOR EACH DATA POINT


		pointCenters = {}
		
		for i in points.keys():
			minDistance = 999999999999999999
			thisCenter = -1
			for center in centres:
				thisDistance = euclideanDistance(points[i],center)

				if(thisDistance < minDistance):
					minDistance = thisDistance
					thisCenter = center
		
		
					#print "hi"
				#print str(thisDistance) + str(thisCenter) 
						
			pointCenters[i] = thisCenter
		

		



			
		
		# point Centers contain the shortest centre from each point
		newCenters = []




		for center in centres:
			cnt = 0
			thisCenter = numpy.zeros((pointCenters[pointCenters.keys()[0]].shape))
			for key in points.keys():
				
				if(numpy.array_equal(pointCenters[key],center)):
					
					for j in range(points[key].shape[1]):

						thisCenter[0][j] += points[key][0][j]



				cnt += 1	

			thisCenter /= cnt		

			newCenters.append(thisCenter)	




		if(numpy.array_equal(newCenters,centres)):
			break


		

		
	




		centres = newCenters
		'''
		p.clf()
		centres = numpy.array(centres)	
		p.plot(data[:,0],data[:,1],'.')
		p.plot(centres[:,0],centres[:,1],'bo')		
		p.axis([0, 5, 0,5])
		p.show()		
		time.sleep(0.5)
		'''

		

	return centres




	
	## determined nearest centeres 

	## To do ,for each cluster find new center by taking mean of all points in that cluster


	## repeat algorithm until new cluster center == old cluster center