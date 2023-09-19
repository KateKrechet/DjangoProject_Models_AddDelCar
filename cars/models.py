from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=10)
    producer = models.CharField(max_length=10)
    year = models.IntegerField()
    number = models.CharField(max_length=9)