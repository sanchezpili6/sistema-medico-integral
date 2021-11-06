from django.db import models
from doctor.models import Doctor

from patients.models import Patient


class History(models.Model):


    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        max_length=45,
        verbose_name='paciente'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        max_length=45,
        verbose_name='medico'
    )
    suffering = models.CharField(
        max_length=45,
        verbose_name='padecimiento'
    )

    diagnosis = models.CharField(
        max_length=45,
        verbose_name='diagnostico'
    )

    treatment = models.CharField(
        max_length=45,
        verbose_name='tratamiento',
        blank=True,
        null=True,
    )

    analysis = models.CharField(
        max_length=45,
        verbose_name='analisis realizados'
    )

    results = models.CharField(
        max_length=45,
        verbose_name='resultados de analisis'
    )
    

    class Meta:
        """Define the behavior of Model."""
        verbose_name = 'Historial Medico'
        verbose_name_plural = 'Historiales Medicos'
