import matplotlib.pyplot as p
import numpy 
from numpy import *
from kmeans	 import *
import numpy as np
from PIL import Image
import sys

def rgb_to_hex(rgb):
  r = rgb[0]
  g = rgb[1]
  b = rgb[2]
  return '#%02X%02X%02X' % (r,g,b)



#data = [[1,2],[2,2],[3,2],[2,3],[4,2]]

#data = [[[1,2]],[[2,2]],[[3,2]],[[2,3]],[[4,2]]]
#data = numpy.array(data)


#print data.shape

img = Image.open(sys.argv[1])
data = np.array(img)

data2 = []

for i in range(data.shape[0]):
	for j in range(data.shape[1]):

		data2.append(data[i][j])

data2 = numpy.array(data2)
print data2.shape


#data = [[[1,2,3]],[[2,27,42]],[[3,2,1]],[[240,250,3]],[[3,2,1]],[[3,2,1]],[[3,2,1]],[[3,2,1]],[[3,2,0]],[[2,3,0]],[[4,2,5]]]






centers = numpy.array(buildModel(data2,3))


for center in centers:

	print rgb_to_hex(center)

#print centers
#print centers.shape




	
'''
p.plot(data[:,0],data[:,1],'.')
p.plot(centers[:,0],centers[:,1],'bo')		
p.axis([0, 5, 0,5])
p.show()
'''




