from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from bs4 import BeautifulSoup

from .serializers import PetSerializer, FidoFinderSerializer, HelpingLostPetsSerializer, LostMyDoggieSerializer, PawBoostSerializer, PetKeySerializer, TabbyTrackerSerializer
from .models import Pet, FidoFinder, HelpingLostPets, LostMyDoggie, PawBoost, PetKey, TabbyTracker

#from Webscraping.scrapers.lostmydoggie_scrap import LostMyDoggie

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('date')
    serializer_class = PetSerializer

class FidoFinderSet(viewsets.ModelViewSet):
    queryset = FidoFinder.objects.all().order_by('date')
    serializer_class = FidoFinderSerializer

class HelpingLostPetsSet(viewsets.ModelViewSet):
    queryset = HelpingLostPets.objects.all().order_by('date')
    serializer_class = HelpingLostPetsSerializer

class LostMyDoggieSet(viewsets.ModelViewSet):
    queryset = LostMyDoggie.objects.all().order_by('date')
    serializer_class = LostMyDoggieSerializer

    '''def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = list(serializer.data)

        json = LostMyDoggie().scrap()

        for scrapped in json:
            new_serializer.append(scrapped)
        
        return Response(new_serializer)'''

class PawBoostSet(viewsets.ModelViewSet):
    queryset = PawBoost.objects.all().order_by('date')
    serializer_class = PawBoostSerializer

class PetKeySet(viewsets.ModelViewSet):
    queryset = PetKey.objects.all().order_by('date')
    serializer_class = PetKeySerializer

class TabbyTrackerSet(viewsets.ModelViewSet):
    queryset = TabbyTracker.objects.all().order_by('date')
    serializer_class = TabbyTrackerSerializer
