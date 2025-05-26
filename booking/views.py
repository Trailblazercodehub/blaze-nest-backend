from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from .tasks import async_send_booking_confirmation

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def perform_create(self, serializer):
        booking = serializer.save()
        async_send_booking_confirmation(booking.id)