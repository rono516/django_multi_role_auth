from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    ROLE_GROUPS = (
        ('administrator', 'Administrator'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('staff', 'Staff')
    )

    role = models.CharField(max_length=15, choices=ROLE_GROUPS)
    middle_name = models.CharField(max_length=200)