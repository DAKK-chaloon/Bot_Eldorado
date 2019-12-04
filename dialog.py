# gialog.py
import cleverbot

from settings import CLEVERBOT_API

cb = cleverbot.Cleverbot(CLEVERBOT_API, timeout=60)

def sayToBot(text):
    try:
        reply = cb.say(text)
    except cleverbot.CleverbotError as error:
        print(error)
    else:
        print("Réponse du bot : " + reply)
    finally:
        cb.close()
    return reply