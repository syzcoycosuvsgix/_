import sys, configparser, os

help = {"Pidor": {"commands": "hack/you", "description": "описание"}}

path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(path)

def get_prefix():
    return config.get("database", "prefix")
try:
    prefix = get_prefix()
except:
    config.set("database", "prefix", ".")
    prefix = "."

def get_plugins(type):
    prefix = get_prefix()
    if type == "all":
        string = "<b>Помощь для</b> <a href='t.me/pidor'>Diamond-Userbot</a>\nДля получения дополнительной информации о том, как использовать плагин, введите <code>{prefix}help <имя плагина></code>\n<b>Доступные плагины:</b>\n"
        for plug in help:
            commands = "<code>" + plug["commands"].replace("/", "</code>, <code>") + "</code>"
            string += f"• <b>{plug["name"]}</b>: {commands}\n"
        return string + "\n\nДля выгрузки плагина используйте <code>{prefix}unloadplugin <имя плагина></code>"
