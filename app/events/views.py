from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

class QuestionnaireResponseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionnaireResponse.objects.all()
    serializer_class = QuestionnaireResponseSerializer
