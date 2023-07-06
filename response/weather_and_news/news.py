from response.main import *
from bs4 import BeautifulSoup
import requests


def news_response(voice_input):
    n1 = news1()
    n2 = news2()
    n3 = news3()
    n4 = news4()
    tts_engine.say(n1)
    tts_engine.say(n2)
    tts_engine.say(n3)
    tts_engine.say(n4)

    
def news1():
    result = requests.get("https://www.pravda.com.ua/rus/news/")
    soup = BeautifulSoup(result.text, 'html.parser')
    news = soup.find('div', class_='article_header')
    return news.text
def news2():
    result = requests.get("https://tsn.ua/")
    soup = BeautifulSoup(result.text, 'html.parser')
    news = soup.find('div', class_="l-sidebar__gap")
    return news.text
def news3():
    res = requests.get('https://www.unian.ua/?utm_source=siteua&utm_medium=siteua&utm_campaign=siteua')
    soup = BeautifulSoup(res.text, 'html.parser')
    
    capt = soup.find('a', class_ = 'main-unit__title').text
    
    return capt
def news4():
    result = requests.get("https://www.pravda.com.ua/news/2023/04/1/7395981/")
    soup = BeautifulSoup(result.text,"html.parser")
    news_caption = soup.find('h1', class_ = 'post_title')
    news_time = soup.find('div', class_ = 'post_time')
    return f'''{news_caption.text}
    {news_time.text}'''

list_tolking.append(Tolking(
    ['новости'],
    news_response))