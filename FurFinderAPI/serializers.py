from rest_framework import serializers
from .models import Pet, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, ReportPets

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'gender', 'size', 'date', 'age', 'state', 'zip', 'location','breed','image')

class ReportPetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportPets
        fields = ('name', 'gender', 'size', 'date', 'age', 'state', 'zip', 'location','breed','image')

class FidoFinderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FidoFinder
        fields = ('name', 'city', 'date', 'breed', 'status', 'image', 'petid')

class HelpingLostPetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpingLostPets
        fields = ('status', 'date', 'location', 'image', 'name', 'breed', 'gender', 'age', 'size', 'color')

class LostMyDoggieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LostMyDoggie
        fields = ('image', 'name', 'status', 'gender', 'location', 'zip', 'breed', 'color', 'date')

class PawBoostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PawBoost
        fields = ('name', 'breed', 'location', 'date', 'petid', 'image')

class PetKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetKey
        fields = ('name', 'breed', 'age', 'gender', 'color', 'image')

class TabbyTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TabbyTracker
        fields = ('name', 'location', 'date', 'breed', 'status', 'image', 'petid')

