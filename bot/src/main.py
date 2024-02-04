import os
from discord import Intents, Client
from packages.event_module import message_handler

TOKEN = os.getenv("TOKEN")

intents = Intents.all()
client = Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_message(message):
    await message_handler(message)

# Bot起動
client.run(TOKEN)