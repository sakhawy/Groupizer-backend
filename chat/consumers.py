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
			self.chat = models.Chat.objects.get(id=self.chat_id)

			self.user = self.scope["user"]

			# Check if user is a memeber
			query = Q(Q(role=Membership.MEMBER) | Q(role=Membership.ADMIN)) & Q(user=self.user)
			self.membership = self.chat.group.memberships.filter(query).first()

			assert self.membership != None # Raise when self.membership is none

		except:
			self.close() 
			return

		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.chat_name,
			self.channel_name
		)
		
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
			self.chat_name,
			{
				'type': 'chat_message',
				'message': message
			}
		)

	# Receive message from room group
	def chat_message(self, event):
		message = event['message']

		# Add message to chat
		models.Message.objects.create(
			user=self.user,
			text=message,
			chat=self.chat,
		)

		# Send message to WebSocket
		self.send(text_data=json.dumps({
			'message': message
		}))