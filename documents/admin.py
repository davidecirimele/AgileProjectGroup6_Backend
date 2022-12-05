from django.contrib import admin

from documents.models import Document, Degree, Student

# Register your models here.

admin.site.register(Document)
admin.site.register(Degree)
admin.site.register(Student)