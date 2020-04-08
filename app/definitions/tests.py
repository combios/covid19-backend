from django.test import TestCase, Client
from django.apps import apps
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status

from .apps import *
from .models import *


class DefinitionsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(DefinitionsConfig.name, "definitions")
        self.assertEqual(apps.get_app_config(
            'definitions').name, "definitions")


class QuestionnaireTest(TestCase):

    def create_questionnaire(self, code="TEST", title="Test questionnaire", description="Test questionnaire"):
        return Questionnaire.objects.create(code=code, title=title, description=description)

    def test_create_questionnaire(self):
        q = self.create_questionnaire()
        self.assertTrue(isinstance(q, Questionnaire))
        self.assertEqual(q.__str__(), q.title)


class QuestionnaireItemTest(TestCase):

    def create_questionnaireitem(self, code="ITEM1", item_type="string"):
        q = QuestionnaireTest().create_questionnaire()
        return QuestionnaireItem.objects.create(
            questionnaire=q,
            code=code,
            order=1,
            text="title",
            item_type=item_type,
            required=False,
            max_length=5,
            choices="['1','2']"
        )

    def test_create_questionnaireitem(self):
        q = self.create_questionnaireitem()
        self.assertTrue(isinstance(q, QuestionnaireItem))
        self.assertEqual(q.__str__(), q.code+":"+q.item_type)


class QuestionnaireViewSetTest(APITestCase):

    def setUp(self):
        q = Questionnaire.objects.create(code="Q", title="TEST", description="TEST")
        q.save()
        self.questoinnaire = q
    
    def test_list(self):
        response = self.client.get(reverse('questionnaires-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        response = self.client.get(reverse('questionnaires-list')+self.questoinnaire.code+"/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)