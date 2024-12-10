import os
from groq import Groq 
import asyncio
from dotenv import load_dotenv
from core.prompts.prompt import *
import logging
from flask import jsonify

load_dotenv('.env.secrets')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/response.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class GroqAIProcessor:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

    
    async def run_completion(self,user_input):
        resp = self.client.chat.completions.create(
            messages=[
                {
                 "role": "system",
                 "content": prompt_for_response
                },

            {
                "role": "user",
                "content": user_input,
            }
            ],
                model= "llama-3.3-70b-versatile"  ,
                temperature = 0.0,
                top_p = 1,
                max_tokens = 1024
            )

        return resp.choices[0].message.content
    
    async def process_text(self , user_text):
        try:
            if user_text == '':
                return "please repeat your question"
            
            res = await self.run_completion(user_text)
            return res 
        
        except Exception as e:
            logger.error(f"Error: {e}")
            return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    process = GroqAIProcessor()
    print(asyncio.run(process.process_text('hello how are you')))