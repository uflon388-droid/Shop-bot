import telebot

API_KEY = '9222967065:AAF32M8Lwaf44VIAMO-T1IGbJ6XYUheapHs'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot.")

bot.polling()
