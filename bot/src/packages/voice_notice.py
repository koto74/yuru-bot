async def voice_access_notice(user, before, after, client, txt_id, vc_id):
    if before.channel != after.channel:
        bot_room = client.get_channel(txt_id)
        if before.channel is not None and before.channel.id == vc_id:
            await bot_room.send("**" + before.channel.name+ "** から __"+ user.display_name + "__ が退出")
        if after.channel is not None and after.channel.id == vc_id:
            await bot_room.send("**" + after.channel.name + "** に、__" + user.display_name + "__  が参加")