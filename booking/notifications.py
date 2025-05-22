from .task import send_notfiication_email
from django_q.tasks import async_task

def notify_user(user, subject, message):
    async_task(
        send_notfiication_email,
        user.id,
        subject
    )