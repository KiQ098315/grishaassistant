from response.main import *
import random
import requests
from bs4 import BeautifulSoup

def get_wether(voice_input):
    weather_dict = {
        'днепр': 'https://ua.sinoptik.ua/погода-дніпро',
        'стокгольм':'https://sinoptik.ua/погода-стокгольм',
        'луцк':'https://sinoptik.ua/погода-луцк',
        'кривой-рог':'https://sinoptik.ua/погода-кривой-рог',
        'житомир':'https://sinoptik.ua/погода-житомир',
        'винниц':'https://sinoptik.ua/погода-винница',
        'ровно':'https://sinoptik.ua/погода-ровно',
        'львов':'https://sinoptik.ua/погода-львов',
        'киев':'https://sinoptik.ua/погода-киев',
        'запорожье':'https://sinoptik.ua/погода-запорожье',
        'одесс':'https://sinoptik.ua/погода-одесса',
        'чернобыл':'https://sinoptik.ua/погода-чернобыль',
        'харьков':'https://sinoptik.ua/погода-харьков'
    }
    # flag = False
    for i in weather_dict.keys():
        if i in voice_input:
            result = requests.get(weather_dict[i])
            soup = BeautifulSoup(result.text, 'html.parser')

            min = soup.find('div', class_='min').find('span').text
            max = soup.find('div', class_='max').find('span').text
            # flag = True
            # print(min, max  tts_engine.say()  
            answers = [
                f'Сегодня в {i}е погода такая: минимум - {min} максимум - {max}',
                f'{i}.Минимальная температура сегодня: {min}. Максимальная: {max}.',
                f'Температура воздуха в {i}е колеблится от {min} до {max}',
                f'В городе {i}e погода такая: минимальная - {min} максимальная - {max}',
                f'Погодка в {i}e ваще кайфарик, холодок где-то на уровне {min} а вот жарить солнышко будет на уровне {max} ',
                f'На протяжении дня в {i}e обещают максимальную температуру - {max} минимальную - {min}',
                f'{i}. Ваша попа будет мерзнуть при минимально температуре {min} и потеть при {max} цельсия.',
                f'Сегодня в городе {i}e минимальная температура воздуха: {min}, а максимальная: {max}',
                f'Температура в городе {i}e сегодня от {min} до {max}',
                f'В {i}e погоды нет, а вот температура от {min} до {max}. Цельсия, если что' #погода это иллюзия духоты
            ]
            answ = random.choice(answers)
            print(answ)
            tts_engine.say(answ)

list_tolking.append(Tolking(
    ['как погода', "какая погода"],
    get_wether))

# get_wether('харьков днепр')

def defs_response(voice_input):
    response = requests.get("https://rozetka.com.ua/apple-iphone-14-pro-max-1tb-deep-purple/p352490925/?gclid=CjwKCAjws7WkBhBFEiwAIi1680KuqMUXQPHdB8YBJt7RVgEXA0wUZPBs3XDSNMZ98LduWWuSPg8hTxoC-fkQAvD_BwE")
    soup = BeautifulSoup(response.content, 'html.parser')
    elements = soup.find_all(class_='product-price__big product-price__big-color-red')
    list_howareyou = [f"Цена на новую версию айфонайзера: {elements[0].text} гривен"]
    random_answer_howareyou = random.choice(list_howareyou)
    tts_engine.say(random_answer_howareyou)
list_tolking.append(Tolking(['айфон', 'iphone'],defs_response)) 