from django.contrib import admin

from doctor.models import Doctor, Team


class DoctorAdmin(admin.ModelAdmin):
    "Admin for Doctor"

    list_display = [
        'pk',
        'name',
        'specialty',
        'certificate',
        'university',
        'affiliation'
    ]

admin.site.register(Doctor, DoctorAdmin)


class TeamAdmin(admin.ModelAdmin):
    "Admin for Team"

    list_display = [
        'pk',
        'number'
    ]

admin.site.register(Team, TeamAdmin)