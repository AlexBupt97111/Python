from urllib.request import urlopen 
from bs4 import BeautifulSoup
import requests 

class Content:
    def __init__(self, url, title, body): 
        self.url = url 
        self.title = title
        self.body = body 

def get_page(url):
    req = requests.get(url)
    if req.status_code == 200: 
        return BeautifulSoup(req.text, "html.parser")
    else:
        return None 

def news_from_site(url):
    bs = get_page(url)
    if bs is None:
        return bs
    else:
        title = bs.find("h1", {"class": "c-card__title"}).text 
        lines = bs.find_all("div", {"class":"c-article__lead"}) 
        body = "\n".join([line.text for line in lines]) 
        return Content(url, title, body) 
      
content = news_from_site("https://tsn.ua/ukrayina/u-prezidenta-motor-sichi-areshtuvali-use-mayno-yogo-vartist-mayzhe-1-mlrd-griven-2194915.html")
if content is None:
    print("Error")
else:
    print("Title: {}".format(content.title))
    print("Adress: {}".format(content.url), "\n")
    print("Text: {}".format(content.body))
