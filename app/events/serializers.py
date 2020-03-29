from rest_framework import serializers
from .models import *

class QuestionnaireResponseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireResponseItem
        fields = ['code','value',]

class QuestionnaireResponseSerializer(serializers.ModelSerializer):

    answers = QuestionnaireResponseItemSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionnaireResponse
        fields = ['id','authored','answers']


