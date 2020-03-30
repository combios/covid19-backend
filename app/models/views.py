from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class ModelMetadataViewSet(viewsets.ModelViewSet):
    queryset = ModelMetadata.objects.all()
    serializer_class = ModelMetadataSerializer
