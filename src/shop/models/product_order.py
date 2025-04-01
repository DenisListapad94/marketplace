from django.db import models


class ProductOrder(models.Model):
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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "order"], name="unique_product_order"
            )
        ]

    def __str__(self):
        return f"{self.detail}"
