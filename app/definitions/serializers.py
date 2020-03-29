from rest_framework import serializers
from .models import Questionnaire, QuestionnaireItem

class QuestionnaireItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireItem
        fields = ['code','order','text','item_type','required','max_length',]

class QuestionnaireSerializer(serializers.ModelSerializer):

    items = QuestionnaireItemSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ['id','code', 'title', 'description','items']


