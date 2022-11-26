from django.contrib import admin

from documents.models import Document, SecondaryEducation, BachelorsDegree, Student

# Register your models here.

admin.site.register(Document)
admin.site.register(SecondaryEducation)
admin.site.register(BachelorsDegree)
admin.site.register(Student)