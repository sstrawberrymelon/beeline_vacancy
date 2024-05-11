from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.VacancyViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
