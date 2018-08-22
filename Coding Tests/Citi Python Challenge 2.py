import pandas as pd
import requests

import datetime
import xml.etree.ElementTree as ET


feed = requests.get('https://itunes.apple.com/us/rss/customerreviews/page=1/id=301724680/xml')

root = ET.fromstring(feed.content)
reviews = []

for i in root:
    if i.tag == '{http://www.w3.org/2005/Atom}entry' and i.find('{http://www.w3.org/2005/Atom}content').attrib.get('type') == 'text':

        reviews.append([i.find('{http://www.w3.org/2005/Atom}title').text,datetime.datetime.strptime(i.find('{http://www.w3.org/2005/Atom}updated').text[:10] , '%Y-%m-%d'), i.find('{http://www.w3.org/2005/Atom}content').text])




data = pd.DataFrame(columns=['Comment Title','Comment Date','Comment'])

j =0
for i in reviews:
    data.loc[j] = [i[0], i[1], i[2]]
    j += 1

#data = data[data['Comment Date'] < '2018-08-13'] #If we want one week earlier data
data.to_csv('result',encoding='utf-8', index=False)



