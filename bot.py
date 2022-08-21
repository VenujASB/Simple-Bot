import asyncio
from pyrogram import Client

api_id = 12345
api_hash = "0123456789abcdef0123456789abcdef"
bot_token = 

async def main():
    async with Client("bot", api_id, api_hash, bot_token) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
