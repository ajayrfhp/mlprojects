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
	pearson =  1 - (num / den)
	return pearson
