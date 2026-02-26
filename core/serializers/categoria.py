from attr import fields
from rest_framework.serializers import ModelSerializer 

from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "_all_"