from django.core.mail import send_mail
from django.conf import settings
from django_q.tasks import async_task
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_booking_confirmation_email(booking_id):
    from .models import Booking
    try:
        booking = Booking.objects.get(id=booking_id)
        subject = f"Bookinf confirmation for {booking.accommodation.name}"
    # HTML email
        context ={
            'user':booking.user,
            'accommodation': booking.accommodation,
            'total_amount': booking.total_amount,
            'support_email': settings.DEFAULT_FROM_EMAIL
        }
        html_message = render_to_string('booking/confirmation_email.html', context)
        plain_message = strip_tags(html_message)
        send_mail(
                subject=subject,
                message=plain_message,
                html_message=html_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.user.email],
                fail_silently=False,
            )
    except Booking.DoesNotExist:
        if settings.DEBUG:
            print(f"Booking not found: {e}")
    
def async_send_booking_confirmation(booking_id):
    # wrapper for sending async notification
    async_task(
        send_booking_confirmation_email,
        booking_id,
        hook=None,
        group="booking_notifications"
    )