from pyrogram import Client,filters
from config import Config
from filters.command_filter import filter_cmd

ubs = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)

@ubs.on_message(filters.create(filter_cmd, kwargs))
def echo(client, message):
    print(message.text)

ubs.run()