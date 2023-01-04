from django.urls import path
from . import views
# from .views import DocumentIDAPIView


urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('student/<str:pk>', views.StudentDetail.as_view()),
    path('discipline/', views.DisciplineList.as_view()),
    path('discipline/<str:pk>', views.DisciplineDetail.as_view()),
    path("document/", views.DocumentList.as_view()),
    path("document/<str:pk>",views.DocumentDetail.as_view()),
    path("degree/", views.DegreeList.as_view()),
    path("degree/<str:pk>",views.DegreeDetail.as_view()),
    path("studentenrolled/", views.StudentEnrolledList.as_view()),
    path("studentenrolled/<str:pk>",views.StudentEnrolledDetail.as_view()),
]
