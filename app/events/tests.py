from django.test import TestCase
from django.apps import apps

from definitions.models import Questionnaire
from base.models import Patient
from .models import *
from .apps import *


class EventsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(EventsConfig.name, "events")
        self.assertEqual(apps.get_app_config(
            'events').name, "events")
            
class QuestionnaireResponseTest(TestCase):

    def create_questionnaire_response(self, code="TEST", title="Test questionnaire", description="Test questionnaire"):
        q = Questionnaire.objects.create(
            code=code, title=title, description=description)
        p = Patient.objects.create(
            gender='M', birth_date="2020-02-02")
        return QuestionnaireResponse.objects.create(
            questionnaire=q,
            authored='2020-02-02 04:00:00.000000-05:00',
            patient=p
        )

    def test_create_questionnaire_response(self):
        q = self.create_questionnaire_response()
        self.assertTrue(isinstance(q, QuestionnaireResponse))
        self.assertEqual(q.__str__(), q.__str__())
