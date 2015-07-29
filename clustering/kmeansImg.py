import numpy 
from numpy import *
import time 
import matplotlib.pyplot as p

## NOT GENERIC CODE 

def euclideanDistance(p1,p2):
	distance = 0
	distance = sum(abs(p1 - p2))

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
		newCenter = []
		for center in centres:
			#print "-----------------------------"
			#print center
			thisCenter = numpy.zeros(points[points.keys()[0]].shape)
			

			cnt = 0
			for key in pointCenters.keys():

				if(numpy.array_equal(pointCenters[key],center)):
					#print points[key]
					cnt +=1

					thisCenter += points[key]
			
			
			


			thisCenter[0] = [ float(x) for x in thisCenter[0] ]		
					
			thisCenter /= cnt


			newCenter.append(thisCenter)



		
		if(numpy.array_equal(newCenter,centres)):
			break

		centres = newCenter	
		p.clf()
		centres = numpy.array(centres)
		'''	
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