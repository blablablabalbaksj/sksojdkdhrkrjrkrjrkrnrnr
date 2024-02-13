import telebot
from background import keep_alive
import datetime
import os


TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Здесь можно отправить свои сообщения в канал \"в заре любят\". Если ваше сообщение содержит не приятную информацию, то оно не будет отправлено!")

@bot.message_handler(content_types=['text'], func=lambda message: True)
def add_text(message):
    username = message.text
    chat_id_id = message.chat.id
    nick = message.from_user.username
    chat_id = 910486417
    message = message.text
    bot.send_message(chat_id, message)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('user_data.txt', 'a') as f:
      f.write(f'Time: {timestamp}, User: {nick}, Chat ID: {chat_id_id}, Message: {username}\n')


keep_alive()

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
  
