import pandas as pd

import feedparser

#https://wiki.python.org/moin/RssLibraries

feed = feedparser.parse('https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US')

print feed.keys() #Feed is array of dictionaries

print feed['entries'][0].keys() #feed['entries'] is a list of dictionaries

entry = []

data = pd.DataFrame(columns=['title','title_detail','summary','link'])

j =0
for i in feed['entries']:
    data.loc[j] = [i.title, i.title_detail, i.summary, i.link]
    j+=1

data.to_csv('result',encoding='utf-8', index=False)






