from rest_framework import serializers
from .models import Banda, Solista

class BandaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Banda
        fields='__all__'

class SolistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Solista 
        fields='__all__'