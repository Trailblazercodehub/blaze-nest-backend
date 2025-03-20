from django.urls import path, include

from .views import AccommodationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccommodationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]