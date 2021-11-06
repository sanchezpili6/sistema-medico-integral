from django.contrib import admin

from prescription.models import Prescription

class PrescriptionAdmin(admin.ModelAdmin):
    "Admin for Prescription"

    list_display = [
        'pk',
        'patient',
        'doctor',
        'medicine'
    ]

admin.site.register(Prescription, PrescriptionAdmin)