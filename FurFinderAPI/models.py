from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    date = models.CharField(max_length=128)

class FidoFinder(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    petid = models.CharField(max_length=128)

class HelpingLostPets(models.Model):
    status = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    color = models.CharField(max_length=128)

class LostMyDoggie(models.Model):
    image = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    zip = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    date = models.CharField(max_length=128)

class PawBoost(models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    petid = models.CharField(max_length=128)
    image = models.CharField(max_length=128)

class PetKey(models.Model):
    name = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    age = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    image = models.CharField(max_length=128)

class TabbyTracker(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    image = models.CharField(max_length=128)
    petid = models.CharField(max_length=128)

