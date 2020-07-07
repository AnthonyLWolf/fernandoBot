import json
from botocore.vendored import requests

TELE_TOKEN='1318346445:AAFuYhLvBurrRN_ZKIJU9C73C6Yi5uJ8a98'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

def send_message(text, chat_id):
    final_text = "Fernando ripete: " + text.lowercase
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id)
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']
    send_message(reply, chat_id)
    return {
        'statusCode': 200
    }
