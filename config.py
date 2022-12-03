import requests
import telebot
from bs4 import BeautifulSoup as bts

'''работает не так как хотелось!!'''

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Введите название игры по английски')


@bot.message_handler(content_types=['text'])
def anecdot(message):
    list_steam = message.text
    try:
        if message.text.lower() in list_steam:
            url = 'https://store.steampowered.com/search/?term=' + message.text
            '''парсим steam по ссылки, получаем название,сылку и цену'''
            r = requests.get(url)
            soup = bts(r.text, 'html.parser')
            name = soup.find('span', class_='title').text
            link = soup.find('a', class_='search_result_row').get('href')
            prise = soup.find('div', class_='search_price').text
            my_message = name + ' :' + link + prise
            bot.send_message(message.chat.id, my_message)
    except:
        bot.send_message(message.chat.id, 'Я не могу найти такую игру')


bot.polling()




