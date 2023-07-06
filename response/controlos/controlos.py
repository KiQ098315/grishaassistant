import osascript
from response.main import *
import random    
import subprocess
import re
import os
from PIL import ImageGrab


#Good dumplings are very very tasty
# really good

def up_volume(voice_input):
    result = osascript.osascript('get volume settings')
    current_volume = int(result[1].split(':')[1].split(',')[0])
    current_volume += 10
    osascript.osascript(f"set volume output volume {current_volume}")
    tts_engine.say('Громкость увеличена')
    result = osascript.osascript('get volume settings')   

list_tolking.append(Tolking(["сделай громче","увеличь звук"], up_volume))

def down_volume(voice_input):
    result = osascript.osascript('get volume settings')
    current_volume = int(result[1].split(':')[1].split(',')[0])
    current_volume -= 10
    osascript.osascript(f'set volume output volume {current_volume}')
    tts_engine.say('Громкость уменьшена')
    result = osascript.osascript('get volume settings')
list_tolking.append(Tolking(['сделай тише','уменьши звук'],down_volume))
#африка
def set_volume(voice_input):
    pattern = r'сделай громкость (\d{1,3})'
    result = re.match(pattern,voice_input)
    if not result:
        print('err')
        return 
    osascript.osascript(f"set volume output volume {result.group(1)}")
    tts_engine.say(f'Громкость установленна на {result.group(1)} процентов')
list_tolking.append(Tolking(['сделай громкость'],set_volume))

def lock_screen(voice_input):


    subprocess.run(['open', '/System/Library/CoreServices/ScreenSaverEngine.app'])
list_tolking.append(Tolking(['выход'],lock_screen))

def create_py_file(voice_input):
    reg = re.match(r'создай python file (.+)', voice_input)
    result_name = reg.group(1)
    path = '/Users/6040h0k/Desktop/программирование/Python/other'
    os.system(f'cd {path}')
    os.system(f'touch {result_name}.py')
    os.system('pwd')
    tts_engine.say(f"Пайтон файл {result_name} создан")
list_tolking.append(Tolking(['создай python file'], create_py_file))
    
    
def open_visual_studio_code(voice_input):
    #Visual Studio Code
    vscode_path = "open  /Applications/Visual\ Studio\ Code.app/"
    os.system(vscode_path)
    tts_engine.say("VS Code открыт")
list_tolking.append(Tolking(['открой вс код', 'запусти визуал студио','запусти вс код','открой визуал студио','открой visual studio','запусти visual studio'], open_visual_studio_code))

def block_system(voice_input):

    applescript = '''
    tell application "System Events" to sleep
    '''
    tts_engine.say("Отключаюсь")
    # Выполнение AppleScript-скрипта
    subprocess.call(['osascript', '-e', applescript]) # tandr
    
list_tolking.append(Tolking(["выключи компьютер", "заблокируй систему"], block_system))

def turn_on_bluetooth(voice_input): #andr, litle tandr
    subprocess.run(["blueutil", "-p", "1"])
    tts_engine.say("Bluetooth успешно запущен")
list_tolking.append(Tolking(["включи bluetooth","запусти bluetooth", "активируй bluetooth"], turn_on_bluetooth))

    
def turn_off_bluetooth(voice_input):
    tts_engine.say('блютуз отключен')
    subprocess.run(["blueutil", "-p", "0"])
list_tolking.append(Tolking(['выключи bluetooth', 'оффни bluetooth', 'выруби bluetooth'], turn_off_bluetooth))



def turn_on_wifi(voice_input): #DenisM
    tts_engine.say('ВайФай включен')
    subprocess.run(["networksetup", "-setairportpower", "Wi-Fi", "on"])
list_tolking.append(Tolking(['включи wifi', 'запусти wifi'], turn_on_wifi))



def turn_off_wifi(voice_input): #Максим Васильев \(@^0^@)/ -_-
    tts_engine.say('ВайФай отключен')
    subprocess.run(["networksetup", "-setairportpower", "Wi-Fi", "off"])

list_tolking.append(Tolking(['выключи wifi','выключи wifi','протокол 9'], turn_off_wifi))


def screenshot(voice_input):
    tts_engine.say('скриншот сделан')
    path = os.path.abspath(__file__ + '/../../..') + '/screens'
    # Сделать скриншот всего экрана
    image = ImageGrab.grab()

    # Сохранить скриншот в файл

    image.save(f"{path}/screenshot{random.randint(1000000,999999999)}.png")
list_tolking.append(Tolking(['сделай скриншот','сфотографируй экран','сделай снимок','заскринь'], screenshot))

    