from django.urls import path, include
from rest_framework import routers
from .views import BookingViewSet, BookingNotificationAPIView

router = routers.DefaultRouter()
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('bookings/<int:pk>/notify/', BookingNotificationAPIView.as_view(), name='booking-notification'),
]