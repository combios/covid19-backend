from django.contrib import admin

from .models import Questionnaire, QuestionnaireItem

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('code','title',)

@admin.register(QuestionnaireItem)
class QuestionnaireItemAdmin(admin.ModelAdmin):
    list_display = ('questionnaire','code','order','item_type','required',)
