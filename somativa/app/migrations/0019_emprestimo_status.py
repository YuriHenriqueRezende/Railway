# Generated by Django 5.0.6 on 2024-05-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_livro_descricao_alter_usuario_biografia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='status',
            field=models.CharField(choices=[('D', 'DEVOLVIDO'), ('A', 'ATRASADO'), ('E', 'EMPRESTADO')], default='E', max_length=100),
        ),
    ]
