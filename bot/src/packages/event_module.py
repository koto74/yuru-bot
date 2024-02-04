from .hello import handle_hello

event_functions = {
    'hello': handle_hello,
}

async def message_handler(message):
    print(message.content)
    event_function = event_functions.get(message.content, None)
    if event_function != None:
        await event_function(message)