from getMesseges import getmessages
import urllib.parse

# def what_to_do():

def send_message(msg, chat_id):
    param = dict()
    param['chat_id'] = chat_id
    param['text'] = msg
    url = 'https://api.telegram.org/bot1056841936:AAF16sILMPdv9j5BFzn2rW7GKD5lSV4tJFc/sendMessage?' + urllib.parse.urlencode(param)
    urllib.request.urlopen(url)


def welcome_message(name, chat_id):
    msg = 'Hi ' + name + '. How are you? \n1.Type "Goal" to see about goal.'
    send_message(msg, chat_id)


def main():
    message_data = getmessages()
    previous_update_id = message_data['update_id']
    while True:
        message_data = getmessages()
        present_id = message_data['update_id']
        if present_id == previous_update_id:
            continue
        else:
            previous_update_id = present_id
            welcome_message(message_data['name'], message_data['chat_id'])

main()