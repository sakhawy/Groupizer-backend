from django.db import models
from django.conf import settings

from groupizer.models import Group

class Chat(models.Model):
	group = models.OneToOneField(Group, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.title

class Message(models.Model):
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
	text = models.TextField()
	sent = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text