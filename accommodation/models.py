from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Accommodation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    amenities = models.CharField(max_length=255, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    availability_status = models.BooleanField(default=True, null=True, blank=True)
    accommodation_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name