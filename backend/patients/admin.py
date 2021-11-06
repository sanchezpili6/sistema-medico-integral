from django.contrib import admin

from patients.models import Patient


class PatientAdmin(admin.ModelAdmin):
    "Admin for Patients"

    list_display = [
        'pk',
        'name',
        'last_name',
        'nss',
        'policy',
    ]

admin.site.register(Patient, PatientAdmin)