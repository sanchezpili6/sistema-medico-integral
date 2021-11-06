from django.db import models

# Un medico puede estar en varios equipos?
class Doctor(models.Model):


    name = models.CharField(
        max_length=45,
        verbose_name='nombre'
    )
    specialty = models.CharField(
        max_length=45,
        verbose_name='especialidad'
    )
    certificate = models.CharField(
        max_length=45,
        verbose_name='cedula profesional',
        unique=True,
    )

    university = models.CharField(
        max_length=45,
        verbose_name='universidad'
    )

    affiliation = models.CharField(
        max_length=45,
        verbose_name='afiliacion',
        blank=True,
        null=True,
    )
    def __str__(self):
        """Return the representation in string"""
        return self.name

    class Meta:
        """Define the behavior of Model."""
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'


class Team(models.Model):

    number = models.CharField(
        max_length=45,
        verbose_name='numero de equipo'
    )

    doctor = models.ManyToManyField(
        Doctor,
        verbose_name= 'Doctor',
        related_name= 'doctors'

    )

    class Meta:
        """Define the behavior of Model."""
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipo de Trabajo'
