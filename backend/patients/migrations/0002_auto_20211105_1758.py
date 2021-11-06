# Generated by Django 3.1.6 on 2021-11-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='nss',
            field=models.CharField(default='2', max_length=45, verbose_name='numero de seguro'),
            preserve_default=False,
        ),
    ]
