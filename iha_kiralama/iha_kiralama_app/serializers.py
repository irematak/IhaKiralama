from rest_framework import serializers
from .models import *

class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = '__all__'  # Tüm model alanlarını al

class IhalarimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ihalarim
        fields = '__all__'  # Tüm model alanlarını al

class KiralananIHASerializer(serializers.ModelSerializer):
    iha_model = serializers.CharField(source='iha.model', read_only=True)  # iha modelini temsil eden yeni bir alan ekledik
    class Meta:
        model = KiralananIHA
        fields = ['id', 'kiralayan_uye', 'iha', 'iha_model', 'baslangic_tarihi', 'bitis_tarihi']


class IHAlarimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ihalarim
        fields = '__all__'  # Tüm model alanlarını al


