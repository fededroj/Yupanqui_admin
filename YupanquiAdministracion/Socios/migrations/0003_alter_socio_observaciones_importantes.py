# Generated by Django 4.2.4 on 2023-11-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socios', '0002_socio_observaciones_importantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='observaciones_importantes',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Observaciones Importantes'),
        ),
    ]