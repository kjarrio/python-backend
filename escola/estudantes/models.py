from django.db import models


class Estudante(models.Model):

    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=250, default='')
    cpf = models.CharField(max_length=14, default='', unique=True)
    rg = models.CharField(max_length=50, default='', unique=True)
    email = models.CharField(max_length=250, default='')
    celular = models.CharField(max_length=20, default='')
    data_nascimento = models.DateField()

    class Meta:
        ordering = ['data_cadastro']
