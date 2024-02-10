import os
from discord import Intents, Client
from discord.ext import tasks
from datetime import datetime, timedelta, timezone

from packages.event_module import message_handler
from packages.voice_notice import voice_access_notice
from packages.get_weather import WeatherInfo

TOKEN = os.getenv("TOKEN")
VOICE_CHANNEL_ID= int(os.getenv("VOICE_CHANNEL_ID"))
TEXT_CHANNEL_ID = int(os.getenv("TEXT_CHANNEL_ID"))

intents = Intents.all()
client = Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    loop.start()

# メッセージ対応用関数
@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message_handler(message)

# 
@client.event
async def on_voice_state_update(user, before, after):
    await voice_access_notice(user, before, after, client, TEXT_CHANNEL_ID, VOICE_CHANNEL_ID)


@tasks.loop(seconds=60)
async def loop():
    current_japan_time = datetime.now(timezone(timedelta(hours=+9), "JST")).strftime("%H:%M")
    if (current_japan_time == "07:00"):
        weather = WeatherInfo(client)
        await weather.check_rain()

# Bot起動
client.run(TOKEN)
