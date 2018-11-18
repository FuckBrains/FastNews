import requests
from tts import *
from bs4 import BeautifulSoup
import unicodedata
import os
import datetime
from datetime import timedelta

publishTime = datetime.datetime.now()
publishTime = publishTime + timedelta(hours=1, minutes=10)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GOOGLE_APPLICATION_CREDENTIALS.json"
result = requests.get("http://www.bbc.com/news")

soup = BeautifulSoup(result.content, "lxml")

#headlines = soup.find_all("h3")[:1]

articleAnchors = soup.findAll("a", class_="gs-c-promo-heading", href=True)[:10]

#for headline in headlines:
#    print headline.text
#    print headline
#print articleAnchors
for elem in articleAnchors:
    title = elem.text.replace("'","")
#    print elem.text
#    print "http://www.bbc.com" +  elem['href']


    URL = "http://www.bbc.com" +  elem['href']
    articleResult = requests.get(URL)
    articleSoup = BeautifulSoup(articleResult.content, "lxml")

    articlePara = articleSoup.findAll("p")[12:18]

    script = ""
#    script = ""
    for para in articlePara:
        script += unicodedata.normalize('NFKD', para.text).encode('ascii','ignore').replace("'","")
#        print para.text
#    print ""
#    print ""
#    print "Call function with parameters Title and Script"
    script = script.replace(".",". ")
    scriptTS(title, script, URL, publishTime)
    publishTime = publishTime + timedelta(minutes=20)
