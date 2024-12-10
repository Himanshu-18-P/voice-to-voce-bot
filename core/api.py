from core.prompts import * 
from core.response import * 
from core.utiles import *

class ProcessInput:

    def __init__(self):
        self.process = GroqAIProcessor()
        self.tts = TextTOSpeech()
        self.stt = SpeechToText()
        self.creat_prompt = PrepareData()

    def get_data(self , user_text , db_path):
        text = self.creat_prompt.retrive_similer_docs_using_fassi(user_text , db_path)
        return text

if __name__ == '__main__':
    print('done')