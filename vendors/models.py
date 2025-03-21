from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class VendorManager(BaseUserManager):
    def create_vendor(self, email, business_name, password=None):
        if not email:
            raise ValueError("Vendors must have an email address")
        vendor = self.model(email=self.normalize_email(email), business_name=business_name)
        vendor.set_password(password)
        vendor.save(using=self._db)
        return vendor


class Vendor(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    business_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = VendorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['business_name']

    def __str__(self):
        return self.business_name
