from importlib.resources import _

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import Student, Discipline, Document, Degree, StudentEnrolled


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email','username', 'codice_fiscale', 'gender', 'password', 'dob', 'region_of_birth', 'country', 'phone_no']

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ['id','name']
        
class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(default=get_user_model(), read_only=True)
    date_of_issue = serializers.CharField()
    date_of_expiration = serializers.CharField()
    class Meta:
        fields = ('owner','id_number', 'type', 'country_of_issue', 'date_of_issue', 'date_of_expiration',
                  'authority_issuing_the_document','document_img')
        model = Document
        read_only_fields = ['owner']

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('student_id', 'type_of_degree','university_nation', 'year_of_enrollment', 'year_of_graduation','discipline')
        model = Degree
        

class StudentEnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('document_id','course_selected')
        model = StudentEnrolled

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email= serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    codice_fiscale = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    dob = serializers.CharField(required=True)
    region_of_birth = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()


        data_dict['first_name'] = self.validated_data.get('first_name','')
        data_dict['last_name'] = self.validated_data.get('last_name','')
        data_dict['username'] = self.validated_data.get('username','')
        data_dict['email'] = self.validated_data.get('email','')
        data_dict['password1'] = self.validated_data.get('password1','')
        data_dict['password2'] = self.validated_data.get('password2','')
        data_dict['codice_fiscale'] = self.validated_data.get('codice_fiscale','')
        data_dict['gender'] = self.validated_data.get('gender','')
        data_dict['dob'] = self.validated_data.get('dob','')
        data_dict['region_of_birth'] = self.validated_data.get('region_of_birth','')
        data_dict['country'] = self.validated_data.get('country','')
        data_dict['phone_no'] = self.validated_data.get('phone_no','')

        return data_dict

class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data
