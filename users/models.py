from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
