from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CoWorkingViewSet, IncubatorViewSet, IncubatorApplicationViewSet, CoWorkingApplicationViewSet

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('coworkings', CoWorkingViewSet)
router.register('incubators', IncubatorViewSet)
router.register('incubator-app', IncubatorApplicationViewSet)
router.register('coworking-app', CoWorkingApplicationViewSet)

urlpatterns = [
    path('', include(router.urls))
]