import data
import functions 



person1 = data.critics.keys()[2]
person2 = "Toby"


#print functions.pearsonDistance(data.critics,person1,person2)

#print "Most similar critcs "
#print functions.mostSimilar(data.critics,"Toby")

#print " "

#print "Product Recommendations for a user"
#print functions.getRecommendations(data.critics,person2)   #how much will one user like a particular  movie

#print " "

productData = functions.flipPersonToMovie(data.critics)

#print "Finding similar movies "
#print functions.mostSimilar(productData,"Superman Returns")   #Find similar movies

#print " "

#print "Finding user Recommendations for a product"
#print functions.getRecommendations(productData,"Just My Luck") #Out of the people Who havent seen the movie Who will like this movie ?

#print " "


#print "Computing Item Similarity"
itemSimilarity = functions.computeItemSimilarities(productData)




print "Item Based Filtering for Recommendations"
print functions.itemBasedFiltering(data.critics,"Toby",itemSimilarity)