import json 
import telegram 
import logging
import sys

def pytlg(message, json_path = 'telegram_keys.json'):

    logging.disable(sys.maxsize)

    try:
        with open(json_path, 'r') as keys_file:
            k = json.load(keys_file)
            token = k['telegram_token']
            chat_id = k['telegram_chat_id']
        bot = telegram.Bot(token=token)
        bot.sendMessage(chat_id=chat_id, text=message)
    except:
        pass

    logging.disable(logging.NOTSET)
