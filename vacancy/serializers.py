from rest_framework import serializers

from vacancy.models import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
