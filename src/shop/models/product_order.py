from django.db import models
from shop.models.base import TimeConfig

class ProductOrder(TimeConfig):
    product = models.ForeignKey(
        to="Product",
        on_delete=models.CASCADE,
        related_name="product_order"
    )
    order = models.ForeignKey(
        to="Order",
        on_delete=models.CASCADE,
        related_name="product_order"
    )

    detail = models.CharField(max_length=50,null=True,blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "order"], name="unique_product_order"
            )
        ]

    def __str__(self):
        return f"{self.detail}"
