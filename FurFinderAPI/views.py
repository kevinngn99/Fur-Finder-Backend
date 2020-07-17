from django.http import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import PetSerializer, FidoFinderSerializer, HelpingLostPetsSerializer, LostMyDoggieSerializer, PawBoostSerializer, PetKeySerializer, TabbyTrackerSerializer, imageReportSerializer, RegistrationSerializer
from .models import Pet, PetImage, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker, imageReport, Account

from Webscraping.scrapers.fidofinder_scrap import FidoFinderScrap
from Webscraping.scrapers.helpinglostpets_scrap import HelpingLostPetsScrap
from Webscraping.scrapers.lostmydoggie_scrap import LostMyDoggieScrap
from Webscraping.scrapers.pawboost_scrap import PawBoostScrap
from Webscraping.scrapers.petkey_scrap import PetKeyScrap
from Webscraping.scrapers.tabbytracker_scrap import TabbyTrackerScrap

import logging
logger = logging.getLogger('django')


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
    queryset = Pet.objects.all().order_by('date')
    serializer_class = PetSerializer

    def post(self, request, formant=None):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True, data=request.data, files=request.files)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
