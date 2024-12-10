from flask import Flask, send_from_directory , request , render_template
from core.api import *
import asyncio

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('templates', 'index.html')

@app.route('/process' , methods = ['POST'])
def process():
    data = request.json
    input = data.get('text' , '')
    res = asyncio.run(init.process.process_text(input))
    audio = init.tts.googletts_base64_audio(res)
    return {'text' : res  , "audio" : audio}

if __name__ == '__main__':
    init = ProcessInput()
    app.run(debug=True)
