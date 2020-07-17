from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Pet(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    city = models.TextField(default='City')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    state = models.TextField(default='State')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class PetImage(models.Model):
    pet = models.ForeignKey(Pet, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)

class FidoFinder(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class HelpingLostPets(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class LostMyDoggie(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class PawBoost(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class PetKey(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class TabbyTracker(models.Model):
    age = models.TextField(default='Age')
    breed = models.TextField(default='Breed')
    color = models.TextField(default='Color')
    date = models.TextField(default='Date')
    gender = models.TextField(default='Gender')
    image = models.TextField(default='Image')
    location = models.TextField(default='Location')
    name = models.TextField(default='Name')
    petid = models.TextField(default='PetID')
    size = models.TextField(default='Size')
    status = models.TextField(default='Status')
    zip = models.TextField(default='Zip')

class imageReport(models.Model):
    image = models.TextField()


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    date_login = models.DateTimeField(verbose_name='date_login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

