import pyrogram, random

def Client(session_name, api_id, api_hash, bot_token, messages):
    bot = pyrogram.Client(session_name, api_id, api_hash, bot_token=bot_token)
    @bot.on_message()
    async def o(client, message):
        if message.text != "a":
            return
        while True:
            await client.send_message(message.chat.id, random.choice(messages))
    bot.run()
