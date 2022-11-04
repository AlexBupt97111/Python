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
    title = bs.find("h1", {"class": "article-title"}).text 
    lines = bs.find_all("p") 
    body = "\n".join([line.text for line in lines]) 
    return Content(url, title, body) 

content = news_from_site("https://bzh.life/ua/mesta-i-veshi/ukrzalizniczya-vidkrila-kramnichku-z-merchem-na-vokzali-u-kievi/")
if content is None:
    print("Error")
else:
    print("Title: {}".format(content.title), "\n")
    print("Adress: {}".format(content.url), "\n")
    print("Text: {}".format(content.body))
