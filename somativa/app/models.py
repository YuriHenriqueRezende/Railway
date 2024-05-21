from django.db import models

# Create your models here.
CARGOS
STATUS
FORMATOS

class fotos(models.Model):
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class usuariosCustomizado(models.Model):
    nome =
    email =
    cpf =
    biografia =
    cargo =

class livro(models.Model):
    titulo =
    foto = 
    descricao = 
    numero_pagina =
    formato =
    numero_edicao =
    autor =
    publicacao = 
    categoria =
    status =
    preco =


class emprestimo(models.Model):
    data_inicio =
    data_fim =

