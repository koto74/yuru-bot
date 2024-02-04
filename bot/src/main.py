import os
from discord import Intents, Client
from packages.event_module import message_handler
from packages.voice_notice import voice_access_notice

TOKEN = os.getenv("TOKEN")
VOICE_CHANNEL_ID= int(os.getenv("VOICE_CHANNEL_ID"))
TEXT_CHANNEL_ID = int(os.getenv("TEXT_CHANNEL_ID"))

intents = Intents.all()
client = Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print("Ready!")


@client.event
async def on_voice_state_update(user, before, after):
    voice_access_notice(user, before,after)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message_handler(message)

# Bot起動
client.run(TOKEN)
