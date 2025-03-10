# Generated by Django 5.1.6 on 2025-03-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('registration_number', models.CharField(max_length=20, unique=True, verbose_name='Matrícula')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, verbose_name='Gênero')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('address', models.TextField(verbose_name='Endereço')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['name'],
            },
        ),
    ]
