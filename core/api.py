from core.prompts import * 
from core.response import * 
from core.utiles import *

class ProcessInput:

    def __init__(self):
        self.process = GroqAIProcessor()
        self.tts = TextTOSpeech()
        self.stt = SpeechToText()


if __name__ == '__main__':
    print('done')