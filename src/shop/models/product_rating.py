from shop.models.base import TimeConfig,Rating
from django.db import models

class ProductRating(Rating,TimeConfig):

    product = models.ForeignKey(
        to="Product",
        related_name="product_rating",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    product_detail = models.CharField(max_length=60,null=True)
