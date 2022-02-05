from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from groupizer import models, serializers

class MembershipViewSet(viewsets.ModelViewSet):
	queryset = models.Membership.objects.all()
	serializer_class = serializers.MembershipSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = models.Group.objects.all()
	serializer_class = serializers.GroupSerializer

class AdViewSet(viewsets.ModelViewSet):
	queryset = models.Ad.objects.all()
	serializer_class = serializers.AdSerializer

class InterestViewSet(viewsets.ModelViewSet):
	queryset = models.Interest.objects.all()
	serializer_class = serializers.InterestSerializer

	@action(methods=["post"], detail=False)
	def subscribe(self, request):
		interest_ids = request.data.get('id')

		if type(interest_ids) != list:
			interest_ids = [interest_ids]
		
		for interest_id in interest_ids:
			try:
				interest = models.Interest.objects.get(id=interest_id)
				interest.users.add(request.user)
			except:
				return Response(status=status.HTTP_400_BAD_REQUEST)
		user_interests = models.Interest.objects.filter(users=request.user)
		user_interests_serializer = serializers.InterestSerializer(user_interests, many=True)
		return Response(user_interests_serializer.data, status=status.HTTP_200_OK)