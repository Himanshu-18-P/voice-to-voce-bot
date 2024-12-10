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

# init = ProcessInput()

def create_app(db_path='fassi_db/smart'):

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
            relvent_text = init.get_data(input , db_path)
            res = asyncio.run(init.process.process_text(input , relvent_text))
            audio = init.tts.googletts_base64_audio(res)
            return {'text' : res  , "audio" : audio}
        
        except Exception as e:
            logger.error(f"Error: {e}")
            return jsonify({"error": str(e)}), 500
        
    return app

if __name__ == '__main__':
    init = ProcessInput()
    app = create_app('fassi_db/smart')
    app.run(debug=True)

# app = create_app()