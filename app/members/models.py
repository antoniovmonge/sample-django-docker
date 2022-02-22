from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Member(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    fun_fact = models.TextField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
