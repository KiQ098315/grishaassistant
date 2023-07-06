from recognize.rec import *
from response.init import *
import os
import asyncio


#Good dumplings are very very tasty
API_URL = 'http://127.0.0.1:5002/check/'
while True:
    # старт записи речи с последующим выводом распознанной речи 
    if requests.get(API_URL).status_code == 200:
        voice_input = record_and_recognize_audio()
        print(voice_input)
        if voice_input == 'стоп':
            break
        else:
            for tolk in list_tolking:
                for req in tolk.request:
                    if req in voice_input:
                        tolk.response(voice_input)
                        break

        tts_engine.runAndWait()
