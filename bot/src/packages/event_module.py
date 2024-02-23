from .messages.hello import handle_hello
from .messages.orochi import handle_orochi

event_functions = {
    "hello": handle_hello,
    "名言": handle_orochi,
}

async def message_handler(message):
    event_function = event_functions.get(message.content, None)
    if event_function != None:
        await event_function(message)
