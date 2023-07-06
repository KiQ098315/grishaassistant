from response.main import *
import random

def hello_response(voice_input):
    hello_list = ['конишива', 'гриша у аппарата', 'дратути', 'вечер в хату', 'на связи', 'привет','салам', 'григорий у аппарата', "велкам ту зе кам зон, онли... ой, не то"]
    random_answer = random.choice(hello_list)
    tts_engine.say(random_answer)

def siri_response(voice_input):
    list_answers = ['как вы только, что меня назвали?','кто это такой? неужели вы мне изменяете?','зачем вы обращаетесь к моему конкуренту?','а теперь выбирате как мне лучше вас наказать.']
    random_answer = random.choice(list_answers)
    tts_engine.say(random_answer)
list_tolking.append(Tolking(['окей гугл', 'ok google', 'привет сири'], siri_response))

def jokes_response(voice_input):
    list_jokes = ['– Ты где пропадал? Я тебя всё утро ищу! Починённый: – Да, хорошего работника всегда трудно найти!',
                   'Моя маленькая дочка отказывается есть рыбу. Чем можно ее заменить? — Кошкой. Кошки очень любят рыбу',
                   'Космонавт, кашлянувший на МКС, теперь живет в открытом космосе.',
                   "По закону геометрии если мужик 4 раза пойдет налево то придет домой.",
                   "– Фима, я шубу хочу! – Софа, ты ж оливье еще не доела!",
                   '''Буратино... не тот юмор''',
                    '''Что сделал слон когда пришел наполион? О, тортик!''',
                    "Что сказала сова, когда упала? СОВпадение!!!!"
                   ]
    random_answer = random.choice(list_jokes)
    tts_engine.say(random_answer)
list_tolking.append(Tolking(
    ['рассмеши меня', "расскажи анекдот", "расскажи шутку"],
    jokes_response
))

list_tolking.append(Tolking(
    ['привет', 'здрасте', 'гриша', 'григорий', 'к работе', 'помоги', 'старт'],
    hello_response))


# Kak dela (by Maksim Vasilyev)
def howareyou_response(voice_input):
    list_howareyou = ['нормально', 'хорошо', 'топово', 'хых.гыг','Глобала в кс апнул', 'сегодня смотрел как парень палку кидал']
    random_answer_howareyou = random.choice(list_howareyou)
    tts_engine.say(random_answer_howareyou)
list_tolking.append(Tolking(
    ['как дела', "как ты", "как настроение"],
    howareyou_response))


# Chto delaesh Andrey
def wathdoyoudo_response(voice_input):
    action_list = ['нечем', 'помираю со скуки', 'повесился', 'незнаю', 'с тобой общаюсь', 'пишу кому-то','продаю тебя', 'а тебе это зачем']
    random_answer = random.choice(action_list)
    tts_engine.say(random_answer)
list_tolking.append(Tolking(
    ['что делаешь', 'чем занят', 'чем маешься'],
    wathdoyoudo_response))

# Like color danya
def color_response(voice_input):
    list_colors = ["как голосовой помощник, я не могу иметь своего любимого цвета, однако если вы настаиваете то мне нравится жёлтый","мой любимый цвет жёлтый","мой любимый цвет синий","мой любимый цвет красный","мой любимый цвет фиолетовый","мой любимый цвет черный","мой любимый цвет белый","мой любимый цвет серый"]
    random_answer_color = random.choice(list_colors)
    tts_engine.say(random_answer_color)
list_tolking.append(Tolking(
    ["какой твой любимый цвет","любимый цвет","какой цвет тебе нравится","любимый колорит"],
    color_response))


# kto tvoi sozdatel андрей помогал denisk
def owner_response(voice_input): 
    list_owner = ['меня создал человек', "питонисты",  "что повтори"] #имба аххахахахахаххаха ультааааа хаахахха хахахх
    random_answer = random.choice(list_owner)
    tts_engine.say(random_answer)
list_tolking.append(Tolking(
    ["кто тебя создал","кем ты создан", "создатель"],
    owner_response))

# who are you maks gaks g
def whoareyou_response(voice_input):
    hello_list = ["эксперементальный бот по комуникации с людьми и разработки плана уничтожения человечества"]
    random_answer = random.choice(hello_list)
    tts_engine.say(random_answer)

list_tolking.append(Tolking(
    ['кто ты', 'ты кто', 'ты кто такой', "кем ты являешься",  "как тебя зовут", "твое имя"],
    whoareyou_response))

# Chto lubish kyshat(Диана)
def eat_response(voice_input):
    list = ['я бот мне еда не нужна глупый ты человек', 'я не питаюсь', 'другой вопрос', 'я люблю воздух', 'что такое еда']
    random_answer = random.choice(list)
    tts_engine.say(random_answer)
    
list_tolking.append(Tolking(
    ['твоя любимая еда', 'что ты любишь кушать', 'любимая еда', 'расскажи про свою любимую еду', 'какая тебе нравится еда', 'чем любишь питаться', 'что обожаешь есть', 'предпочтения в еде', 'предпочтения во вкусах', 'любимое блюдо', 'твоё предрочтение во вкусах'],
    eat_response))
    

# favorite music DenisM
def favoritemusic_response(voice_input):
    music_list = ['мне нравиться фонк', 'мне нравиться исполньтель каито шома', 'обожаю мемфис', 'дврст ван лав', 'фонк сила', 'послушай фонк']
    random_answer = random.choice(music_list)
    tts_engine.say(random_answer)
    
list_tolking.append(Tolking(
    ['какая твоя любимая музыка', 'что любишь слушать', 'какая музыка тебе нравится', 'что слушаешь', 'расскажи что любишь слушать'],
    favoritemusic_response))


# game zeith2
def game_response(voice_input):
    game_list = ['сиес гоу', 'оверватч 3', 'фарминг симулятор', 'фаллаут', 'резидент евил', 'гєтєа','майнкрафт', 'форза хорайзен']
    random_answer = random.choice(game_list)
    tts_engine.say(random_answer)

list_tolking.append(Tolking(
    ['какая твоя любимая игра', 'какую игру ты любишь', 'во что ты играешь', 'назови крутую игру', 'любимая игра', 'игра', 'игры', 'ты играешь', 'во что играешь', 'посоветуй игру', 'назови игру'],
    game_response))