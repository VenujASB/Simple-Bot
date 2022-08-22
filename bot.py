from pyrogram import Client, filters


api_id = 18862638
api_hash = "2a4a8dc0c1f6c9cb65f9f144439558ae"
bot_token = "5713884943:AAGBn_ESkg3y0VZurKkFnFf2pzbtfnCWSmQ"
string_session = "BQBrfiEqIY7OM2aMMpAbT-GoaiunVq3aiQnFAXXBO6zCyqSu4lAf7B4_oxSmpX4AQ82V3qcBpJJgZ7taCfunOEpChFsUnotPUJN5gkCflvU8d3b9c0v4k_JTiX3uiOsFBut91GOeMn4-0CvqEVvrUkMRi3Z8KXyhGjyeqbxRdwTRBAC9nGKByOA9V_qGvGh93qVcSpI3Rx5Z7EDRs41o4hjTMC1_KBWdRbJM_pT_vLPHIQmfCiix7cyTFwoQa0zfo0PXsuGrpamzccPp0QJ1HAad5fYzfmjfn02dQdok_dCl7PN2SVMWZvZ8h6nSJtPVyXlc2b193_6WO3WsRW4sK3HpdkfIGgA"

bot = Client("bot", api_id, api_hash, bot_token, string_session)


@bot.on_message(filters.regex("hi"))
async def send_hi(_, message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = "Hello!")   
                       
print("Bot is alive!")
bot.run()
