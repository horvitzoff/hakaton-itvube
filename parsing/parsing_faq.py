import time
from bs4 import BeautifulSoup
from requests import get
from data.const import Urls
import json

def pars():
    soup = BeautifulSoup(get(Urls.url_faq).text,features="lxml")
    html = soup.find('div',class_='menu__result').find_all('section')
    slovar ={}
    for i in range(len(html)):
        section = html[i].find_all('div',class_ = 'expand-panel')
        for x in range(len(section)):
            title = section[x].find('span').text
            text = section[x].find('div').text
            slovar[title] = text
    with open("/json/data_file.json", "w",encoding='utf8') as write_file:
        json.dump(slovar, write_file,ensure_ascii=False)

def parsing():
    while True:
        pars()
        time.sleep(86400)
