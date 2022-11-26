from django.urls import path
from rest_framework.routers import SimpleRouter

from documents.views import DocumentViewSet

router = SimpleRouter()
router.register('',DocumentViewSet, basename = "documents")

urlpatterns = router.urls