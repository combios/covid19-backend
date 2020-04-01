from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

class QuestionnaireViewSet(viewsets.ViewSet):

    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def list(self, request):
        serializer = QuestionnaireSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        questionnaire = get_object_or_404(self.queryset, code=pk)
        serializer = QuestionnaireSerializer(questionnaire)
        return Response(serializer.data)

class QuestionnaireItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuestionnaireItem.objects.all()
    serializer_class = QuestionnaireItemSerializer
