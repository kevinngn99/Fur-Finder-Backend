from rest_framework import serializers
from .models import Pet, imageReport

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'gender', 'age', 'breed', 'size', 'dob')

class imageReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imageReport
        fields = '__all__' # all model fields will be included