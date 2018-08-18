import pandas as pd

import feedparser

import requests



feed = requests.get('https://itunes.apple.com/us/rss/customerreviews/page=1/id=301724680/xml')

print feed.keys() #Feed is array of dictionaries

print feed['entries'][0].keys() #feed['entries'] is a list of dictionaries

entry = []

data = pd.DataFrame(columns=['title','title_detail','summary','link'])

j =0
for i in feed['entries']:
    data.loc[j] = [i.title, i.title_detail, i.summary, i.link]
    j+=1

data.to_csv('result',encoding='utf-8', index=False)






