from django.shortcuts import render
from rest_framework import generics
from .models import interesado, bachillerato, licenciatura, grado_academico, visita
from .serializers import InteresadoSerializer, BachilleratoSerializer, LicenciaturaSerializer, GradoAcademicoSerializer, VisitaSerializer

# Create your views here.

class InteresadoListCreateView(generics.ListCreateAPIView):
    queryset = interesado.objects.all()
    serializer_class = InteresadoSerializer
    
class BachilleratoListCreateView(generics.ListCreateAPIView):
    queryset = bachillerato.objects.all()
    serializer_class = BachilleratoSerializer
    
class LicenciaturaListCreateView(generics.ListCreateAPIView):
    queryset = licenciatura.objects.all()
    serializer_class = LicenciaturaSerializer
    
class GradoAcademicoListCreateView(generics.ListCreateAPIView):
    queryset = grado_academico.objects.all()
    serializer_class = GradoAcademicoSerializer
    
class VisitaListCreateView(generics.ListCreateAPIView):
    queryset = visita.objects.all()
    serializer_class = VisitaSerializer
