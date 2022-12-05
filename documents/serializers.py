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
        fields = ('student_id', 'university_nation', 'year_of_enrollment', 'year_of_graduation', 'bachelors_grade',
                  'minimum_bachelor_mark', 'maximum_bachelor_mark','discipline')
        model = BachelorsDegree

class MastersDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'university_nation', 'year_of_enrollment', 'year_of_graduation', 'masters_grade',
                  'minimum_masters_grade', 'maximum_masters_grade','discipline')

class DoctorateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'university_nation', 'year_PhD_started', 'year_PhD_ended', 'doctorate_grade',
                  'minimum_doctorate_mark', 'maximum_doctorate_mark','discipline')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('document_id','course_grade','secondary_education','bachelors_degree','masters_degree','doctorate')
        model = Student
