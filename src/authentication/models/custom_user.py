from django.contrib.auth.models import AbstractUser
from django.db import models
from shop.models.base import TimeConfig

class CustomUser(AbstractUser,TimeConfig):
    phone=models.CharField(max_length=20)


    def __str__(self):
        return  f"{self.username} "