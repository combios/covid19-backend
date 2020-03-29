from django.contrib import admin

from .models import *

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ('questionnaire','authored',)

@admin.register(QuestionnaireResponseItem)
class QuestionnaireResponseItemAdmin(admin.ModelAdmin):
    list_display = ('response','code','value',)
