from django.db import models
from django.conf import settings

class Feedback(models.Model):
    title = models.CharField(max_length=40)
    description=models.CharField(max_length=256,null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(
        to="Product",
        on_delete=models.CASCADE,
        related_name='feedbacks',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        blank=True,
        null=True
    )

    def __str__(self):
        return  f"{self.title}"