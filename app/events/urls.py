from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'questionnaire-responses', QuestionnaireResponseViewSet)

urlpatterns = router.urls