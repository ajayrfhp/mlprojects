import feedparser
import re



def getFeatures(d):
	title = d['feed']['title']
	words = getWords(html)
	wordCount = {}

	for word in words:
		if word in wordCount.keys():
			wordCount[word] += 1
		else:
			wordCount[word] = 1	 
	
	return title,wordCount	


def getWords(html):
	txt=re.compile(r'<[^>]+>').sub('',html)
	words=re.compile(r'[^A-Z^a-z]+').split(txt)
	html = [word.lower( ) for word in words if word!='']
	return html
