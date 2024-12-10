from flask import Flask, send_from_directory , request , jsonify
from core.api import *
import asyncio
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/main.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def serve_index():
        # to render html file
        return send_from_directory('templates', 'index.html')

    @app.route('/process' , methods = ['POST'])
    def process():
        try:
            "this api will take text or audio from user ,process it and audio response"
            data = request.json
            input = data.get('text' , '')
            if data.get("is_audio" , False):
                input = init.stt(input)
            res = asyncio.run(init.process.process_text(input))
            audio = init.tts.googletts_base64_audio(res)
            return {'text' : res  , "audio" : audio}
        
        except Exception as e:
            logger.error(f"Error: {e}")
            return jsonify({"error": str(e)}), 500
        
    return app

if __name__ == '__main__':
    init = ProcessInput()
    app = create_app()
    app.run(debug=True)
