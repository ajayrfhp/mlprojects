import pandas 
import numpy
import copy
import random
import matplotlib.pyplot as plt 
import math


def tanmato(v1,v2):
	intersections = 0
	unions = 0

	for i in range(v1.shape[0]):
		if(v1[i] == 1 and v2[i] == 1):
			intersections += 1
		if(v1[i] == 1 or v2[i] == 1):
			unions += 1
	if(unions == 0 and intersections ==0):
		return 1

	return 1 - (float(intersections)/unions)		
			


def correct(a,positionX,positionY,sampleData,finalDistance):
	for z in range(100l):
		for i in range(sampleData.shape[0]):
			result = resultantForce(i,positionX,positionY,finalDistance,sampleData)
			
			positionX[i] += a*result[0]
			positionY[i] += a*result[1]

	return (positionX,positionY)

data = pandas.read_table('blogdata.txt')

transformedData = copy.copy(data)
transformedData.Item = map(lambda x:data[data.Item==x].index.item(),data.Item)

#sampleData = numpy.array([[0,1,0,0,0],[0,1,0,0,1],[0,0,0,1,0],[1,1,1,1,1],[1,1,0,1,1]])
sampleData = numpy.array([[1,0,1,1,1],[1,1,1,1,1]])

## compute final distance

## find current distance, computer how much point needs to move in each axis. find error and move with a step size

plt.plot(positionX.values(),positionY.values(),'o')
plt.show()