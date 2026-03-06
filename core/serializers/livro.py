from rest_framework import serializers
from django.core.validators import EmailValidator

class AutorSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100, required=False, allow_blank=True)


class LivroSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=200)
    autor = AutorSerializer()
    descricao = serializers.CharField(required=False)
    data_publicacao = serializers.DateField(required=False)