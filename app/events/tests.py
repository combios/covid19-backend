from django.test import TestCase
from django.apps import apps
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .apps import *
from .models import *


class DefinitionsConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(EventsConfig.name, "events")
        self.assertEqual(apps.get_app_config('events').name, "events")

class QuestionnaireResponseTest(TestCase):

    def setUp(self):
        p = Patient()
        p.birth_date = "1990-04-08"
        p.gender = "M"
        p.save()
        q = Questionnaire()
        q.save()
        self.patient = p
        self.questionnaire = q


    def create_questionnaireresponse(self):
        return QuestionnaireResponse.objects.create(
            questionnaire=self.questionnaire,
            authored = "2020-04-08T00:08:41.585Z",
            patient = self.patient
        )

    def test_create_questionnaireresponse(self):
        q = self.create_questionnaireresponse()
        self.assertTrue(isinstance(q, QuestionnaireResponse))
        self.assertEqual(q.__str__(), "QuestionnaireResponse:{id}-{authored}".format(id=q.id,authored=q.authored))


class QuestionnaireResponseViewSetTest(APITestCase):

    def setUp(self):
        p = Patient()
        p.birth_date = "1990-04-08"
        p.gender = "M"
        p.save()
        q = Questionnaire()
        q.save()
        self.patient = p
        self.questionnaire = q


    def test_list(self):

        response = self.client.get(reverse('questionnaire_responses-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        data = {
            "patient":self.patient.id,
            "questionnaire":1,
            "authored": "2020-04-08T00:08:41.585Z",
            "answers": {
                "q1":"a1",
                "q2":"a2"
            }
        }
        response = self.client.post(reverse('questionnaire_responses-list'),data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_noanswers(self):
        data = {
            "patient":self.patient.id,
            "questionnaire":1,
            "authored": "2020-04-08T00:08:41.585Z",
        }
        response = self.client.post(reverse('questionnaire_responses-list'),data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invaliddata(self):
        q = Questionnaire()
        q.save()
        data = {
            "patient":"123456",
            "questionnaire":1,
            "authored": "2020-04-08T00:08:41.585Z",
        }
        response = self.client.post(reverse('questionnaire_responses-list'),data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
