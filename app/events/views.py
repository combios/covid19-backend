from django.shortcuts import render
from rest_framework import viewsets
from django_cognito_jwt import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class QuestionnaireResponseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionnaireResponse.objects.all()
    serializer_class = QuestionnaireResponseSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
