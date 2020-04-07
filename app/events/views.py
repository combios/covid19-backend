from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import *
from .serializers import *

class QuestionnaireResponseViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   #mixins.UpdateModelMixin,
                   #mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = QuestionnaireResponse.objects.all()
    serializer_class = QuestionnaireResponseSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        answers = request.data["answers"]
        del data["answers"]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        qr = QuestionnaireResponse.objects.get(pk=serializer.data["id"])
        for code in answers:
            a = QuestionnaireResponseItem()
            a.code = code
            a.value = answers[code]
            a.response = qr
            a.save()
        headers = self.get_success_headers(serializer.data)
        serializer.data["answers"] = answers
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

