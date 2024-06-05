import os
from discord import Intents, app_commands, Interaction, Client
from discord.ext import tasks
from datetime import datetime, timedelta, timezone

from packages.event_module import message_handler
from packages.voice_notice import voice_access_notice
from packages.get_weather import WeatherInfo
from commands.robokssay import robokssay

TOKEN = os.getenv("TOKEN")
ENTRY_EXIT_MONITOR_VOICE_CHANNEL_ID = int(os.getenv("ENTRY_EXIT_MONITOR_VOICE_CHANNEL_ID"))
ENTRY_EXIT_MONITOR_NOTIFICATION_CHANNEL_ID = int(os.getenv("ENTRY_EXIT_MONITOR_NOTIFICATION_CHANNEL_ID"))
WEATHER_NOTIFICATION_CHANNEL_ID = int(os.getenv("WEATHER_NOTIFICATION_CHANNEL_ID"))

intents = Intents.all()
client = Client(intents=intents)
tree = app_commands.CommandTree(client)


# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    await tree.sync()
    loop.start()


# メッセージ対応用関数
@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message_handler(message)


# ボイスチャンネル参加/退出時の通知
@client.event
async def on_voice_state_update(user, before, after):
    await voice_access_notice(
        user,
        before,
        after,
        client,
        ENTRY_EXIT_MONITOR_NOTIFICATION_CHANNEL_ID,
        ENTRY_EXIT_MONITOR_VOICE_CHANNEL_ID,
    )


# 定期実行関数
@tasks.loop(seconds=60)
async def loop():
    current_japan_time = datetime.now(timezone(timedelta(hours=+9), "JST")).strftime("%H:%M")
    if current_japan_time == "07:00":
        weather = WeatherInfo(client)
        await weather.send_rain_alert(WEATHER_NOTIFICATION_CHANNEL_ID)


tree.add_command(robokssay)


# Bot起動
client.run(TOKEN)
