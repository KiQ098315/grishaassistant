import pyttsx3

tts_engine = pyttsx3.init()

class Tolking:
    def __init__(self, request, response):
        self.request = request 
        self.response = response

list_tolking = []