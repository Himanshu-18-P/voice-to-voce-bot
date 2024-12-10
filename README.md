# voice-to-voce-bot

**voice-to-voce-bot** is an interactive voice-to-voice conversational assistant that accepts natural language speech queries and responds in a human-like voice. It leverages advanced language models and text-to-speech (TTS) services to deliver a smooth, spoken Q&A experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Features

- **Natural Language Input:** Speak your questions as you would to another person.
- **Human-like Responses:** Uses advanced TTS to provide responses in a natural, lifelike voice.
- **Customizable Backends:** Integrate with various language models or speech APIs as needed.

**Prerequisites:**
- Python 3.8+
- A `.env.secrets` file in the project root with:
  ```bash
  GROQ_API_KEY='your_groq_api_key'
  API_KEY='your_api_key'

## Installation
- git clone https://github.com/Himanshu-18-P/voice-to-voce-bot.git
- cd voice-to-voce-bot
- pip install -r requirements.txt

## Configuration
- mkdir log
- Ensure that .env.secrets in the project root contains your keys
  GROQ_API_KEY='your_groq_api_key'
  API_KEY='your_api_key'
- Place google_tts.json inside google_api/
  core/google_api/google_tts.json
-Place your PDF in system_prompt/
  system_prompt/your_file.pdf

## Usage

- Generate embeddings from your PDF
  python creat_db.py
- In main.py, pass the db_path to create_app()
  app = create_app(db_path='path_to_your_db')
- Run the application
  python main.py
- Follow the on-screen instructions. Speak your query, and the bot will respond with a synthesized, human-like voice.

