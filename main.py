import telebot

TOKEN = "YOUR_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot. 😊")

bot.infinity_polling()
