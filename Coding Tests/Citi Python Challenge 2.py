import pandas as pd

import feedparser

#https://wiki.python.org/moin/RssLibraries

feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')

print feed.keys() #feed is array of dictionaries

print feed['entries'][0].keys() #feed['entries'] is a list of dictionaries

print feed['feed'].keys()
entry = []

data = pd.DataFrame(columns=['title','title_detail','summary','link'])

j =0
for i in feed['entries']:
    data.loc[j] = [i.title, i.title_detail, i.summary, i.link]
    j+=1

print data.head()






