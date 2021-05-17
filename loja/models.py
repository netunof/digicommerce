from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import os

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    def novo_nome(instance, filename):
            ext = filename.split('.')[-1]
            filename = "%s.%s" % (instance.nome, ext)
            return os.path.join('upload', filename)

    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField()
    descricao = models.TextField(blank=True, null=True)
    foto1 = models.ImageField(upload_to=novo_nome, blank=True, null=True)
    foto2 = models.ImageField(upload_to=novo_nome, blank=True, null=True)
    foto3 = models.ImageField(upload_to=novo_nome, blank=True, null=True)
    foto4 = models.ImageField(upload_to=novo_nome, blank=True, null=True)
    foto5 = models.ImageField(upload_to=novo_nome, blank=True, null=True)
    
    criado = models.DateTimeField(auto_now=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    cep = models.PositiveIntegerField()
    logradouro = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
