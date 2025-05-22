from django_q.tasks import async_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_notification_email(user_id, notification_type, context):
    """
    Actual task that will be executed asynchronously
    """
    from customuser.models import CustomUser
    
    try:
        user = CustomUser.objects.get(id=user_id)
        
        # Email subject and template selection based on notification type
        email_templates = {
            "booking_confirmation": {
                'subject': f"Booking Confirmation #{context.get('booking_id', '')}",
                'template': 'emails/booking_confirmation.html'
            },
            "new_booking_received": {
                'subject': f"New Booking for {context.get('accommodation_name', 'your accommodation')}",
                'template': 'emails/new_booking_received.html'
            },
            "booking_cancellation": {
                'subject': f"Booking Cancelled #{context.get('booking_id', '')}",
                'template': 'emails/booking_cancelled.html'
            }
        }
        
        template_config = email_templates.get(notification_type, {
            'subject': "Notification from BlazeNest",
            'template': 'emails/general_notification.html'
        })
        
        # Render email content
        html_content = render_to_string(template_config['template'], {
            'user': user,
            **context
        })
        
        # Create and send email
        msg = EmailMultiAlternatives(
            template_config['subject'],
            html_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return True
    except Exception as e:
        # You should log this error to your error tracking system
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to send notification: {str(e)}")
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