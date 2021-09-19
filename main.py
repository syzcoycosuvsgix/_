from pyrogram import Client, idle
import sys

app = Client("diamond")

if __name__ == "__main__":
    app.start()
    if len(sys.argv) == 4:
        try:
            type = sys.argv[3]
            if type == "update": text = "**Обновление установлено успешно!**"
            else: text = "**Перезагрузка прошла успешно!**"
            app.send_message(
                chat_id=sys.argv[1], text=text, reply_to_message_id=int(sys.argv[2])
            )
        except:
            app.send_message(
                chat_id=sys.argv[1], text=text
            )
    idle()
