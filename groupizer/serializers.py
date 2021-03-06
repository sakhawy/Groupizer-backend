from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from groupizer import models
from accounts.serializers import UserSerializer
from chat.models import Chat

class MembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Membership
		fields = '__all__'

	user = UserSerializer(read_only=True)

	def create(self, validated_data):
		# Get the user
		user = self.context["request"].user
		
		role = models.Membership.PENDING

		membership = models.Membership.objects.create(user=user, role=role, **validated_data)
		
		return membership

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Group
		fields = ('id', 'title', 'ad', 'memberships', 'chat')

	memberships = MembershipSerializer(many=True, read_only=True)

class AdSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Ad
		fields = '__all__'

	user = UserSerializer(read_only=True)
	group = GroupSerializer(read_only=True)

	def create(self, validated_data):
		# Get the authed user
		user = self.context["request"].user

		# Create a group for the ad
		group = models.Group.objects.create(
			title = validated_data["title"],
		)

		# Create a chat
		chat = Chat.objects.create(
			group=group,
			title=group.title 
		)

		# Create an admin membership
		membership = models.Membership.objects.create(
			role = models.Membership.ADMIN,
			user=user,
			group=group
		)

		# Create the ad using validated_data + above-created data
		ad = models.Ad.objects.create(**validated_data)
		ad.user = user
		ad.group = group
		ad.save()

		return ad
		

class InterestSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Interest
		fields = '__all__'