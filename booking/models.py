from django.db import models
from customuser.models import CustomUser
from accommodation.models import Accommodation
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import async_send_booking_confirmation


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, null=True, blank=False)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return f"{self.user} - {self.accommodation}"

@receiver(post_save, sender=Booking)
def booking_post_save(Sender, instance, created, **kwargs):
    if created:
        async_send_booking_confirmation(instance.id)