from django.db import models
from base.models import Patient
from definitions.models import Questionnaire

class QuestionnaireResponse(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questionnaire")
    authored = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="questionnaire_responses")

    def __str__(self):
        return "QuestionnaireResponse:{id}-{authored}".format(id=self.id,authored=self.authored)

class QuestionnaireResponseItem(models.Model):
    response = models.ForeignKey(QuestionnaireResponse, on_delete=models.CASCADE, related_name="answers")
    code = models.SlugField()
    value = models.CharField(max_length=256)