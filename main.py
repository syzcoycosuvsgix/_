import multi, configparser, json
from multiprocess import Process

config = configparser.ConfigParser()
config.read("config.ini")
tokens = json.loads(config["json"]["root"])["TOKENS"]
text = json.loads(config["json"]["root"])["TEXT"]
api_id = config["pyrogram"]["api_id"]
api_hash = config["pyrogram"]["api_hash"]

print("total accounts> %d \n" % len(tokens))
input("1) flood to chat\n\n>> ")

for token in tokens:
    multi.Client(
    session_name=token,
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
    messages=text).start()
    print(f"Log as {token[:5]}")
print("send <a> to chat")
pyrogram.idle()
