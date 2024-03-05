from django.shortcuts import render

# Create your views here.
from .serializer import BandaSerializer, SolistaSerializer
from .models import Banda,Solista
from rest_framework import viewsets 

class BandaViewset(viewsets.ModelViewSet):
    queryset=Banda.objects.all()
    serializer_class=BandaSerializer 

class SolistaViewset(viewsets.ModelViewSet):
    queryset=Solista.objects.all()
    serializer_class=SolistaSerializer 
    