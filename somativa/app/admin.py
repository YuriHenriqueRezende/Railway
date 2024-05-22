from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ('email','nome', 'is_staff', 'is_active', 'cpf')
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('cpf','nome', 'biografia', 'foto')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','nome', 'cpf', 'biografia', 'foto', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','nome', 'cpf')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(Usuario, CustomUserAdmin)

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
    list_display = ['id', 'titulo',  'descricao', 'numero_pagina', 'formato', 'numero_edicao', 'autor', 'publicacao', 'categoriaFK', 'status', 'preco','fotos']
    list_display_links = ('id', 'titulo', 'descricao', 'numero_pagina', 'formato', 'numero_edicao', 'autor', 'publicacao', 'categoriaFK', 'status', 'preco','fotos')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(livro, AdminLivro)

class AdminEmprestimo(admin.ModelAdmin):
    model = emprestimo
    list_display = ['id', 'usuarioFK', 'data_inicio', 'data_fim']
    list_display_links = ('id', 'usuarioFK', 'data_inicio', 'data_fim')
    search_fields = ('usuarioFK',)
    list_per_page = 10

admin.site.register(emprestimo, AdminEmprestimo)