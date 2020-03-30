from django.shortcuts import render
from rest_framework import viewsets
from django_cognito_jwt import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class QuestionnaireViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
class QuestionnaireItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionnaireItem.objects.all()
    serializer_class = QuestionnaireItemSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
