from django.db import models

class QuestionnaireResponse(models.Model):
    questionnaire = models.IntegerField()
    authored = models.DateTimeField()

    def __str__(self):
        return super().__str__()

class QuestionnaireResponseItem(models.Model):
    response = models.ForeignKey(QuestionnaireResponse, on_delete=models.CASCADE, related_name="answers")
    code = models.SlugField()
    value = models.CharField(max_length=256)