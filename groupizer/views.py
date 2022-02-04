from rest_framework import viewsets

from groupizer import models, serializers

class AdViewSet(viewsets.ModelViewSet):
	queryset = models.Ad.objects.all()
	serializer_class = serializers.AdSerializer

class InterestViewSet(viewsets.ModelViewSet):
	queryset = models.Interest.objects.all()
	serializer_class = serializers.InterestSerializer