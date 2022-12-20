from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import StudentSerializer,DisciplineSerializer,DocumentSerializer,DegreeSerializer,StudentEnrolledSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from . import models


class DisciplineList(generics.ListCreateAPIView):
    queryset=models.Discipline.objects.all()
    serializer_class = DisciplineSerializer

class DocumentIDAPIView(APIView):
    serializer_class = DocumentSerializer
    queryset = models.Document.objects.all()

    def get_document(self,pk):
        try:
            return models.Document.objects.get(pk = pk)
        except Document.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_document(pk)
            serializer = DocumentSerializer(data)
        else:
            data = models.Document.objects.all()
            serializer = DocumentSerializer(data, many=True)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        document_to_update = models.Document.objects.get(pk=pk)
        serializer = DocumentSerializer(instance=document_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Documents Updated Successfully',
            'data': serializer.data
        }

        return response

    def post(self,request,format=None):
        data = request.data
        serializer = DocumentSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = models.Document.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })

    

class DegreeAPIView(APIView):
    serializer_class = DegreeSerializer
    queryset = models.Degree.objects.all()

    def get_degree(self,pk):
        try:
            return models.Degree.objects.get(pk = pk)
        except Degree.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_degree(pk)
            serializer = DegreeSerializer(data)
        else:
            data = models.Degree.objects.all()
            serializer = DegreeSerializer(data, many=True)

        return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = DegreeSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = models.Degree.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class StudentEnrolledAPIView(APIView):
    queryset = models.StudentEnrolled.objects.all()
    serializer_class = StudentEnrolledSerializer

    def get_student(self,pk):
        try:
            return models.StudentEnrolled.objects.get(pk = pk)
        except StudentEnrolled.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentEnrolledSerializer(data)
        else:
            data = models.StudentEnrolled.objects.all()
            serializer = StudentEnrolledSerializer(data, many=True)

        return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = StudentEnrolledSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Student added succesfully',
            'data':serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        student_to_update = models.StudentEnrolled.objects.get(pk=pk)
        serializer = StudentEnrolledSerializer(instance=student_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Student Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = models.StudentEnrolled.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Student deleted succesfully'
        })

class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def student_login(request):
    username=request.POST['username']
    password=request.POST['password']
    studentData=models.Student.objects.get(username=username,password=password)
    if studentData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool': False})

