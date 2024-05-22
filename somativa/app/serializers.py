from rest_framework import serializers
from . models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        many = True

class fotoslivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = fotoslivro
        fields = '__all__'
        many = True

class categoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = '__all__'
        many = True

class livroSerializer(serializers.ModelSerializer):
    foto = fotoslivroSerializer(read_only=True)
    class Meta:
        model = livro
        fields = '__all__'
        many = True

class emprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = emprestimo
        fields = '__all__'
        many = True