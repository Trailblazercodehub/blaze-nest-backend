from django.db import models
from customuser.models import CustomUser
from accommodation.models import Accommodation

# Create your models here.
class SecurityReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    accommondation = models.ForeignKey(Accommodation, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    
    