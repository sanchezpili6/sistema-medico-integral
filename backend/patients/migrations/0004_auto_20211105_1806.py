# Generated by Django 3.1.6 on 2021-11-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='nss',
            field=models.CharField(max_length=45, unique=True, verbose_name='numero de seguro'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='policy',
            field=models.CharField(max_length=45, unique=True, verbose_name='poliza seguros'),
        ),
    ]
