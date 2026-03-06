from django.db import models
from django.core.validators import EmailValidator
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    class Meta:
        db_table = 'autor'
    
    def __str__(self):
        return self.nome


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'email']


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


router = DefaultRouter()
router.register(r'autores', AutorViewSet)

urlpatterns = router.urls