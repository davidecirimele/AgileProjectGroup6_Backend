from django.shortcuts import render
from rest_framework import viewsets

from documents.models import Document, SecondaryEducation, BachelorsDegree, Student
from documents.serializers import DocumentSerializer, SecondaryEducationSerializer, BachelorsDegreeSerializer, \
    StudentSerializer


# Create your views here.

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SecondaryEducationViewSet(viewsets.ModelViewSet):
    queryset = SecondaryEducation.objects.all()
    serializer_class = SecondaryEducationSerializer

class BachelorsDegreeViewSet(viewsets.ModelViewSet):
    queryset = BachelorsDegree.objects.all()
    serializer_class = BachelorsDegreeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
