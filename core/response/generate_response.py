import os
from groq import Groq 
import asyncio
from dotenv import load_dotenv
from core.prompts.prompt import *

load_dotenv('.env.secrets')

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
        if user_text == '':
            return "please repeat your question"
        
        res = await (self.run_completion(user_text))
        return res 
    


if __name__ == '__main__':
    process = GroqAIProcessor()
    print(asyncio.run(process.process_text('hello how are you')))