from django.db import models
from documento.models import Documento

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

    