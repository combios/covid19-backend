from django.urls import include, path
from rest_framework import routers
from .views import PatientViewSet, PatientDataViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'patients-data', PatientDataViewSet)

urlpatterns = router.urls