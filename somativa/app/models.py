from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

# Create your models here.
STATUS = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
]

FORMATOS = [
        ("E","E-BOOK"),
        ("F","FISICO")
]

class fotoslivro(models.Model):
    nome = models.CharField(max_length=50)
    link = models.URLField(max_length=200, verbose_name="Image URL")

    def __str__(self):
        return self.nome
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    cpf = models.CharField(max_length=20)
    biografia = models.CharField(max_length=200, null=True, blank=True)
    foto = models.URLField(max_length=200, verbose_name="Image URL", null=True, blank=True)

    objects = Gerenciador()
    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class categorias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class livro(models.Model):
    titulo = models.CharField(max_length=50)
    imagemfk = models.ForeignKey(fotoslivro, related_name='fotosusuariosFKFK', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    numero_pagina = models.IntegerField()
    formato = models.CharField(max_length=100, choices=FORMATOS)
    numero_edicao = models.IntegerField()
    autor = models.ForeignKey(Usuario, related_name='fotosusuariosFKFK', on_delete=models.CASCADE)
    publicacao = models.IntegerField()
    categoriaFK = models.ForeignKey(categorias, related_name='categoriasFKFK', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default="P")
    preco = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.titulo

class emprestimo(models.Model):
    livroFK = models.ForeignKey(livro, on_delete=models.CASCADE)
    usuarioFK = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'{self.usuarioFK} - {self.livroFK}'
    
