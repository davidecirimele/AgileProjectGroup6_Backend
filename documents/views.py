from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import Student, Document, Degree
from documents.serializers import DocumentSerializer,StudentSerializer, DegreeSerializer


class DocumentIDAPIView(APIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get_document(self,pk):
        try:
            return Document.objects.get(id_number = pk)
        except Document.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_document(pk)
            serializer = DocumentSerializer(data)
        else:
            data = Document.objects.all()
            serializer = DocumentSerializer(data, many=True)

            return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        document_to_update = Document.objects.get(pk=pk)
        serializer = StudentSerializer(instance=document_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Student Updated Successfully',
            'data': serializer.data
        }

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
        document_to_delete = Document.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class DegreeAPIView(APIView):
    serializer_class = DegreeSerializer
    queryset = Degree.objects.all()

    def get_degree(self,pk):
        try:
            return Degree.objects.get(pk = pk)
        except Degree.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_degree(pk)
            serializer = DegreeSerializer(data)
        else:
            data = Degree.objects.all()
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
        document_to_delete = Degree.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class StudentsAPIView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_student(self,pk):
        try:
            return Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)

            return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = StudentSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        student_to_update = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Student Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = Student.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })
