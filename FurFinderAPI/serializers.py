from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'gender', 'age', 'breed', 'size', 'dob')