from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    hotel = models.CharField(max_length=250)
    payment = models.CharField(max_length=250)
