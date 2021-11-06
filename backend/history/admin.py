from django.contrib import admin

from history.models import History


class HistoryAdmin(admin.ModelAdmin):
    "Admin for History"

    list_display = [
        'pk',
        'patient',
        'doctor',
        'treatment'
    ]

admin.site.register(History, HistoryAdmin)