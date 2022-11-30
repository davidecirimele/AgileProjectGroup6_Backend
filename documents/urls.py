from django.urls import path

from documents.views import DocumentViewSet

urlpatterns = [
    path('add-document-id/',DocumentViewSet.addIdentityDocument)
]