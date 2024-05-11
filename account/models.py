from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = models.CharField(_('Phone number'), max_length=200, unique=True)
    password = models.CharField(('Password'), max_length=128)
    email = models.EmailField(('Email'), unique=True)
    first_name = models.CharField(('First Name'), max_length=150)
    last_name = models.CharField(('Last Name'), max_length=150)




    def __str__(self):
        return self.phone_number
