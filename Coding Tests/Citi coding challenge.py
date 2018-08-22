import pandas as pd
import requests

import datetime
import xml.etree.ElementTree as ET


feed = requests.get('http://www.hindustantimes.com/rss/topnews/rssfeed.xml')

with open('reviews.xml', 'wb') as f:
    f.write(feed.content)

tree = ET.parse('reviews.xml')
#print feed.content
#print tree.getroot().findall('.')
