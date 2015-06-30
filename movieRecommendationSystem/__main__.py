import data
import functions 



person1 = data.critics.keys()[2]
person2 = "Toby"


#print functions.pearsonDistance(data.critics,person1,person2)
#print functions.mostSimilar(data.critics,"Toby")

#print functions.getListOfMovies(data.critics)

print functions.getRecommendations(data.critics,person2)   #how much will one user like a particular  movie


productData = functions.flipPersonToMovie(data.critics)



print functions.mostSimilar(productData,"Superman Returns")   #Find similar movies



print functions.getRecommendations(productData,"Just My Luck") #Out of the people Who havent seen the movie Who will like this movie ?


#how much will one user like a particular  movie
#Find similar movies
#Out of the people Who havent seen the movie Who will like this movie ?