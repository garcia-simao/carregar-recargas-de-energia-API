from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario
from .serializers import UsuarioSerializer
from .models import CarregarRecarga
from .serializers import CarregarRecargaSerializer



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 


class CarregarRecargaViewSet(viewsets.ModelViewSet):
    queryset = CarregarRecarga.objects.all()
    serializer_class = CarregarRecargaSerializer 

