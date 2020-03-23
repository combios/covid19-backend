from django.contrib import admin

from .models import Patient, PatientData

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','gender','birth_date',)

@admin.register(PatientData)
class PatientDataAdmin(admin.ModelAdmin):
    list_display = ('patient','firstname','surname','email')
