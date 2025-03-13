from django.urls import path

from .views import AccommodationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccommodationViewSet)

urlpatterns = router.urls