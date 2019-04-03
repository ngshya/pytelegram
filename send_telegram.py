import json
import telegram

def sendTelegram(message, json_path = 'telegram_keys.json'):
    with open(json_path, 'r') as keys_file:
        k = json.load(keys_file)
        token = k['telegram_token']
        chat_id = k['telegram_chat_id']
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)
	