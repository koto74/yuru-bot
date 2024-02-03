import os
from discord import Intents, Client

TOKEN = os.getenv("TOKEN")

intents = Intents.all()
client = Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print("Ready!")

# Bot起動
client.run(TOKEN)