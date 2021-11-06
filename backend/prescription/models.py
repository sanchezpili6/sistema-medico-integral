from django.db import models

from doctor.models import Doctor
from history.models import History

from patients.models import Patient

class Prescription(models.Model):


    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        max_length=45,
        verbose_name='paciente'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name='medico'
    )
    medicine = models.CharField(
        max_length=45,
        verbose_name='medicina'
    )

    class Meta:
        """Define the behavior of Model."""
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

