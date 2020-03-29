from rest_framework import serializers
from .models import *


class ModelParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelParameter
        fields = ['name', 'type', 'description']


class ModelMetadataSerializer(serializers.HyperlinkedModelSerializer):
    inputs = ModelParameterSerializer(many=True)

    class Meta:
        model = ModelMetadata
        fields = ['name', 'description', 'inputs']
