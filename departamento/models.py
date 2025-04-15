from django.db import models
from documento.models import Documento
from django.contrib.auth.models import User

APROVATION_STATUS = [
    ('in_hold', 'Aguardando por Aprovacao'),
    ('aproved', 'Aprovado'),
    ('rejected', 'Rejeitado')
]

# Create your models here.
class Departamento(models.Model):

    nome = models.CharField(
        null=False,
        max_length=200
    )

    create_at = models.DateField(
        null=False,
        auto_now_add=True
    )

    updated_at = models.DateField(
        null=False,
        auto_now=True
    )

    status = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome
    
class DocumentoDoDepartamento(models.Model):
    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE
    )

    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE
    )

class DocumentoEnviado(models.Model):

    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
    )

    user_enviou = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        related_name='Utilizador_enviou'
    )

    enviar_para = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    descricao_de_envio = models.TextField(
        null=False
    )

    estado_de_aprovacao = models.CharField(
        max_length=100,
        choices=APROVATION_STATUS,
        default=APROVATION_STATUS[0][0],
        null=False,
        editable=False
    )

    user_aprovou = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        related_name='Utilizador_aprovou',
        null=True,
    )

    def __str__(self):
        return self.documento.nome

    