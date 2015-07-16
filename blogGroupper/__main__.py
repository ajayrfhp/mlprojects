import feedparser
import re
from  parser import *
import json






data = {}

def generateFeatures():
	with open("blogGroupper/feedList.txt","r") as f:	
		urls = f.readlines()
		for url in urls:
			try :
				title,featureVector =  generateFeed(url)
				data[title] = featureVector
				
			except AttributeError:
				continue
			
			print urls.index(url)
			
	with open ('blogGroupper/feature.json','wb') as f2:
		json.dump(json.dumps(data),f2)



with open('blogGroupper/feature.json') as f:
     data = json.loads(json.load(f))


print data.keys()
