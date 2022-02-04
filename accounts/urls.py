from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = [

]