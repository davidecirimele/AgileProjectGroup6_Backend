from rest_framework import serializers

from documents.models import Document, SecondaryEducation, BachelorsDegree, Student


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_number', 'type', 'country_of_issue', 'date_of_issue', 'date_of_expiration',
                  'authority_issuing_the_document')
        model = Document


class SecondaryEducationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'year_of_enrollment', 'year_of_graduation', 'country')
        model = SecondaryEducation


class BachelorsDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student', 'university_nation', 'year_of_enrollment', 'year_of_graduation', 'bachelors_grade',
                  'minimum_bachelor_mark', 'maximum_bachelor_mark')
        model = BachelorsDegree

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('document_id','secondary_education')
        model = Student
