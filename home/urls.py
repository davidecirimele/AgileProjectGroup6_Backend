from django.urls import path
from . import views
# from .views import DocumentIDAPIView


urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('student-login',views.student_login),
    path('discipline/', views.DisciplineList.as_view()),
    path("document/", views.DocumentIDAPIView.as_view()),
    path("document/<str:pk>",views.DocumentIDAPIView.as_view()),
    path("degree/", views.DegreeAPIView.as_view()),
    path("degree/<str:pk>",views.DegreeAPIView.as_view()),
    path("studentenrolled/", views.StudentEnrolledAPIView.as_view()),
    path("studentenrolled/<str:pk>",views.StudentEnrolledAPIView.as_view()),
]
