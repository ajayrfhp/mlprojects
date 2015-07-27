import matplotlib.pyplot as p
import numpy 
from numpy import *
from pylab import *
from kmeans import *
data = [[1,2],[2,2],[3,2],[2,3],[4,2]]
plot(data,'.')

data = numpy.array(data)



buildModel(data,2)

#p.show()



