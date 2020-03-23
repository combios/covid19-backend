from rest_framework import serializers
from .models import Patient, PatientData


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'gender', 'birth_date',]


class PatientDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientData
        fields = ['patient','firstname','surname','email','document_type']