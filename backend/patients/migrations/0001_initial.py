# Generated by Django 3.1.6 on 2021-11-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=45, verbose_name='apellido')),
                ('policy', models.CharField(max_length=45, verbose_name='poliza seguros')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Paciente',
            },
        ),
    ]
