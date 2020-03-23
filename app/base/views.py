from django.shortcuts import render
from rest_framework import viewsets

from .models import Patient, PatientData
from .serializers import *

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class PatientDataViewSet(viewsets.ModelViewSet):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
