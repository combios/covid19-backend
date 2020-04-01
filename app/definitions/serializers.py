from rest_framework import serializers
from .models import Questionnaire, QuestionnaireItem

class QuestionnaireItemSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='code')
    type = serializers.CharField(source='item_type')
    title = serializers.CharField(source='text')
    choices = serializers.JSONField()

    class Meta:
        model = QuestionnaireItem
        fields = ['name','order','title','type','required','max_length','choices',]

class QuestionnaireSerializer(serializers.ModelSerializer):

    elements = QuestionnaireItemSerializer(source='items', many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ['id','code', 'title', 'description','elements']
