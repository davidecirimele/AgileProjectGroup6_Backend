import json

from allauth.account.views import login
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status

from .models import Student, StudentEnrolled, Document, Degree
from .permissions import IsOwner, IsHe, IsAdmin
from .serializers import StudentSerializer, DisciplineSerializer, DocumentSerializer, DegreeSerializer, \
    StudentEnrolledSerializer, CustomLoginSerializer, CustomRegisterSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from . import models


class DisciplineList(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset=models.Discipline.objects.all()
    serializer_class = DisciplineSerializer

class StudentList(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsHe,
    ]
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(username=self.request.user)
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
        IsHe,
    ]
    queryset=models.Student.objects.all()
    serializer_class = StudentSerializer

class DocumentList(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    queryset=models.Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
    

class DegreeList(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
        IsOwner,
    ]
    serializer_class = DegreeSerializer

    def get_queryset(self):
        return Degree.objects.filter(student_id=self.request.user)

class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
        IsOwner,
    ]
    queryset=models.Degree.objects.all()
    serializer_class = DegreeSerializer

class StudentEnrolledList(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
        IsHe,
    ]
    serializer_class = StudentEnrolledSerializer

    def get_queryset(self):
        return Degree.objects.filter(student_id=self.request.user)

class StudentEnrolledDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
        IsHe
    ]
    queryset=models.StudentEnrolled.objects.all()
    serializer_class = StudentEnrolledSerializer


class CustomRegisterView(RegisterView):
    queryset = Student.objects.all()

class StudentAPIView(APIView):
    @staticmethod
    def get(request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    class GenericStudentAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin,
                                mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
        serializer_class = StudentSerializer
        queryset = Student.objects.all()

        lookup_field = 'id'

        def get(self,request, username = None):
            if username:
                return self.retrieve(request)
            else:
                return self.list(request)

        def post(self, request):
            return self.create(request)

        def put(self, request, username = None):
            return self.update(request,username)

        def delete(self, request, username):
            return self.destroy(request, username)

    class Login(LoginView):
        permission_classes = (permissions.AllowAny,)

        def post(self, request, *args, **kwargs):
            serializer = CustomLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            return super().post(request, format=None)
