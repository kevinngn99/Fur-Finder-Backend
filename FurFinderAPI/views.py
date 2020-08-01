from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from .serializers import PetSerializer, FidoFinderSerializer, HelpingLostPetsSerializer, LostMyDoggieSerializer, PawBoostSerializer, PetKeySerializer, TabbyTrackerSerializer, imageReportSerializer, RegistrationSerializer, UserMessagesSerializer
from .models import Pet, PetImage, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, imageReport, Account, UserMessages

from Webscraping.scrapers.fidofinder_scrap import FidoFinderScrap
from Webscraping.scrapers.helpinglostpets_scrap import HelpingLostPetsScrap
from Webscraping.scrapers.lostmydoggie_scrap import LostMyDoggieScrap
from Webscraping.scrapers.pawboost_scrap import PawBoostScrap
from Webscraping.scrapers.petkey_scrap import PetKeyScrap
from Webscraping.scrapers.tabbytracker_scrap import TabbyTrackerScrap
from Webscraping.prediction import reportPrediction
from profanity import profanity

import os
import tempfile

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            print("Token " + token)
        else:
            data = serializer.errors
        return Response(data)



class PetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # a non registered user cannot access this view
    queryset = Pet.objects.all().order_by('date')
    serializer_class = PetSerializer
    lookup_field = 'petid'

    # if we had an edit or delete method we would have to add an author to the post
    # and do the following inside the delete method
    # user = request.user  # which gets the user with that token
    # if pet_post.author != user:
    #   return Response({'response': "You don't have permission to delete that"})

    # for create we'd only have to set the following
    # account = request.user
    # pet_post = Pet(author=account)
    #def delete(self, request, pk, format=None):
    #    snippet = self.get_object(pk)
    #    snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, **kwargs):

        '''
        for key, value in request.FILES.items():

            fd, path = tempfile.mkstemp()

            try:
                with os.fdopen(fd, 'wb') as tmp:
                    tmp.write(value.read())
                    
                    predict = reportPrediction(path)
                    
                    if predict == "is not a pet":
                        print(value, 'Removed because image is NOT a pet.')
                    else:
                        print(value,  'Not removed because image IS a pet.')
            finally:
                os.remove(path)
        '''

        return super().create(request)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FidoFinderSet(viewsets.ModelViewSet):
    queryset = FidoFinder.objects.all().order_by('date')
    serializer_class = FidoFinderSerializer

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = None

        if 'zip' in kwargs:
            new_serializer = FidoFinderScrap().scrap(kwargs['zip'])[0]
        
        return Response(new_serializer)


class HelpingLostPetsSet(viewsets.ModelViewSet):
    queryset = HelpingLostPets.objects.all().order_by('date')
    serializer_class = HelpingLostPetsSerializer

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = list(serializer.data)

        if 'zip' in kwargs:
            json = HelpingLostPetsScrap().scrap(kwargs['zip'])
            for scrapped in json:
                new_serializer.append(scrapped)
        
        return Response(new_serializer)


class LostMyDoggieSet(viewsets.ModelViewSet):
    queryset = LostMyDoggie.objects.all().order_by('date')
    serializer_class = LostMyDoggieSerializer

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = list(serializer.data)

        if 'zip' in kwargs:
            json = LostMyDoggieScrap().scrap(kwargs['zip'])
            for scrapped in json:
                new_serializer.append(scrapped)
        
        return Response(new_serializer)


class PawBoostSet(viewsets.ModelViewSet):
    queryset = PawBoost.objects.all().order_by('date')
    serializer_class = PawBoostSerializer
    
    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = list(serializer.data)

        if 'zip' in kwargs:
            json = PawBoostScrap().scrap(kwargs['zip'])
            for scrapped in json:
                new_serializer.append(scrapped)
        
        return Response(new_serializer)


class PetKeySet(viewsets.ModelViewSet):
    queryset = PetKey.objects.all().order_by('name')
    serializer_class = PetKeySerializer

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = None

        if 'zip' in kwargs:
            new_serializer = PetKeyScrap().scrap(kwargs['zip'])[0]
        
        return Response(new_serializer)


class TabbyTrackerSet(viewsets.ModelViewSet):
    queryset = TabbyTracker.objects.all().order_by('date')
    serializer_class = TabbyTrackerSerializer

    def list(self, request, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = None

        if 'zip' in kwargs:
            new_serializer = TabbyTrackerScrap().scrap(kwargs['zip'])[0]
        
        return Response(new_serializer)


class imageReportViewSet(viewsets.ModelViewSet):
    queryset = imageReport.objects.all()
    serializer_class = imageReportSerializer

class UserMessagesViewSet(viewsets.ModelViewSet):
    queryset = UserMessages.objects.all()
    serializer_class = UserMessagesSerializer
