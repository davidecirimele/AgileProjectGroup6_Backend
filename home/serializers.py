from rest_framework import serializers
from .models import Student,Discipline,Document, Degree,StudentEnrolled


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'username', 'codice_fiscal', 'gender', 'password', 'confirm_password', 'dob', 'region_of_birth', 'country', 'phone_no']


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ['id','name']
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_number', 'type', 'country_of_issue', 'date_of_issue', 'date_of_expiration',
                  'authority_issuing_the_document')
        model = Document

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'type_of_degree','university_nation', 'year_of_enrollment', 'year_of_graduation','discipline')
        model = Degree
        

class StudentEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('document_id','course_selected')
        model = StudentEnrolled