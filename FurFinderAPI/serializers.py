from rest_framework import serializers
from .models import Pet, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, imageReport

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'gender', 'size', 'date', 'age', 'state', 'zip', 'location','breed','image')

class FidoFinderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FidoFinder
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class HelpingLostPetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelpingLostPets
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class LostMyDoggieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LostMyDoggie
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class PawBoostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PawBoost
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class PetKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetKey
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class TabbyTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TabbyTracker
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'image', 'location', 'name', 'petid', 'size', 'status', 'zip')

class imageReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imageReport
        fields = '__all__' # all model fields will be included
