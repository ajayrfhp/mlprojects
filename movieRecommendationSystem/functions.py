from math import sqrt
def similarityDistance(data,person1,person2):
	disimiliarFlag = True
	for movie1 in data[person1]:
		if movie1 in data[person2]:
			disimiliarFlag = False
	
	if(disimiliarFlag):
		return 0

	distance = 0
	for movie1 in data[person1]:
		if movie1 in data[person2]:
			distance += (data[person1][movie1]-data[person2][movie1])*(data[person1][movie1]-data[person2][movie1])
	return 1/distance
					
def mostSimilar(data,person1):
	persons = data.keys()
	scores = {}
	for person in persons:
		if(person!=person1):
			thisDistance = pearsonDistance(data,person1,person)
			scores[person] = thisDistance

	sorted(scores.items(),key=lambda scores:scores[1])		
	
	return scores		


def pearsonDistance(data,person1,person2):
	disimiliarFlag = True
	for movie1 in data[person1]:
		if movie1 in data[person2]:
			disimiliarFlag = False

	si={}
	for item in data[person1]:
		if item in data[person2]: 
			si[item]=1
	n=len(si)		
		

	##########I DONT UNDERSTAND THIS METRIC :P . THE INTUITION JUST ABSOLUTELY NOT THERE .PEOPLE SAY IT WORKS  :P

	if(disimiliarFlag):
		return 0

	sum1 = sum([data[person1][movie] for movie in si])
	sum2 = sum([data[person2][movie] for movie in si])
	
	
	sumSquares1 = sum([data[person1][movie]*data[person1][movie] for movie in si])
	sumSquares2 = sum([data[person2][movie]*data[person2][movie] for movie in si])

	pSum = sum([data[person2][movie]*data[person1][movie] for movie in si])

	num = pSum -(sum1*sum2)/n
	den=sqrt((sumSquares1-pow(sum1,2)/n)*(sumSquares2-pow(sum2,2)/n))	
	if(den==0): return 0
	return num/den

	###NOT UNDERSTANDING PART ENDS HERE :P


def getListOfMovies(data):
	listOfCritics = data.keys()
	listOfMovies = []
	for critic in listOfCritics:
		for movie in data[critic].keys():
			listOfMovies.append(movie)

	listOfMovies = list(set(listOfMovies))		
	return listOfMovies		


def flipPersonToMovie(data):
	movies = getListOfMovies(data)
	result = {}
	for movie in movies:
		thisResult = {}
		for person in data.keys():
			if movie in data[person].keys():
				thisResult[person] = data[person][movie]
		result[movie] = thisResult
	return result			




def getRecommendations(data,person):
	movies = getListOfMovies(data)
	unWatchedMovies = []
	for movie in movies:
		if movie not in data[person].keys():
			unWatchedMovies.append(movie)
	


	movieRecommendations = {}
	for movie in unWatchedMovies:
		cnt = 0
		thisMovieRating = 0
		for person1 in data.keys():
			similarityIndex = pearsonDistance(data,person,person1)
			if(similarityIndex<0):
				break
			
			if(person1!=person and movie in data[person1].keys() ):
				#print str(similarityIndex)+str(person1)
				thisMovieRating += similarityIndex*data[person1][movie]
				cnt += similarityIndex
		thisMovieRating = thisMovieRating /cnt			
		movieRecommendations[movie] = thisMovieRating



	return movieRecommendations	 
	

