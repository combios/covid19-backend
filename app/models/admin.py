from django.contrib import admin
from .models import *


@admin.register(ModelParameter)
class ModelParameterAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description']


@admin.register(ModelMetadata)
class ModelMetadataAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
