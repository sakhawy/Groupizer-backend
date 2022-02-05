from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ('id', 'name', 'email', 'password', 'token')

	token = serializers.SerializerMethodField('get_token')

	def get_token(self, obj):
		token = str(RefreshToken.for_user(obj).access_token)
		return token

	def create(self, validated_data):
		password = validated_data.pop('password')
		user = models.User(**validated_data)
		user.set_password(password)
		user.save()

		return user