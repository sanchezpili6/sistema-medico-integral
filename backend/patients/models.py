from django.db import models

# Create your models here.
class Patient(models.Model):


    name = models.CharField(
        max_length=45,
        verbose_name='nombre'
    )
    last_name = models.CharField(
        max_length=45,
        verbose_name='apellido'
    )
    nss = models.CharField(
        max_length=45,
        unique=True,
        verbose_name='numero de seguro'
    )
    policy = models.CharField(
        max_length=45,
        unique=True,
        verbose_name='poliza seguros'
    )

    class Meta:
        """Define the behavior of Model."""

        verbose_name = 'Paciente'
        verbose_name_plural = 'Paciente'
