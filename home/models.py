from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models

from backend import settings


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, codice_fiscale, gender, password, dob, region_of_birth,country, phone_no):
        if not email:
            raise ValueError('Users must have email Address')

        email = self.normalize_email(email)

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            codice_fiscale = codice_fiscale,
            gender = gender,
            password = password,
            dob = dob,
            region_of_birth = region_of_birth,
            country = country,
            phone_no = phone_no
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, first_name,last_name,email,username,codice_fiscale,gender,password,dob,region_of_birth,country,phone_no):
        user = self.model(
            first_name="Clark",
            last_name="Kent",
            email=email,
            username=username,
            codice_fiscale="KNTCRK01C01A123U",
            gender="M",
            password=password,
            dob='1979-01-01',
            region_of_birth="Calabria",
            country="Rende",
            phone_no="1234567890"
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

GENDER_OPTIONS = (('M','MALE'),('F','FEMALE'))

class Student(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=100)
    codice_fiscale = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    dob = models.DateField(max_length=100)
    region_of_birth = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100, unique= True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','email','password','codice_fiscale','gender','dob','region_of_birth','country','phone_no']
    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    def is_staff(self):
        return self.is_staff

    def is_admin(self):
        return self.is_admin

    def is_superuser(self):
        return self.is_superuser

    class Meta:
        app_label = 'home'

class Discipline(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Document(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id_number = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=15)
    country_of_issue = models.CharField(max_length=30)
    date_of_issue = models.DateField()
    date_of_expiration = models.DateField()
    authority_issuing_the_document = models.CharField(max_length=50)
    document_img = models.ImageField(upload_to="templates/users/%Y/%m/%d/",blank=True)

    def __str__(self):
        return self.id_number


class Degree(models.Model):
    student_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    type_of_degree = models.CharField(max_length=15)
    university_nation = models.CharField(max_length=15)
    year_of_enrollment = models.DateField()
    year_of_graduation = models.DateField()
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)

    def __str__(self):
        return self.student_id


class StudentEnrolled(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    course_selected = models.CharField(max_length=20, default='BachelorsDegree')

    def __str__(self):
        return self.document_id