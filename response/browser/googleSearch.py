from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from response.main import *
import time
import os
import re
import random
service = Service(executable_path=os.path.abspath(__file__ + "/../../..") + "/chromedriver")
driver = None
def open_browser(voice_input):
    global driver
    if not driver:
        
        driver = webdriver.Chrome(service=service)
        # driver = webdriver.Chrome()
        driver.get('https://www.google.com/')
        tts_engine.say('Браузер открыт')

def close_browser(voice_input):
    tts_engine.say('браузер закрыт')
    global driver
    if driver:
        driver.close()
        driver = None
list_tolking.append(Tolking(['закрой браузер'], close_browser))
def searchGoogle(voice_input):
    global driver
    print(driver)
    if not driver:
        open_browser(voice_input)
    driver.get('https://www.google.com/webhp?hl=uk&ictx=2&sa=X&ved=0ahUKEwi-7-GXl73-AhWpgf0HHbqKCRYQPQgJ')
    search = driver.find_element(By.NAME,'q')

    result = re.match(r'найди (.+)', voice_input)
    try:
        request = result.group(1)
        search.send_keys(request)
        search.submit()
        tts_engine.say(f'Вот результаты поиска по запросу {request}')
    except:
        print('error')


list_tolking.append(Tolking(
    ['найди'], searchGoogle
))
list_tolking.append(Tolking(
    ['открой браузер', 'запусти браузер', 'включи браузер', 'раскрой браузер'], open_browser
)) 

def music(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
    voice_input = re.match('включи песню (.+)', voice_input).group(1)
    tts_engine.say("Включаю музыку")
    driver.get('https://open.spotify.com/search')
    search = driver.find_elements(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0')[0]
    time.sleep(1)
    search.send_keys(voice_input)
    time.sleep(3)
    search = driver.find_elements(By.CLASS_NAME, 'gvLrgQXBFVW6m9MscfFA')[1]
    search.click()
    time.sleep(2) #Хочу пельмени! Артем, мы в тебя верим)
    search = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button/span')
    search.click()
    time.sleep(5)
    button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div/div[1]/div[2]/p/a')
    button.click()
    time.sleep(2)
    search = driver.find_element(By.ID, 'login-username')
    search.send_keys('clastbro22@gmail.com')
    search = driver.find_element(By.ID, 'login-password')
    search.send_keys('qwerty123456')
    time.sleep(2)
    search = driver.find_element(By.CLASS_NAME, 'encore-bright-accent-set')               
    search.click() 


list_tolking.append(Tolking(
    ['включи песню'], music
))

def youtube(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
    voice_input = re.match(r'.+видео(.+)', voice_input).group(1)
    driver.get('https://www.youtube.com/')
    search_youtube = driver.find_element(By.NAME, 'search_query')
    search_youtube.send_keys(voice_input)
    search_youtube.submit()
    time.sleep(3)
    video = driver.find_element(By.CLASS_NAME, 'ytd-video-renderer')
    video.click()
    tts_engine.say("Ютуб включён")

def twitch(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
    voice_input = re.match(r'.+стрим(.+)', voice_input).group(1)
    driver.get('https://www.twitch.tv/?lang=ru')
    time.sleep(1)
    search =  driver.find_element(By.TAG_NAME, 'input')
    search.click()
    search.send_keys(voice_input)
    search = driver.find_element(By.CLASS_NAME, "dSicFr")
    search.click()
    time.sleep(3)
    search = driver.find_element(By.CLASS_NAME, "search-result-card__img-wrapper")
    search.click()
    tts_engine.say("Твич включён")

def series(voice_input):
    global driver
    if not driver:
        open_browser(voice_input)
    driver.get('https://hd-rezka.biz/serialy/')
    time.sleep(3)
    try:
        close_notif = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/span")
        close_notif.click()
        time.sleep(2)
    except:
        pass
    x_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/span')
    x_button.click()
    time.sleep(3)
    try:
        close_notif = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/span")
        close_notif.click()
        time.sleep(2)
    except:
        pass
    serial = driver.find_elements(By.CLASS_NAME, 'short-story')
    choise = random.choice(serial)
    choise.click()
    time.sleep(3)
    try:
        close_notif = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/span")
        close_notif.click()
        time.sleep(2)
    except:
        pass
    x_button = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/span')
    x_button.click()
    try:
        close_notif = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/span")
        close_notif.click()
        time.sleep(2)
    except:
        pass

list_tolking.append(Tolking(
    ['сериал'], series)
)

list_tolking.append(Tolking(
    ['включи видео', 'открой видео', 'запусти видео', 'найди видео', 'видео'], youtube
))
list_tolking.append(Tolking(
    ['включи стрим', 'открой стрим', 'покажи стрим'], twitch
))
