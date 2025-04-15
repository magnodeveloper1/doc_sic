from django.db import models
from django.contrib.auth.models import User

DOCUMENT_STATUS = [
    ('created', 'Criado'),
    ('sent', 'Enviado para Aprovacao'),
    ('rejected', 'Rejeitado'),
    ('aproved', 'Aprovado')
]

# Create your models here.
class Documento(models.Model):
    nome = models.CharField(
        max_length=200,
        unique=True
    )

    created_at = models.DateField( 
        auto_now_add=True,
        verbose_name='Data de Criacao'
    )

    updated_at = models.DateField(
        auto_now=True,
        verbose_name='Data de Atualicao'
    )

    status = models.CharField(
        max_length=50,
        null=False,
        default=DOCUMENT_STATUS[0][0],
        choices=DOCUMENT_STATUS
    )

    status_at = models.DateField(
        null=True,
        verbose_name='Data do Staus'
    )

    texto = models.TextField()

    documento = models.FileField(
        null=False,
        upload_to='static/'
    )

    utilizador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return self.nome

class DocPartilhado(models.Model):

    documento = models.ForeignKey(
        to=Documento,
        on_delete=models.CASCADE
    )

    partilhado_com = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Partilhado_Com'
    )

    partilhado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Partilhado_Por'
    )

    create_at = models.DateField(
        null=False,
        auto_now=True
    )

    def __str__(self):
        return self.documento.nome

