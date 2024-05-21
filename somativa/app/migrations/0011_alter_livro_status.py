# Generated by Django 5.0.6 on 2024-05-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_categorias_fotoslivro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.CharField(choices=[('P', 'Pendente'), ('C', 'Cancelado(a)'), ('A', 'Aprovado(a)')], default='P', max_length=100),
        ),
    ]
