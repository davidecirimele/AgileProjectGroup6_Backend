from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    codice_fiscal = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    region_of_birth = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)

    
    #class Meta:
        #verbrose_name_plural = "1. Students"

class Discipline(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Document(models.Model):
    id_number = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=15)
    country_of_issue = models.CharField(max_length=30)
    date_of_issue = models.DateField()
    date_of_expiration = models.DateField()
    authority_issuing_the_document = models.CharField(max_length=50)

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