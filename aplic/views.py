from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from aplic.models import Pet, Usuario, Ong, Endereco, Vacina
from aplic.api.serializer import PetsSerializer, UsuariosSerializer, OngsSerializer, EnderecosSerializer, VacinasSerializer

# Create your views here.

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer

class OngsViewSet(viewsets.ModelViewSet):    
    queryset = Ong.objects.all()
    serializer_class = OngsSerializer

class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer

class VacinasViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinasSerializer

class IndexView(TemplateView):
    template_name = 'index.html'
