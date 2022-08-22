import os
from pyrogram import Client, filters
from config import Config
import aiofiles
import aiohttp

bot_token = Config.bot_token
api_id = Config.api_id
api_hash = Config.api_hash

bot = Client("bot", api_id, api_hash, bot_token)

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

@bot.on_message(filters.regex("hi"))
async def send_hi(_, message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = "Hello!")   
                       
print("Bot is alive!")
bot.run()
