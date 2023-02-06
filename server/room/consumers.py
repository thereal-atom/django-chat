import json
import requests
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

base_url = 'http://localhost:50451/room/'

class RoomConsumer(WebsocketConsumer):
    def connect(self):

        room_id = self.scope["url_route"]["kwargs"]["room_id"]

        res = requests.get(base_url + room_id)

        if res.status_code < 200 or res.status_code >= 300:
            self.close()

        room = res.json()

        self.room_group_name = room['name'].replace(' ', '-')
        self.room_id = room_id

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'room_message',
                'message': data,
            }
        )

    def room_message(self, event):
        message = event['message']

        payload = { 'content': message['content'] }
        headers = { 'Content-Type': 'application/json' }

        res = requests.post('http://localhost:50451/room/' + self.room_id + '/message/', headers = headers, json = payload)

        if res.status_code >= 200 and res.status_code < 300:
            self.send(text_data = json.dumps({
                'type': 'chat',
                'message': res.json(),
            }))
        else:
            self.send(text_data = json.dumps({
                'type': 'error',
                'message': 'unknown' if res.text == None else res.text,
            }))