# Generated by Django 4.2.20 on 2025-04-15 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departamento', '0005_documentoenviado_descricao_de_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentoenviado',
            name='estado_de_aprovacao',
            field=models.CharField(choices=[('in_hold', 'Aguardando por Aprovacao'), ('aproved', 'Aprovado'), ('rejected', 'Rejeitado')], default=('in_hold', 'Aguardando por Aprovacao'), editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='documentoenviado',
            name='user_enviou',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
