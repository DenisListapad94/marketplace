from django.db import models

class Queue(models.Model):
    value = models.PositiveIntegerField()