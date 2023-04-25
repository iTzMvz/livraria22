from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Livro, Autor
from livraria.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, AutorSerializer
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]   

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer  