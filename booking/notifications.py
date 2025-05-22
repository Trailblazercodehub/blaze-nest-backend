from django_q.tasks import async_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_notification_email(user_id, notification_type, context):
    """
    Actual task that will be executed asynchronously
    """
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    try:
        user = User.objects.get(id=user_id)
        
        # Email subject and template selection based on notification type
        if notification_type == "booking_confirmation":
            subject = f"Booking Confirmation #{context['booking_id']}"
            template = 'emails/booking_confirmation.html'
        elif notification_type == "custom_message":
            subject = "Notification About Your Booking"
            template = 'emails/custom_notification.html'
        else:
            subject = "Notification from BlazeNest"
            template = 'emails/general_notification.html'
        
        # Render email content
        html_content = render_to_string(template, {
            'user': user,
            **context
        })
        
        # Create and send email
        msg = EmailMultiAlternatives(
            subject,
            html_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return True
    except Exception as e:
        # Log error here
        return False

def notify_user(user, notification_type, context):
    """
    Queue notification task
    """
    async_task(
        'booking.notifications.send_notification_email',
        user.id,
        notification_type,
        context
    )