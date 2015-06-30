import data
import functions 
import model



person1 = data.critics.keys()[2]
person2 = "Toby"


#print functions.pearsonDistance(data.critics,person1,person2)
#print functions.mostSimilar(data.critics,"Toby")

#print functions.getListOfMovies(data.critics)

print functions.getRecommendations(data.critics,person2)