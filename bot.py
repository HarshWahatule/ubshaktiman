from pyrogram import Client
from config import Config

ubs = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)

@ubs.on_message()
def echo(client, message):
    print(message.text)