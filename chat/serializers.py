from rest_framework import serializers

from chat import models

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Message
		fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Chat
		fields = ('id', 'title', 'group', 'messages')

	messages = MessageSerializer(many=True, read_only=True)
