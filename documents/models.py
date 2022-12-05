from django.db import models

from courses.models import Discipline


# Create your models here.

class Document(models.Model):
    id_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=10)
    country_of_issue = models.CharField(max_length=20)
    date_of_issue = models.DateField()
    date_of_expiration = models.DateField()
    authority_issuing_the_document = models.CharField(max_length=20)

    def __str__(self):
        return self.id_number


class SecondaryEducation(models.Model):
    student_id = models.ForeignKey(Document, on_delete=models.CASCADE, to_field='id_number')
    year_of_enrollment = models.DateField()
    year_of_graduation = models.DateField()
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.student_id


class BachelorsDegree(models.Model):
    student_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    university_nation = models.CharField(max_length=15)
    year_of_enrollment = models.DateField()
    year_of_graduation = models.DateField()
    bachelors_grade = models.CharField(max_length=10)
    minimum_bachelor_mark = models.IntegerField()
    maximum_bachelor_mark = models.IntegerField()
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)

    def __str__(self):
        return self.student_id

class MastersDegree(models.Model):
    student_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    university_nation = models.CharField(max_length=15)
    year_of_enrollment = models.DateField()
    year_of_graduation = models.DateField()
    masters_grade = models.CharField(max_length=10)
    minimum_masters_grade = models.IntegerField()
    maximum_masters_grade = models.IntegerField()
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)

    def __str__(self):
        return self.student_id

class Doctorate(models.Model):
    student_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    university_nation = models.CharField(max_length=15)
    year_PhD_started = models.DateField()
    year_PhD_ended = models.DateField()
    doctorate_grade = models.CharField(max_length=10)
    minimum_doctorate_mark = models.IntegerField()
    maximum_doctorate_mark = models.IntegerField()
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)

    def __str__(self):
        return self.student_id

class Student(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.PROTECT, to_field='id_number')
    course_grade = models.CharField(max_length=20, default='BachelorsDegree')
    secondary_education = models.ForeignKey(SecondaryEducation, on_delete=models.PROTECT)
    bachelors_degree = models.ForeignKey(BachelorsDegree, on_delete=models.PROTECT)
    masters_degree = models.ForeignKey(MastersDegree, on_delete=models.PROTECT)
    doctorate = models.ForeignKey(Doctorate, on_delete=models.PROTECT)

    def __str__(self):
        return self.document_id