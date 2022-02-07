import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db.models import Q

from chat import models
from groupizer.models import Membership

class ChatConsumer(WebsocketConsumer):
	def connect(self):

		self.chat_id = self.scope['url_route']['kwargs']['chat']
		self.chat_name = 'chat_%s' % self.chat_id
		
		self.accept()
		
		# Check chat existance
		try:
			chat = models.Chat.objects.get(id=self.chat_id)

			self.user = self.scope["user"]

			# Check if user is a memeber
			role = Q(role=Membership.MEMBER) | Q(role=Membership.ADMIN) 
			self.user = chat.group.memberships.filter(user=self.user, role=role).first()

			assert self.user != None # Raise when self.user is none

		except:
			self.close() 
			return

		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.chat_name,
			self.channel_name
		)

		# Close anon users' connection
		if self.user.is_anonymous:
			self.disconnect(403)
			self.close()
		
	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.chat_name,
			self.channel_name
		)

	# Receive message from WebSocket
	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		# Send message to room group
		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message
			}
		)

	# Receive message from room group
	def chat_message(self, event):
		message = event['message']

		# Send message to WebSocket
		self.send(text_data=json.dumps({
			'message': message
		}))