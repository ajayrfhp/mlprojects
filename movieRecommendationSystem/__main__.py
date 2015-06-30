import data
import functions 



person1 = data.critics.keys()[2]
person2 = "Toby"


#print functions.pearsonDistance(data.critics,person1,person2)
#print functions.mostSimilar(data.critics,"Toby")

#print functions.getListOfMovies(data.critics)

#print functions.getRecommendations(data.critics,person2)


productData = functions.flipPersonToMovie(data.critics)



print functions.mostSimilar(productData,"Superman Returns")



