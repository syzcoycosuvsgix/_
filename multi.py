import pyrogram, random

def Client(session_name, api_id, api_hash, bot_token):
    return pyrogram.Client(session_name, api_id, api_hash, bot_token=bot_token)
