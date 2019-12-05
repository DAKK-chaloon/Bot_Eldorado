# Eldorado

Eldorado is a project of a Voice Cleverbot made for Discord and written in Python.

# Installation

- Install GoogleSDK and Python 3.7.0.
- Run CMD and move in bot directory.
- Write in the CMD "venv\Scripts\activate" and press enter.
- Write "set GOOGLE_APPLICATION CREDENTIALS=[PATH]" and replace [PATH] by the path of your credential.

# Configuration

- Fill the .env file with your prefered settings.
- You need to complete the file with your bot token and your cleverbot API.

# Run

- In cmd, write "python bot.py" and wait for launch.
- Send DISCORD_COMMAND + help in Discord channel to get help.

# Documentation :

- Speech To Text :
    - https://cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1?hl=fr
    - https://cloud.google.com/speech-to-text/docs/streaming-recognize?hl=fr#speech-streaming-recognize-python
    - https://github.com/Olical/snowball
    - https://refruity.xyz/writing-discord-bot/

- Text To Speech : 
    - https://cloud.google.com/text-to-speech/docs/audio-profiles?hl=fr
    - https://cloud.google.com/text-to-speech/docs/reference/libraries?hl=fr
    - https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries?hl=fr

- Redirect audio output to input :
    - https://www.howtogeek.com/364369/how-to-record-your-pc%E2%80%99s-audio-with-virtual-audio-cable/