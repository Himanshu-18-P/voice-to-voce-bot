# voice-to-voce-bot

**voice-to-voce-bot** is an interactive voice-to-voice conversational assistant. You can speak a question in natural language, and it will respond with a human-like voice. This bot leverages language models and text-to-speech services to provide a seamless, spoken Q&A experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Features

- **Natural Language Input:** Ask questions just like you would to a human.
- **Human-like Responses:** The bot generates voice responses using advanced text-to-speech (TTS) technology.
- **Customizable Backends:** Easily integrate different language models or speech APIs.

## Installation

**Prerequisites:**
- Python 3.8+
- Create a `log/` directory for logs.
- A `.env.secrets` file (placed in the project root) with the following environment variables:
  - `GROQ_API_KEY=''`
  - `API_KEY=''`
- A `google_api/` folder containing `google_tts.json` (your Google TTS credentials).

**Steps:**
```bash
git clone https://github.com/Himanshu-18-P/voice-to-voce-bot.git
cd voice-to-voce-bot
pip install -r requirements.txt
