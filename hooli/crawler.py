import urllib2
from bs4 import BeautifulSoup
from helpers import rewrite
f = open('urls.txt','w')



class crawler():
	cnt = 0
	linkMap = {}
	
	def init(self):
		self.cnt = 0
		self.linkMap = {}
	def crawl(self,url):
		if(url == None):
			return
		response = urllib2.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html,'html.parser')
		
		links = soup.find_all('a')
		for link in links:
			print self.cnt,url,link.get('href')
			parsedUrl = rewrite(url,link.get('href'))
			if(parsedUrl != None):
				if(parsedUrl.count('pdf') != 0 ):
					return
			if( parsedUrl not in self.linkMap.keys()):
				if( self.cnt > 1000):
					return 
				self.cnt += 1
				self.linkMap[parsedUrl] = 1
				
				try:
					self.crawl(parsedUrl)
				#except  urllib2.HTTPError :	
				#f.write(str(link.get('href'))+'\n')
				#print 'error in ',parsedUrl
				#print link.get('href'),url,self.cnt,parsedUrl
				except:
					zxzcx = 1
					

		return 		
