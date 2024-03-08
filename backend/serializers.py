from rest_framework import serializers
from .models import interesado, bachillerato, licenciatura, grado_academico, visita

class InteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = interesado
        fields = '__all__'
        
class BachilleratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = bachillerato
        fields = '__all__'
        
class LicenciaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = licenciatura
        fields = '__all__'
        
class GradoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = grado_academico
        fields = '__all__'
        
class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = visita
        fields = '__all__'