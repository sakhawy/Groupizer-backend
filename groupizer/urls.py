from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from groupizer import views

router = DefaultRouter()

router.register(r'ads', views.AdViewSet)
router.register(r'interests', views.InterestViewSet)

urlpatterns = [

]