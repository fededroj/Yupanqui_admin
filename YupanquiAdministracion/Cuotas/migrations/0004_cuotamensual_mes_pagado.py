# Generated by Django 4.2.4 on 2023-11-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuotas', '0003_cuotaactividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuotamensual',
            name='mes_pagado',
            field=models.BooleanField(default=False),
        ),
    ]
