# Generated by Django 4.2.20 on 2025-04-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_departamento_create_at_departamento_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
