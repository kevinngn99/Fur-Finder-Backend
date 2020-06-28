from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PetSerializer, imageReportSerializer
from .models import Pet, imageReport
from bs4 import BeautifulSoup

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('name')
    serializer_class = PetSerializer

    def list(self, request):
        scrapped = {
            "name": "Zuko",
            "gender": "Male",
            "age": "1",
            "breed": "Inu Shiba",
            "size": "Medium",
            "dob": "May 4, 2019"
        }

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        
        new_serializer = list(serializer.data)
        new_serializer.append(scrapped)
        
        return Response(new_serializer)

class imageReportViewSet(viewsets.ModelViewSet):
    queryset = imageReport.objects.all()
    serializer_class = imageReportSerializer