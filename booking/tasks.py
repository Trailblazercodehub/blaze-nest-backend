from django_q.tasks import async_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()

def send_notfiication_email(user_id, subject, message):
    try:
        user = User.objects.get(id=user_id)
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL
            [user.email],
            fail_silently=False,
        )
        return f"Email sent to {user.email}"
    except User.DoesNotExist:
        return "User not found"
    except Exception as e:
        return f"Error sending email: {str(e)}"