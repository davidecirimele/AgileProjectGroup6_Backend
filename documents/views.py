from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import SecondaryEducation, BachelorsDegree, Student, MastersDegree, Doctorate, Document
from documents.serializers import DocumentSerializer, SecondaryEducationSerializer, BachelorsDegreeSerializer, \
    StudentSerializer, MastersDegreeSerializer, DoctorateSerializer


class DocumentIdViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

class DocumentIDAPIView(APIView):

    def get_document(self,pk):
        try:
            return Document.objects.get(pk = pk)
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




class SecondaryEducationViewSet(viewsets.ModelViewSet):
    serializer_class = SecondaryEducationSerializer
    queryset = SecondaryEducation.objects.all()

class SecondaryEducationAPIView(APIView):

    def get_secondaryeducation(self,pk):
        try:
            return SecondaryEducation.objects.get(pk = pk)
        except SecondaryEducation.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_secondaryeducation(pk)
            serializer = SecondaryEducationSerializer(data)
        else:
            data = SecondaryEducation.objects.all()
            serializer = SecondaryEducationSerializer(data, many=True)

            return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = SecondaryEducationSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = SecondaryEducation.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class BachelorsDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = BachelorsDegreeSerializer
    queryset = BachelorsDegree.objects.all()

class BachelorsDegreeAPIView(APIView):

    def get_bachelorsdegree(self,pk):
        try:
            return BachelorsDegree.objects.get(pk = pk)
        except BachelorsDegree.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_bachelorsdegree(pk)
            serializer = BachelorsDegreeSerializer(data)
        else:
            data = BachelorsDegree.objects.all()
            serializer = BachelorsDegreeSerializer(data, many=True)

            return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = BachelorsDegreeSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = BachelorsDegree.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })

class MastersDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = MastersDegreeSerializer
    queryset = MastersDegree.objects.all()

class MastersDegreeAPIView(APIView):

    def get_mastersdegree(self,pk):
        try:
            return MastersDegree.objects.get(pk = pk)
        except MastersDegree.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_mastersdegree(pk)
            serializer = MastersDegreeSerializer(data)
        else:
            data = MastersDegree.objects.all()
            serializer = MastersDegreeSerializer(data, many=True)

            return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = MastersDegreeSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = MastersDegree.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class DoctorateViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorateSerializer
    queryset = Doctorate.objects.all()

class DoctorateAPIView(APIView):

    def get_doctorate(self,pk):
        try:
            return Doctorate.objects.get(pk = pk)
        except Doctorate.DoesNotExist:
            return Http404

    def get(self,request,pk = None,format = None):
        if pk:
            data = self.get_doctorate(pk)
            serializer = DoctorateSerializer(data)
        else:
            data = Doctorate.objects.all()
            serializer = DoctorateSerializer(data, many=True)

            return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = DoctorateSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message':'Document added succesfully',
            'data':serializer.data
        }

        return response

    def delete(self, request, pk, format = None):
        document_to_delete = Doctorate.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentsAPIView(APIView):

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

    def delete(self, request, pk, format = None):
        document_to_delete = Student.objects.get(pk = pk)

        document_to_delete.delete()

        return Response({
            'message':'Document deleted succesfully'
        })
