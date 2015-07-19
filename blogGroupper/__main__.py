import feedparser
import re
from  parser import *
import json
from functions import *
from math import sqrt

'''
REFERENCE : http://www.econ.upf.edu/~michael/stanford/maeb7.pdf

INTUITION : 
	Generate simillarity matrix for all features 
	Each feature is a  node .
	choose 2 closest features ,create their parent. 
	The feature vector of parent  is combined node is the mean of the 2 contributing nodes.
	Repeat untill u get all nodes are connected and u get a single root.



'''





data = {}



with open('feature.json') as f:
     data = json.loads(json.load(f))





data = [[0,0.5000,0.4286,1.0000,0.2500,0.6250,0.3750],
 [0.5000,0,0.7143,0.8333,0.6667,0.2000,0.7778],
 [0.4286,0.7143,0,1.0000,0.4286,0.6667,0.3333],
 [1.0000,0.8333,1.0000,0,1.0000,0.8000,0.8571],
 [0.2500,0.6667,0.4286,1.0000,0,0.7778,0.3750],
 [0.6250,0.2000,0.6667,0.8000,0.7778,0,0.7500],
 [0.3750,0.7778,0.3333,0.8571,0.3750,0.7500,0]]


 
 

 data = numpy.array(data)