from django.db import models

# Create your models here.
class infrared(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    infrared_data = models.CharField(max_length=100)
    get_data_time = models.DateTimeField(auto_now=True)
class ultrasonic(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    ultrasonic_data = models.CharField(max_length=100)
    get_data_time = models.DateTimeField(auto_now=True)
class images(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    images_data = models.ImageField()
    get_data_time = models.DateTimeField(auto_now=True)