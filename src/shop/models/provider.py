from django.db import models
from shop.models.base import TimeConfig

class Provider(TimeConfig):
    name = models.CharField(max_length=40)
    country=models.CharField(max_length=40,null=True,blank=True)
    zip_address = models.CharField(max_length=40,null=True,blank=True)


    def __str__(self):
        return  f"{self.name}"