import uuid
from django.db import models

# An organized collection of questions intended to solicit information from patients, 
# providers, or other individuals involved in the healthcare domain.
class Questionnaire(models.Model):
    code = models.SlugField()
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

# An item part of questionnaire, usually a question, message or group of questions.
class QuestionnaireItem(models.Model):
    Q_ITEM_CHOICES = [
        ('group','group'),
        ('display','display'),
        ('string','string'),
        ('text','text'),
        ('boolean','boolean'),
        ('decimal','decimal'),
        ('integer','integer'),
        ('date','date'),
        ('dateTime','dateTime')
    ]

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='items')
    code = models.SlugField()
    order = models.IntegerField()
    text = models.CharField(max_length=512)
    item_type = models.CharField(max_length=12,choices=Q_ITEM_CHOICES)
    required = models.BooleanField()
    max_length = models.IntegerField()
    #answer_options = models.CharField(max_length=1024) # In JSON format

    def __str__(self):
        return self.code+":"+self.item_type


class Measure(models.Model):
    pass
