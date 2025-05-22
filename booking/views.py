from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

# new imports 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .notification import notify_user


# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    


class BookingCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            booking = serializer.save(user=request.user)
            
            # send async notification
            notify_user(
                user=request.user,
                notification_type="booking_confirmation",
                context={
                    'booking_id': booking.id,
                    'date': booking.date,
                    'time': booking.time,
                }
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
class BookingNotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        booking_id = request.data.get('booking_id')
        message = request.data.get('message')
        
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
            
            # Send async notification
            notify_user(
                user=request.user,
                notification_type="custom_message",
                context={
                    'booking_id': booking.id,
                    'message': message,
                }
            )
            
            return Response(
                {"status": "Notification queued successfully"},
                status=status.HTTP_202_ACCEPTED
            )
        except Booking.DoesNotExist:
            return Response(
                {"error": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND
            )