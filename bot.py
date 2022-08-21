import asyncio
from pyrogram import Client

api_id = 18862638
api_hash = "2a4a8dc0c1f6c9cb65f9f144439558ae"
bot_token = "5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ"

async def main():
    async with Client("bot", api_id, api_hash, bot_token) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
