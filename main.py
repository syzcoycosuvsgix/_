import multi, configparser, json, db
from multiprocessing import Process as Thread

config = configparser.ConfigParser()
config.read("config.ini")

tokens = db.ROOT["TOKENS"]
text = db.ROOT["TEXT"]
api_id = config["pyrogram"]["api_id"]
api_hash = config["pyrogram"]["api_hash"]

print("total accounts> %d \n" % len(tokens))

for token in tokens:
    Thread(multi.Client(
    session_name=token,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
    messages=text)).start()
    print(f"Log as {token[:5]}")
print("send <a> to chat")
pyrogram.idle()
