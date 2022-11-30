from django.shortcuts import render
from django.http import *
from rest_framework import viewsets

from documents.models import Document, SecondaryEducation, BachelorsDegree, Student, MastersDegree, Doctorate
from documents.serializers import DocumentSerializer, SecondaryEducationSerializer, BachelorsDegreeSerializer, \
    StudentSerializer, MastersDegreeSerializer, DoctorateSerializer

from documents.forms import *


# Create your views here.

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def addIdentityDocument(request):
        if request.method == "POST":
            form = DocumentIDform(request.POST)
            #if form.is_valid():
            form.save()
        else:
            form = DocumentIDform()
        return HttpResponse()
        #id number is unique, so a document can be added only if not exists in the database
        #doc = Document(id_number=id, type=type, country_of_issue=country, date_of_issue=issue,
        #               date_of_expiration=expiry, authority_issuing_the_document=authority)

        #doc.save()


    def getDocuments(self):
        return self.queryset

    def getDocumentById(self,id):
        return Document.objects.filter(id_number=id)


class SecondaryEducationViewSet(viewsets.ModelViewSet):
    serializer_class = SecondaryEducationSerializer

    def addSecondaryEducation(id, enrollment,graduation,country):
        se = SecondaryEducation(student_id= id, year_of_enrollment=enrollment,
                                year_of_graduation=graduation,country=country)
        se.save()

    def getSecondaryEducationOfTheStudent(id):
        return SecondaryEducation.objects.filter(student_id=id)

class BachelorsDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = BachelorsDegreeSerializer

    def addBachelorsDegree(id,university,enrollment,graduation,grade,min,max,discipline):
        bd = BachelorsDegree(student_id=id,university_nation=university,year_of_enrollment=enrollment,
                             year_of_graduation=graduation,bachelors_grade=grade,minimum_bachelor_mark=min,
                             maximum_bachelor_mark=max,discipline=discipline)
        bd.save()

    def getBachelorsDegreeOfTheStudent(id):
        return BachelorsDegree.objects.filter(student_id=id)


class MastersDegreeViewSet(viewsets.ModelViewSet):
    serializer_class = MastersDegreeSerializer

    def addMastersDegree(id, university, enrollment, graduation, grade, min, max, discipline):
        md = MastersDegree(student_id=id, university_nation=university, year_of_enrollment=enrollment,
                             year_of_graduation=graduation, masters_grade=grade, minimum_masters_grade=min,
                             maximum_masters_grade=max, discipline=discipline)
        md.save()

    def getMastersDegreeOfTheStudent(id):
        return MastersDegree.objects.filter(student_id=id)

class DoctorateViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorateSerializer

    def addPhD(id, university, enrollment, graduation, grade, min, max, discipline):
        d = Doctorate(student_id=id, university_nation=university, year_PhD_started=enrollment,
                            year_PhD_ended=graduation, doctorate_grade=grade, minimum_doctorate_mark=min,
                            maximum_doctorate_mark=max, discipline=discipline)
        d.save()

    def getPhdByTheStudent(id):
        return Doctorate.objects.filter(student_id=id)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
