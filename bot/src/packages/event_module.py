from .hello import handle_hello

events_function = {
    'hello': handle_hello,
}

async def message_handler(message):
    print(message.content)
    event_function = events_function.get(message.content, None)
    if event_function != None:
        await event_function(message)