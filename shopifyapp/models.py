from django.db import models
from django.utils import timezone

# Create your models here.

class Subscribe(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email

from django.db import models
from django.utils import timezone

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  # Use EmailField for validation
    phone = models.CharField(max_length=20)    # Reduced max length for phone
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VehicleReport(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, default='000-000-0000')
    description = models.TextField()
    vehicle_image = models.ImageField(upload_to='media/images')
    datetime = models.DateTimeField(default=now)  # Correct default

    def __str__(self):
        return self.customer_name
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class VehicleReport(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, default='000-000-0000')
    description = models.TextField()
    vehicle_image = models.ImageField(upload_to='media/images')
    datetime = models.DateTimeField(default='YYYY-MM-DD HH:MM:SS')



    def __str__(self):
        return self.customer_name

class WebsiteContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LoginForms(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class CreateForm(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname




class ImageModel(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField()
    vehicle_image = models.ImageField(upload_to='images/')
    datetime = models.DateTimeField(auto_now_add=True)


    def  __str__(self):
        return self.customer_name