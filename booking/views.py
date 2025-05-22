from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Booking
from .serializers import BookingSerializer
from .notifications import notify_user

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related('user', 'accommondation')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users can only see their own bookings
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        self._send_creation_notifications(booking)

    def perform_update(self, serializer):
        booking = serializer.save()
        self._send_update_notifications(booking)

    def perform_destroy(self, instance):
        self._send_cancellation_notifications(instance)
        super().perform_destroy(instance)

    def _send_creation_notifications(self, booking):
        """Send notifications when a booking is created"""
        # Notification to guest
        notify_user(
            user=booking.user,
            notification_type="booking_confirmation",
            context={
                'booking_id': booking.id,
                'accommodation_name': booking.accommondation.name if booking.accommondation else "N/A",
                'total_amount': booking.total_amount,
                'booking_date': timezone.now().strftime("%Y-%m-%d %H:%M"),
            }
        )

        # Notification to accommodation owner
        if booking.accommondation and booking.accommondation.owner:
            notify_user(
                user=booking.accommondation.owner,
                notification_type="new_booking_received",
                context={
                    'booking_id': booking.id,
                    'guest_name': booking.user.get_full_name() or booking.user.username,
                    'accommodation_name': booking.accommondation.name,
                    'total_amount': booking.total_amount,
                    'booking_date': timezone.now().strftime("%Y-%m-%d %H:%M"),
                }
            )

    def _send_update_notifications(self, booking):
        """Send notifications when a booking is updated"""
        notify_user(
            user=booking.user,
            notification_type="booking_updated",
            context={
                'booking_id': booking.id,
                'accommodation_name': booking.accommondation.name if booking.accommondation else "N/A",
                'changes': "Your booking details have been updated",
            }
        )

    def _send_cancellation_notifications(self, booking):
        """Send notifications when a booking is cancelled"""
        notify_user(
            user=booking.user,
            notification_type="booking_cancelled",
            context={
                'booking_id': booking.id,
                'accommodation_name': booking.accommondation.name if booking.accommondation else "N/A",
                'cancellation_date': timezone.now().strftime("%Y-%m-%d %H:%M"),
            }
        )

        if booking.accommondation and booking.accommondation.owner:
            notify_user(
                user=booking.accommondation.owner,
                notification_type="booking_cancelled_owner",
                context={
                    'booking_id': booking.id,
                    'guest_name': booking.user.get_full_name() or booking.user.username,
                    'accommodation_name': booking.accommondation.name,
                    'cancellation_date': timezone.now().strftime("%Y-%m-%d %H:%M"),
                }
            )

class BookingNotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        booking_id = request.data.get('booking_id')
        message = request.data.get('message')
        notification_type = request.data.get('notification_type', 'custom_message')
        
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
            
            # Send async notification
            notify_user(
                user=request.user,
                notification_type=notification_type,
                context={
                    'booking_id': booking.id,
                    'message': message,
                    'accommodation_name': booking.accommondation.name if booking.accommondation else "N/A",
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