
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
	
	for i in points.keys():
		minDistance = 999999999999999999
		thisCenter = -1
		for center in centres:
			thisDistance = euclideanDistance(points[i],center)
			if(thisDistance < minDistance):
				thisDistance = minDistance
				thisCenter = center

		pointCenters[i] = thisCenter
	print points
	print pointCenters		