import uuid
from django.db import models

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female')
]

DOCUMENT_TYPE_CHOICES = [
    ('RG','Registro civil / NUIP'),
    ('TI','Tarjeta de identidad'),
    ('CC','Cedula de ciudadania'),
    ('CE','Cedula de extranjeria'),
    ('PA','Passport'),

]

# This model covers data about patients in health-related 
# activities. It doesn't contain PII (Personal 
# Identifiable Information):
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()


# This model covers PII information for a patient
class PatientData(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPE_CHOICES)
    document_id = models.CharField(max_length=16)


