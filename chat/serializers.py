from rest_framework import serializers

from chat import models
from accounts.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Message
		fields = '__all__'

	user = UserSerializer(read_only=True)

class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Chat
		fields = ('id', 'title', 'group', 'messages')

	messages = MessageSerializer(many=True, read_only=True)
