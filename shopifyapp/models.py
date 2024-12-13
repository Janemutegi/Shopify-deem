from django.db import models
from django.utils import timezone

# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  # Use EmailField for validation
    phone = models.CharField(max_length=20)    # Reduced max length for phone
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class VehicleReport(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, default='000-000-0000')
    description = models.TextField()
    vehicle_image = models.ImageField(upload_to='media/images')
    datetime = models.DateTimeField(default=timezone.now)  # Correct default

    def __str__(self):
        return self.customer_name


class LoginForms(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email





