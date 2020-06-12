from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    date = models.CharField(max_length=128)

