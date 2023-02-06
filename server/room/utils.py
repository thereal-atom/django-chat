from room.models import Room, Message

def get_room(id_or_name: str, get_by_name: bool) -> Room:
    room = None

    try:
        if get_by_name == True:
            room = Room.objects.get(name = id_or_name)
        else:
            room = Room.objects.get(id = id_or_name)
    except Room.DoesNotExist:
        room = None

    return room

def get_message(id: str) -> Message:
    message = None

    try:
        message = Message.objects.get(id = id)
    except Message.DoesNotExist:
        message = None

    return message