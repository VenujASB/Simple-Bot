from pyrogram import Client, filters

api_id = 18862638
api_hash = "2a4a8dc0c1f6c9cb65f9f144439558ae"
bot_token = "5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ"

app = Client("bot", api_id, api_hash, bot_token)


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("**Hello Friend!**")


app.run()
