from rest_framework import serializers

from documents.models import Document, Degree, Student


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_number', 'type', 'country_of_issue', 'date_of_issue', 'date_of_expiration',
                  'authority_issuing_the_document')
        model = Document

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'type_of_degree','university_nation', 'year_of_enrollment', 'year_of_graduation','discipline')
        model = Degree

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('document_id','course_selected')
        model = Student
