from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from groupizer import models

class AdSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Ad
		fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Interest
		fields = '__all__'