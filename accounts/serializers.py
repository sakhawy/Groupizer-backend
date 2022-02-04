from rest_framework import serializers

from accounts import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('name', 'email', 'password')