from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from chat import models, serializers

class ChatViewSet(viewsets.ModelViewSet):
	queryset = models.Chat.objects.all()
	serializer_class = serializers.ChatSerializer

class MessageViewSet(viewsets.ModelViewSet):
	queryset = models.Message.objects.all()
	serializer_class = serializers.MessageSerializer