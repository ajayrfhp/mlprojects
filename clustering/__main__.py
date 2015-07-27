import matplotlib.pyplot as p
import numpy 
from numpy import *
from kmeans import *
data = [[1,2],[2,2],[3,2],[2,3],[4,2]]


data = numpy.array(data)

centers = numpy.array(buildModel(data,2))



	

p.plot(data[:,0],data[:,1],'.')
p.plot(centers[:,0],centers[:,1],'bo')		
p.axis([0, 5, 0,5])
p.show()







