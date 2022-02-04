from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from accounts import models, serializers

class UserViewSet(viewsets.ModelViewSet):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer

	def get_queryset(self):
		return models.User.objects.filter(id=self.request.user.id)

	@action(methods=["post"], detail=False)
	def login(self, request):
		email = request.data.get('email', None)
		password = request.data.get('password', None)
		
		user = authenticate(email=email, password=password)
		if user is not None:
			user_serializer = serializers.UserSerializer(user)
			return Response(user_serializer.data, status=status.HTTP_200_OK)
		return Response(status=status.HTTP_400_BAD_REQUEST)