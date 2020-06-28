from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    dob = models.CharField(max_length=128)

class imageReport(models.Model):
    image = models.TextField()
