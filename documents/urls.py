from django.urls import path
from documents.views import DocumentIDAPIView, StudentsAPIView, DegreeAPIView

urlpatterns = [
    path("document", DocumentIDAPIView.as_view()),
    path("document/<str:pk>",DocumentIDAPIView.as_view()),
    path("degree", DegreeAPIView.as_view()),
    path("degree/<str:pk>",DegreeAPIView.as_view()),
    path("student", StudentsAPIView.as_view()),
    path("student/<str:pk>",StudentsAPIView.as_view()),
]