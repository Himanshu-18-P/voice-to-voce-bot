import os
import base64
from google.cloud import texttospeech
import io
from pydub import AudioSegment
import logging
from flask import jsonify

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/tts.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'core/google_api/google_tts.json'


class TextTOSpeech:

    def __init__(self):
        self.code = "en-IN"
        self.name = "en-IN-Neural2-D"
    
    # function for text to speech with the help of google tts
    def googletts_base64_audio(self , text):
        try:
            client = texttospeech.TextToSpeechClient()
            synthesis_input = texttospeech.SynthesisInput(text = text)
            voice = texttospeech.VoiceSelectionParams(
                    language_code=self.code,
                    name= self.name,
                    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
                )

            audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.MP3 , 
                    effects_profile_id = ['small-bluetooth-speaker-class-device'] ,
                    speaking_rate = 1 ,
                    pitch = 0.9 
                )
            response = client.synthesize_speech(
                input= synthesis_input , voice=voice , audio_config=audio_config
            )
            audio_content_base64 = base64.b64encode(response.audio_content).decode('utf-8')
            return audio_content_base64
        
        except Exception as e:
            logger.error(f"Error: {e}")
            return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    test = TextTOSpeech() 
    print(test.googletts_base64_audio('hello'))
    print('done')