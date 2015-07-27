from math import sqrt

def pearson(v1,v2):
	sum1 = sum(v1)
	sum2 = sum(v2)

	sum1Squares = sum([v**v for v in v1])
	sum2Squares = sum([v**v for v in v2])

	productsum = sum([v1[i]*v2[i] for i in range(len(v1))])


	num = productsum - ((sum1*sum2)/len(v1))
	den = sqrt((sum1Squares - (sum1*sum1)/len(v1)) * (sum2Squares - (sum2*sum2)/len(v2)) )
	if(den == 0):
		return 0
	pearson =   (num / den)
	return pearson


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


def getClosestFeatures(data):
	data = np.tril(data)
	maxValue = np.tril(data).max()
	indices = [((i,j) if data[i][j]==maxValue else (-1,-1) ) for j in range(data.shape[1]) for i in range(data.shape[0])  ]
	indices = filter(lambda a:a!=(-1,-1),indices)
 	index = indices[0]
 	return index
