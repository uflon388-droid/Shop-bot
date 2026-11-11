import telebot

TOKEN = "9222967065:AAF32M8LWaf44VlAMo-T1IGbJ6XYUheapHs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot. 😊")

bot.infinity_polling()
