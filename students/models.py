from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    name = models.CharField('Nome', max_length=100)
    registration_number = models.CharField('Matrícula', max_length=20, unique=True)
    birth_date = models.DateField('Data de Nascimento')
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=15)
    address = models.TextField('Endereço')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.registration_number})"