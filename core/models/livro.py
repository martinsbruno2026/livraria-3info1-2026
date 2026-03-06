from django.db import models
from categoria import Categoria
from editora import Editora
from autor import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_publicacao = models.DateField()
    quantidade_estoque = models.IntegerField(default=0)
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='livros'
    )
    editora = models.ForeignKey(
        Editora,
        on_delete=models.PROTECT,
        related_name='livros'
    )
    autores = models.ManyToManyField(
        Autor,
        related_name='livros'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self):
        return self.titulo