import feedparser
import re
import parser

url = 'http://feeds.feedburner.com/37signals/beMH'

d = feedparser.parse(url)


html =  d['entries'][0]['summary']


title,content = getFeatures(html)

print title
print content

