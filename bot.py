import os
import telebot


bot = telebot.TeleBot("5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm Simple Bot")

bot.polling()
