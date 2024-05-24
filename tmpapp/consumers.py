import json
from channels.generic.websocket import AsyncWebsocketConsumer

class YourConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		print("WebSocket connection opened")
		await self.accept()

	async def disconnect(self, close_code):
		print("WebSocket connection closed")
		pass

	async def receive(self, text_data):
		print(f"Received message: {text_data}")
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		await self.send(text_data=json.dumps({
			'message': message
		}))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        print('room_group_name:', self.room_group_name, "connected")
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message = text_data_json['message']
        print('message:', message, "received")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': message_type,
                'message': message,
                'user': self.channel_name
            }
        )

    async def update_ball_position(self, event):
        message = event['message']
        user = event['user']
        print(f'message: {message} from user {user} broadcasting')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'update_ball_position',
            'message': message,
            'user': user
        }))