import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env.secrets')

class SpeechToText:

    def __init__(self):
        self.client = OpenAI(api_key = os.getenv("API_KEY"))
    
    # function convert audio in text using 
    def convert_to_text(self , audio_path):
        audio_file= open(audio_path, "rb")
        transcription = self.client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file , 
        language='en'
        )
        return transcription.text
    
if __name__ == '__main__':
    ll = SpeechToText()
