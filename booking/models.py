from django.db import models
from customuser.models import CustomUser
from accommodation.models import Accommodation

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accommondation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, null=True, blank=False)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return f"{self.user} - {self.accommondation}"