from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    msi = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    aircondition = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    carimage = models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.name



class BookCar(models.Model):
    carname = models.CharField(max_length=50)
    pickup = models.CharField(max_length=50)
    pickupdatetime = models.DateTimeField(default=datetime.now, blank=True)
    dropoff = models.CharField(max_length=50)
    dropoffdatetime = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)

    def __str__(self):
        return self.name

