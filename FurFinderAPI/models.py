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
    image=models.TextField()

class ReportPets(models.Model):
    name = models.TextField()
    gender = models.TextField()
    size = models.TextField()
    date = models.TextField()
    age = models.TextField()
    state = models.TextField()
    zip = models.TextField()
    location = models.TextField()
    breed = models.TextField()
    image=models.TextField()    

class FidoFinder(models.Model):
    name = models.TextField()
    city = models.TextField()
    date = models.TextField()
    breed = models.TextField()
    status = models.TextField()
    image = models.TextField()
    petid = models.TextField()

class HelpingLostPets(models.Model):
    status = models.TextField()
    date = models.TextField()
    location = models.TextField()
    image = models.TextField()
    name = models.TextField()
    breed = models.TextField()
    gender = models.TextField()
    age = models.TextField()
    size = models.TextField()
    color = models.TextField()

class LostMyDoggie(models.Model):
    image = models.TextField()
    name = models.TextField()
    status = models.TextField()
    gender = models.TextField()
    location = models.TextField()
    zip = models.TextField()
    breed = models.TextField()
    color = models.TextField()
    date = models.TextField()

class PawBoost(models.Model):
    name = models.TextField()
    breed = models.TextField()
    location = models.TextField()
    date = models.TextField()
    petid = models.TextField()
    image = models.TextField()

class PetKey(models.Model):
    name = models.TextField()
    breed = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    color = models.TextField()
    image = models.TextField()

class TabbyTracker(models.Model):
    name = models.TextField()
    location = models.TextField()
    date = models.TextField()
    breed = models.TextField()
    status = models.TextField()
    image = models.TextField()
    petid = models.TextField()