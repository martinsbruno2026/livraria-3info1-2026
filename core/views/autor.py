from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from rest_framework import serializers

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'email']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer