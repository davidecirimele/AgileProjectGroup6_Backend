from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.views import DisciplineViewSet

router = SimpleRouter()
router.register('',DisciplineViewSet, basename = "documents")

urlpatterns = router.urls