from rest_framework.viewsets import ModelViewSet

from vacancy import serializers
from vacancy.models import Vacancy
from vacancy.serializers import VacancyListSerializer, VacancyDetailSerializer


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()


    def get_serializer_class(self):
        """
        Вернуть соответствующий класс сериализатора в зависимости от запрашиваемого действия.
        """
        if self.action == 'list':
            return serializers.VacancyListSerializer
        return serializers.VacancyDetailSerializer



9