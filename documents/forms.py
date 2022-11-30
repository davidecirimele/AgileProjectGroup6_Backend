from django import forms

from documents.models import Document


class DocumentIDform(forms.Form):
    id_number = forms.CharField(max_length=10)
    type = forms.CharField(max_length=10)
    country_of_issue = forms.CharField(max_length=20)
    date_of_issue = forms.DateField(input_formats=("%d/%m/%Y",))
    date_of_expiration = forms.DateField(input_formats=("%d/%m/%Y",))
    authority_issuing_the_document = forms.CharField(max_length=20)

class SecondaryEducationForm(forms.Form):
    student_id = forms.CharField(max_length=10)
    year_of_enrollment = forms.DateField(input_formats=("%d/%m/%Y",))
    year_of_graduation = forms.DateField(input_formats=("%d/%m/%Y",))
    country = forms.CharField(max_length=10)

class BachelorsDegreeForm(forms.ModelForm):
    student_id = forms.CharField(max_length=10)
    university_nation = forms.CharField(max_length=15)
    year_of_enrollment = forms.DateField(input_formats=("%d/%m/%Y",))
    year_of_graduation = forms.DateField(input_formats=("%d/%m/%Y",))
    bachelors_grade = forms.CharField(max_length=10)
    minimum_bachelor_mark = forms.IntegerField()
    maximum_bachelor_mark = forms.IntegerField()
    discipline = forms.CharField(max_length=20)

class MastersDegreeForm(forms.ModelForm):
    student_id = forms.CharField(max_length=10)
    university_nation = forms.CharField(max_length=15)
    year_of_enrollment = forms.DateField(input_formats=("%d/%m/%Y",))
    year_of_graduation = forms.DateField(input_formats=("%d/%m/%Y",))
    masters_grade = forms.CharField(max_length=10)
    minimum_masters_grade = forms.IntegerField()
    maximum_masters_grade = forms.IntegerField()
    discipline = forms.CharField(max_length=20)

class DoctorateForm(forms.ModelForm):
    student_id = forms.CharField(max_length=10)
    university_nation = forms.CharField(max_length=15)
    year_PhD_started = forms.DateField(input_formats=("%d/%m/%Y",))
    year_PhD_ended = forms.DateField(input_formats=("%d/%m/%Y",))
    doctorate_grade = forms.CharField(max_length=10)
    minimum_doctorate_mark = forms.IntegerField()
    maximum_doctorate_mark = forms.IntegerField()
    discipline = forms.CharField(max_length=20)