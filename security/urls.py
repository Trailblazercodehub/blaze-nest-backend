from django.urls import path, include
from .views import SecurityReportViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', SecurityReportViewSet)

urlpatterns = [
    path('', include(router.urls))
]
