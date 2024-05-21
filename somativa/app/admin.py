from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdminUsuarioCustomizado(admin.ModelAdmin):
    model = usuariosCustomizado
    list_display = ['id',  'email', 'cpf', 'biografia', 'cargo', 'foto']
    list_display_links = ('id', 'email', 'cpf', 'biografia', 'cargo', 'foto')
    ordering = ['email']
    search_fields = ['nome',]

admin.site.register(usuariosCustomizado, AdminUsuarioCustomizado)

class AdminFoto(admin.ModelAdmin):
    model = fotoslivro
    list_display = ['id', 'nome','link']
    list_display_links = ('id', 'nome','link')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(fotoslivro, AdminFoto)


class AdminCategorias(admin.ModelAdmin):
    model = categorias
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(categorias, AdminCategorias)

class AdminLivro(admin.ModelAdmin):
    model = livro
    list_display = ['id', 'titulo', 'imagemfk', 'descricao', 'numero_pagina', 'formato', 'numero_edicao', 'autor', 'publicacao', 'categoriaFK', 'status', 'preco']
    list_display_links = ('id', 'titulo', 'imagemfk', 'descricao', 'numero_pagina', 'formato', 'numero_edicao', 'autor', 'publicacao', 'categoriaFK', 'status', 'preco')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(livro, AdminLivro)

class AdminEmprestimo(admin.ModelAdmin):
    model = emprestimo
    list_display = ['id', 'livroFK', 'usuarioFK', 'data_inicio', 'data_fim']
    list_display_links = ('id', 'livroFK', 'usuarioFK', 'data_inicio', 'data_fim')
    search_fields = ('livroFK',)
    list_per_page = 10

admin.site.register(emprestimo, AdminEmprestimo)