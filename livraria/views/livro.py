from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
