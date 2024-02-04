import os
from discord import Intents, Client
from packages.event_module import message_handler

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
async def on_message(message):
    if message.author.bot:
        return
    await message_handler(message)
@client.event
async def on_voice_state_update(user, before, after):
    if before.channel != after.channel:
        botRoom = client.get_channel(TEXT_CHANNEL_ID)
        if before.channel is not None and before.channel.id == VOICE_CHANNEL_ID:
            await botRoom.send("**" + before.channel.name+ "** から __"+ user.display_name + "__ が退出")
        if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID:
            await botRoom.send("**" + after.channel.name + "** に、__" + user.display_name + "__  が参加")    

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message_handler(message)

# Bot起動
client.run(TOKEN)
