from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import views
from django.urls import path, include

router = DefaultRouter()
router.register('', views.ContactMessageViewSet)

urlpatterns = [
    path('feedback/', views.UserRegisterView.as_view()),
]
