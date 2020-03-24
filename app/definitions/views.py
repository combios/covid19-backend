from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

class QuestionnaireViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    
class QuestionnaireItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionnaireItem.objects.all()
    serializer_class = QuestionnaireItemSerializer
