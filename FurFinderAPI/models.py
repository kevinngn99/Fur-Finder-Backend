from django.db import models

class Pet(models.Model):
    name = models.TextField()
    gender = models.TextField()
    size = models.TextField()
    date = models.TextField()
    age = models.TextField()
    state = models.TextField()
    zip = models.TextField()
    location = models.TextField()
    breed = models.TextField()
    image = models.TextField()

class FidoFinder(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class HelpingLostPets(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class LostMyDoggie(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class PawBoost(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class PetKey(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class TabbyTracker(models.Model):
    age = models.TextField()
    breed = models.TextField()
    city = models.TextField()
    color = models.TextField()
    date = models.TextField()
    gender = models.TextField()
    image = models.TextField()
    location = models.TextField()
    name = models.TextField()
    petid = models.TextField()
    size = models.TextField()
    status = models.TextField()
    zip = models.TextField()

class imageReport(models.Model):
    image = models.TextField()
