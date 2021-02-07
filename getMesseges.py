import urllib.request
import json

def getmessages():
    data = urllib.request.urlopen('https://api.telegram.org/bot1056841936:AAF16sILMPdv9j5BFzn2rW7GKD5lSV4tJFc/getupdates').read()
    data = json.loads(data)
    message_id = data['result'][-1]['message']['message_id']
    update_id = data['result'][-1]['update_id']
    chat_id = data['result'][-1]['message']['from']['id']
    name = data['result'][-1]['message']['from']['first_name']
    date = data['result'][-1]['message']['date']
    text = data['result'][-1]['message']['text']
    message_data = {
        'update_id' : update_id,
        'chat_id' : chat_id,
        'name' : name,
        'message_id' : message_id,
        'date' : date,
        'text' : text
    }
    return message_data
