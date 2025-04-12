from django.db import models
from shop.models.base import TimeConfig

class ProductDetail(TimeConfig):

    height=models.FloatField(null=True,blank=True)
    weight=models.FloatField(null=True,blank=True)
    description_all = models.CharField(max_length=256)

    product = models.OneToOneField(
        to="Product",
        on_delete=models.CASCADE,
        related_name="product_detail"
    )

