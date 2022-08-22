from pyrogram import Client, filters
import os


api_id = 18862638
api_hash = "2a4a8dc0c1f6c9cb65f9f144439558ae"
bot_token = "5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ"

bot = Client("bot", api_id, api_hash, bot_token)


@bot.on_message(filters.regex("hi"))
async def send_hi(_, message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = "Hello!")   
                       
print("Bot is alive!")
bot.run()
