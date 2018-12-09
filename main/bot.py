import json

import requests
import telebot

TOKEN = '746320164:AAEOrs5dcD-9HKUngbAbzO6B4tPvabj_Mvo'
bot = telebot.TeleBot(TOKEN)
API_PATH = 'http://127.0.0.1:8000'


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Введите название')
    bot.register_next_step_handler(msg, add_title)


def add_title(message):
    msg = bot.send_message(message.chat.id, 'Введите содержимое заметки')
    bot.register_next_step_handler(message, add_text, message.text)


def add_text(message, title):
    text = message.text
    data = {'title': title, 'text': text}
    req = requests.post(API_PATH + '/add_note/', data=data)
    print(req.status_code)


@bot.message_handler(commands=['get_tasks'])
def get_tasks(message):
    req = requests.get(API_PATH + '/get_notes/')
    data = json.loads(req.text)
    for note in data:
        title = 'Название заметки - ' + note['title'] + '\n'
        text = 'Текст заметки - ' + note['text'] + '\n'
        full_date = note['date'].rsplit('T')
        date = 'Дата создания - ' + full_date[0] + '\n'
        time = 'Время создания - ' + full_date[1]
        bot.send_message(message.chat.id, title + text + date + time)


bot.polling(none_stop=True)
