from django.db import models

DTYPE_CHOICES = models.TextChoices('dtype', 'NUMBER STRING').choices


class ModelParameter(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=DTYPE_CHOICES)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class ModelMetadata(models.Model):
    """ Model Metadata /models/ """
    name = models.SlugField(max_length=60)
    description = models.CharField(max_length=200, blank=True)
    inputs = models.ManyToManyField(ModelParameter, related_name='inputs')
    outputs = models.ManyToManyField(ModelParameter, related_name='outputs')

    def __str__(self):
        return self.name
