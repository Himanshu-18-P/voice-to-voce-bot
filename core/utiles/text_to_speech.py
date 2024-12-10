import os
import base64
from google.cloud import texttospeech
import io
from pydub import AudioSegment


# function for text to speech with the help of google tts
class TextTOSpeech:

    def __init__(self):
        self.code = "en-IN"
        self.name = "en-IN-Neural2-D"
 
    def googletts_base64_audio(self , text):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'core/google_api/google_tts.json'
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
    
if __name__ == '__main__':
    test = TextTOSpeech() 
    print(test.googletts_base64_audio('hello'))
    print('done')