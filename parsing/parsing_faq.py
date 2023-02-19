import time
from bs4 import BeautifulSoup
from loader import dp
from requests import get
from data.const import Urls
import json
import asyncio
import os


@dp.message_handler()
async def pars():
    soup = BeautifulSoup(get(Urls.url_faq).text, features="lxml")
    html = soup.find('div', class_='menu__result').find_all('section')
    slovar = {}
    for i in range(len(html)):
        section = html[i].find_all('div', class_='expand-panel')
        for x in range(len(section)):
            title = section[x].find('span').text
            text = section[x].find('div').text
            slovar[title] = text
    with open("parsing/json/data_file.json", "w+", encoding='utf8') as write_file:
        json.dump(slovar, write_file, ensure_ascii=False)


async def parsing():
    import aioschedule
    import asyncio
    aioschedule.every().day.at('00:00').do(parsing)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


