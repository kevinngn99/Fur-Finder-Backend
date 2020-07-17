from rest_framework import serializers
from .models import Pet, PetImage, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, imageReport, Account


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']

    def save(self):
        account = Account(
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

class PetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetImage
        fields = ('image', )

class PetSerializer(serializers.HyperlinkedModelSerializer):
    images = PetImageSerializer(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = ('age', 'breed', 'city', 'color', 'date', 'gender', 'images', 'name', 'petid', 'size', 'state', 'status', 'zip')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        pet = Pet.objects.create(
            age = validated_data.get('age'),
            breed = validated_data.get('breed'),
            city = validated_data.get('city'),
            color = validated_data.get('color'),
            date = validated_data.get('date'),
            gender = validated_data.get('gender'),
            name = validated_data.get('name'),
            petid = validated_data.get('petid'),
            size = validated_data.get('size'),
            state = validated_data.get('state'),
            status = validated_data.get('status'),
            zip = validated_data.get('zip')
        )

        for image_data in images_data.values():
            PetImage.objects.create(pet=pet, image=image_data)

        return pet

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
