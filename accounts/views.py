from rest_framework import viewsets

from accounts import models, serializers

class UserViewSet(viewsets.ModelViewSet):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer