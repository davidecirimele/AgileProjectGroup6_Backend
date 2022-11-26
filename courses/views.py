from django.shortcuts import render
from rest_framework import viewsets

from courses.models import Discipline
from courses.serializers import DisciplineSerializer


# Create your views here.

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer