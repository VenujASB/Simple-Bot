import os
from pyrogram import Client, filters
from config import Config

bot_token = Config.bot_token
api_id = Config.api_id
api_hash = Config.api_hash

bot = Client("bot", api_id, api_hash, bot_token)


@bot.on_message(filters.regex("hi"))
async def send_hi(_, message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = "Hello!")   
                       
print("Bot is alive!")
bot.run()
