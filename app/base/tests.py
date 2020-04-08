from django.test import TestCase
from django.apps import apps

from .apps import *
class BaseConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(BaseConfig.name, "base")
        self.assertEqual(apps.get_app_config('base').name, "base")

from .models import *
from .serializers import *

class PatientSerializerTest(TestCase):
    def setUp(self):
        self.patient_attrs = {
            'gender': 'M',
            'birth_date': '1950-02-02'
        }

        self.serializer_data = {
            'gender': 'M',
            'birth_date': '1950-02-02'
        }

        self.patient = Patient.objects.create(**self.patient_attrs)
        self.serializer = PatientSerializer(instance=self.patient)

    def test_expected_fields(self):
        data = self.serializer.data
        self.assertEquals(set(data.keys()), set(['id','gender','birth_date']))

