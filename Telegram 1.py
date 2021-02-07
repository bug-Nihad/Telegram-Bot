import urllib.request, urllib.parse
import json
import time


def send_message(chat_id, msg):
    param = dict()
    param['chat_id'] = chat_id
    param['text'] = msg
    url = 'https://api.telegram.org/bot1056841936:AAF16sILMPdv9j5BFzn2rW7GKD5lSV4tJFc/sendMessage?' + urllib.parse.urlencode(param)
    urllib.request.urlopen(url)

def activity(result):
    # print(json.dumps(result, indent=1))
    sender = result['from']['first_name']
    id = result['chat']['id']
    text = result['text']
    # print(sender, text, id)
    print(time_last)
    msg = 'Hi ' + sender +'. How are you? I am Pycharm'
    send_message(id, msg)


def welcome_message(result):
    sender = result['from']['first_name']
    msg = 'Hi ' + sender + '. How are you? I am Pycharm'
    send_message(id, msg)

def analyse_text(text):
    print('Analysing Text.')






i = 0
while True:

    data = urllib.request.urlopen('https://api.telegram.org/bot1056841936:AAF16sILMPdv9j5BFzn2rW7GKD5lSV4tJFc/getupdates').read()
    data = json.loads(data)


    if i == 0:
        time_last = data['result'][-1]['message']['date']
        i = 1
        continue
    time_now = data['result'][-1]['message']['date']
    if time_last == time_now:
        continue
    if int(time_now) - int(time_last) >=300:
        welcome_message(data['result'][-1]['message'])
    time_last = time_now
    analyse_text(data['result'][-1]['message']['text'])
    time.sleep(1)