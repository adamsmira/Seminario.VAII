from django.shortcuts import render
from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer

class Alunoviews(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer