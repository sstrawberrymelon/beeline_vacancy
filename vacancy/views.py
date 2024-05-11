from rest_framework.viewsets import ModelViewSet

from vacancy.models import Vacancy
from vacancy.serializers import VacancyListSerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer