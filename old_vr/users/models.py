from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    phone = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
