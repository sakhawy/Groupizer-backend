from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from groupizer import models

class MembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Membership
		fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Group
		fields = '__all__'

	memberships = MembershipSerializer(many=True, read_only=True)

class AdSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Ad
		fields = '__all__'

	def create(self, validated_data):
		# Get the authed user
		user = self.context["request"].user

		# Create a group for the ad
		group = models.Group.objects.create(
			title = validated_data["title"],
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