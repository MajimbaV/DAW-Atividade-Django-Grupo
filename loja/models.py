from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=100)
    endereco = models.TextField(max_length=100)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class CategoriaProduto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)
    preco = models.CharField(max_length=100)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.PROTECT, related_name="+")
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome

class Pedido (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="+")
    dataPedido = models.DateField(max_length=30, default=timezone.now)
    produtos = models.ManyToManyField(Produto)
    
class Funcionario (models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=100)
    endereco = models.TextField(max_length=100)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
class Departamento (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField(max_length=100)
    funcionarios = models.ManyToManyField(Funcionario)
    
    class Meta:
        ordering = ['nome']
        
    def __str__(self):
        return self.nome