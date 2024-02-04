async def voice_access_notice(user, before, after):
    if before.channel != after.channel:
        bot_room = client.get_channel(TEXT_CHANNEL_ID)
        if before.channel is not None and before.channel.id == VOICE_CHANNEL_ID:
            await bot_room.send("**" + before.channel.name+ "** から __"+ user.display_name + "__ が退出")
        if after.channel is not None and after.channel.id == VOICE_CHANNEL_ID:
            await bot_room.send("**" + after.channel.name + "** に、__" + user.display_name + "__  が参加")