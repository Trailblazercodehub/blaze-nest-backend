from django.urls import path, include
from rest_framework import routers
from .views import MaintenanceReportViewSets

router = routers.DefaultRouter()
router.register('', MaintenanceReportViewSets)

urlpatterns = [
    path('', include(router.urls))
]
