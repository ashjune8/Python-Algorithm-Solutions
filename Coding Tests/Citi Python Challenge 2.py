import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime


feed = requests.get('https://itunes.apple.com/us/rss/customerreviews/page=1/id=301724680/xml')
soup = BeautifulSoup(feed.text)
entry = soup.find_all('entry')

reviews = []

for i in entry:
    if i.find('content', type="text"):
        reviews.append([i.title.string,datetime.datetime.strptime(i.updated.string[:10] , '%Y-%m-%d'),i.content.string])

data = pd.DataFrame(columns=['Comment Title','Comment Date','Comment'])

j =0
for i in reviews:
    data.loc[j] = [i[0], i[1], i[2]]
    j += 1

#data = data[data['Comment Date'] < '2018-08-13'] #If we want one week earlier data
data.to_csv('result',encoding='utf-8', index=False)



