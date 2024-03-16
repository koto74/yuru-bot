import asyncio

from .messages.hello import handle_hello
from .messages.orochi import handle_orochi

event_functions = {
    "hello": handle_hello,
    "名言": handle_orochi,
}


async def message_handler(message):
    event_function = event_functions.get(message.content, None)
    if event_function != None:
        async with message.channel.typing():
            await asyncio.sleep(2)
        await event_function(message)
