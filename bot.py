from telebot import TeleBot
from telebot import types
import requests
import imgkit
from io import BytesIO

API = "http://127.0.0.1:8080"

bot = TeleBot("6050972405:AAHdvLfM86oSaCLMq9y2hKUEV1mhjPh_a7w") 

CHAT_ID = "@birth_matrix_zakharova"

button_calc = types.InlineKeyboardButton('Рассчитать', callback_data='calc')
keyboard_calc = types.InlineKeyboardMarkup()
keyboard_calc.add(button_calc)

button_subscribe = types.InlineKeyboardButton('Подписаться', url='https://t.me/birth_matrix_zakharova')
keyboard_subscribe = types.InlineKeyboardMarkup()
keyboard_subscribe.add(button_subscribe)

button_prompt = types.InlineKeyboardButton('Рассчитать', url='https://t.me/birth_matrix_bot')
keyboard_prompt = types.InlineKeyboardMarkup()
keyboard_prompt.add(button_prompt)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!\nЯ рассчитаю твою матрицу судьбы", reply_markup=keyboard_calc)

@bot.message_handler(commands=['prompt'])
def start_message(message):
    bot.send_message(CHAT_ID, "Привет!\nЯ рассчитаю твою матрицу судьбы", reply_markup=keyboard_prompt)

def test(user): 
    result = bot.get_chat_member(CHAT_ID, user)
    return result.status != 'left'

@bot.callback_query_handler(lambda query: query.data == "calc")
def ask(query):
    try:
        user = query.message.chat.id
        result = test(user)
        if(not result):
            bot.send_message(user, "Вы не подписанны на канал!", reply_markup=keyboard_subscribe)
        else:
            bot.send_message(user, "Ваша дата рождения? (дд.мм.гггг)")
    except:
        bot.send_message(user, "Произошла непредвиденная ошибка! Если это повторится - свяжитесь с администратором.")

@bot.message_handler(content_types=['text'])
def get_matrix(message):
    user = message.chat.id
    try:
        if(test(user)):
            image = calc(message.text)
            bot.send_photo(user, photo=image)
        else:
            bot.send_message(user, "Вы не подписанны на канал!", reply_markup=keyboard_subscribe)
    except:
        if(test(user)):
            bot.send_message(user, "Возможно вы неверно ввели дату рождения (дд.мм.гггг)")

def getv(value):
    return value if value<=22 else value-22

def calc(birth):
    req = requests.post(API+"/calc", json={'birth': birth, 'type':'a'})

    if(req.text=="error"):
        raise Exception()
    data = req.json()

    config = imgkit.config(wkhtmltoimage='D:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    file = imgkit.from_string(data['pictgm'], False, config=config, options = {"enable-local-file-access": None, 'crop-w': 516})
    
    bio = BytesIO(file)
    bio.name = 'matrix.jpeg'
    bio.seek(0)

    return bio

bot.polling()