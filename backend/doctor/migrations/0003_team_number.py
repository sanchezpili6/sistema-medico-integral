# Generated by Django 3.1.6 on 2021-11-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20211105_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='number',
            field=models.CharField(default='2', max_length=45, verbose_name='numero de equipo'),
            preserve_default=False,
        ),
    ]