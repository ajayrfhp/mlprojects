import numpy 
from numpy import *

def euclideanDistance(p1,p2):
	distance = 0
	for dimension  in range(p1.shape[0]):
		distance += abs(p1[dimension] - p2[dimension])
	
	return distance


def buildModel(data,k):
	points = {}
	for i in range(len(data)):
		points[i] = data[i]

	centres = data[0:k]
	pointCenters = {}
	newCenters = []
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
	
		newCenters.append(tuple(thisCenter))
	
	print newCenters		

	newCenters = list(set(newCenters))	
	
	print newCenters
	print centres
	
	## determined nearest centeres 

	## To do ,for each cluster find new center by taking mean of all points in that cluster


	## repeat algorithm until new cluster center == old cluster center