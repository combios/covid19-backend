from rest_framework import serializers
from .models import *

class QuestionnaireResponseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireResponseItem
        fields = ['code','value',]

class QuestionnaireResponseSerializer(serializers.ModelSerializer):

    #answers = QuestionnaireResponseItemSerializer(many=True, read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = QuestionnaireResponse
        fields = ['id','patient','authored','answers','questionnaire']

    def get_answers(self, obj):
        answers = {x.code: x.value for x in obj.answers.all()}
        return answers


