import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from room.models import Room, Message
from room.utils import get_room as db_get_room, get_message as db_get_message
from utils.core import generate_id, model_to_list_dicts

# ======================================================================================================================
# = rooms ==============================================================================================================
# ======================================================================================================================

def create_room(request: HttpRequest):
    data = json.loads(request.body.decode('utf-8'))

    name = data.get('name')
    description = data.get('description')

    if (name == None or description == None or name == '' or description == ''):
        return HttpResponse(status = 400, content = 'missing data')

    existing_room = db_get_room(name, True)

    if (existing_room != None):
        return HttpResponse(status = 400, content = 'room with name ' + name + ' already exists')

    room = Room.objects.create(
        id = generate_id('room'),
        name = name,
        description = description
    )

    return JsonResponse(model_to_dict(room))

# get

def get_room(request: HttpRequest, id: str):
    room = db_get_room(id, False)

    if (room == None):
        return HttpResponse(status = 400, content = 'room with id ' + id + ' doesn\'t exist')

    return JsonResponse(model_to_dict(room))

# get all

def get_all_rooms(request: HttpRequest):
    rooms = model_to_list_dicts(Room.objects.filter())

    return JsonResponse({ 'data': rooms })

# delete

def delete_room(request: HttpRequest, id: str):
    room = db_get_room(id, False)

    if (room == None):
        return HttpResponse(status = 400, content = 'room with id ' + id + ' doesn\'t exist')

    Room.objects.get(id = id).delete()

    return HttpResponse('room deleted')

# ======================================================================================================================
# = messages ===========================================================================================================
# ======================================================================================================================

def create_message(request: HttpRequest, room_id: str):
    room = db_get_room(room_id, False)

    if (room == None):
        return HttpResponse(status = 400, content = 'room with id ' + room_id + ' doesn\'t exist')

    data = json.loads(request.body.decode('utf-8'))

    content = data.get('content')
    # author_id = data.get('author_id')

    # or author_id == None or author_id == ''
    if (content == None or content == ''):
        return HttpResponse(status = 400, content = 'missing data')

    message = Message.objects.create(
        id = generate_id('msg'),
        # author_id = author_id,
        content = content,
        room_id = room_id,
    )

    return JsonResponse(model_to_dict(message))

# get

def get_message(request: HttpRequest, id: str):
    message = db_get_message(id)

    if (message == None):
        return HttpResponse(status = 400, content = 'message with id ' + id + ' doesn\'t exist')

    return JsonResponse(model_to_dict(message))

# get all

def get_room_messages(request: HttpRequest, room_id: str):
    messages = model_to_list_dicts(Message.objects.filter(room_id = room_id))

    return JsonResponse({ 'data': messages })

# delete

def delete_message(request: HttpRequest, id: str):
    message = db_get_message(id)

    if (message == None):
        return HttpResponse(status = 400, content = 'message with id ' + id + ' doesn\'t exist')

    Message.objects.get(id = id).delete()

    return HttpResponse('message deleted')
