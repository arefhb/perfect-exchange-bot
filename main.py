import telebot

from dotenv import load_dotenv
import os

load_dotenv()  # خواندن متغیرهای محیطی از فایل .env
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! به بات صرافی خوش آمدید.")

bot.polling()
