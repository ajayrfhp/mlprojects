import feedparser
import re

def generateFeed(url):
	feed = feedparser.parse(url)
	return getFeatures(feed)

def getFeatures(feed):
	title = []
	try :
		title = feed.feed.title
		
		html = feed.entries[0].summary
		words = getWords(html)
		wordCount = {}

		for word in words:
			if word in wordCount.keys():
				wordCount[word] += 1
			else:
				wordCount[str(word)] = 1	 
		
		return title,wordCount

	except AttributeError :
		raise AttributeError	


def getWords(html):
	txt=re.compile(r'<[^>]+>').sub('',html)
	words=re.compile(r'[^A-Z^a-z]+').split(txt)
	html = [word.lower( ) for word in words if word!='']
	return html
