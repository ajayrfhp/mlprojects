import matplotlib.pyplot as p
import numpy 
from numpy import *
from kmeans import *
data = [[1,2,3],[2,2,3],[3,2,4],[2,3,5],[4,2,1]]


data = numpy.array(data)

centers = numpy.array(buildModel(data,3))

print centers


	
'''
p.plot(data[:,0],data[:,1],'.')
p.plot(centers[:,0],centers[:,1],'bo')		
p.axis([0, 5, 0,5])
p.show()
'''






