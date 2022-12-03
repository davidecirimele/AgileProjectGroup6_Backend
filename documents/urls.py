from django.urls import path, include
from rest_framework import routers

from documents import views
from documents.views import DocumentIDAPIView, SecondaryEducationAPIView, BachelorsDegreeAPIView, MastersDegreeAPIView, \
    DoctorateAPIView, StudentsAPIView

router = routers.DefaultRouter()
router.register(r'documents',views.DocumentIdViewSet,'document')
router.register(r'secondaryeducations',views.SecondaryEducationViewSet,'secondaryeducation')
router.register(r'bachelorsdegrees',views.BachelorsDegreeViewSet,'bachelorsdegree')
router.register(r'mastersdegrees',views.MastersDegreeViewSet,'mastersdegree')
router.register(r'doctorates',views.DoctorateViewSet,'doctorate')
router.register(r'students',views.StudentViewSet,'student')

urlpatterns = [
    path("iddoc/",include(router.urls)),
    path("document", DocumentIDAPIView.as_view()),
    path("document/<str:pk>",DocumentIDAPIView.as_view()),
    path("secondaryeducation", SecondaryEducationAPIView.as_view()),
    path("secondaryeducation/<str:pk>",SecondaryEducationAPIView.as_view()),
    path("bachelorsdegree", BachelorsDegreeAPIView.as_view()),
    path("bachelorsdegree/<str:pk>",BachelorsDegreeAPIView.as_view()),
    path("mastersdegree", MastersDegreeAPIView.as_view()),
    path("mastersdegree/<str:pk>",MastersDegreeAPIView.as_view()),
    path("doctorate", DoctorateAPIView.as_view()),
    path("doctorate/<str:pk>",DoctorateAPIView.as_view()),
    path("student", StudentsAPIView.as_view()),
    path("student/<str:pk>",StudentsAPIView.as_view()),
]