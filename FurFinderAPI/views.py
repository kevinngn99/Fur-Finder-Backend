from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PetSerializer
from .models import Pet
from bs4 import BeautifulSoup
from Webscraping.lostmydoggie_scrap import LostMyDoggie

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('date')
    serializer_class = PetSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        new_serializer = list(serializer.data)

        json = LostMyDoggie().scrap()

        for scrapped in json:
            new_serializer.append(scrapped)
        
        return Response(new_serializer)
