from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet)
router.register(r'api/bloodreq', BloodRequestViewSet, basename='bloodreq')


urlpatterns = [
    path('', include(router.urls)),
]