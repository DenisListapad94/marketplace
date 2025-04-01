from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=40)
    country=models.CharField(max_length=40,null=True,blank=True)
    zip_address = models.CharField(max_length=40,null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.name}"