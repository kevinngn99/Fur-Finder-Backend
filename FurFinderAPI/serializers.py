from rest_framework import serializers
from .models import Pet, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, imageReport
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def save(self):
        account = User(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'gender', 'size', 'date', 'age', 'state', 'zip', 'location','breed','image')

class FidoFinderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FidoFinder
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class HelpingLostPetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpingLostPets
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class LostMyDoggieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LostMyDoggie
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class PawBoostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PawBoost
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class PetKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetKey
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class TabbyTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TabbyTracker
        fields = ('age', 'breed', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class imageReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imageReport
        fields = '__all__' # all model fields will be included
