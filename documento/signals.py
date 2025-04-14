from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Documento, DocPartilhado

@receiver(post_save, sender=Documento)
def my_handler(sender, **kwargs):
    shared = DocPartilhado()
    shared.documento = sender
    shared.save()
