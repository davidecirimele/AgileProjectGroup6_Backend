from rest_framework import serializers

from courses.models import Discipline


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (['name'])
        model = Discipline
