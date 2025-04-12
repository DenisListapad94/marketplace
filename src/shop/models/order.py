from django.db import models
from django.conf import settings
from shop.models.base import TimeConfig

class Order(TimeConfig):
    name = models.CharField(max_length=40)
    description=models.CharField(max_length=256,blank=True)



    product = models.ManyToManyField(
        to="Product",
        through="ProductOrder",
        related_name='order',
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True,
        null=True
    )

    def __str__(self):
        return  f"{self.name}"