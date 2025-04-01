from django.db import models

class ProductDetail(models.Model):

    height=models.FloatField(null=True,blank=True)
    weight=models.FloatField(null=True,blank=True)
    description_all = models.CharField(max_length=256)

    product = models.OneToOneField(
        to="Product",
        on_delete=models.CASCADE,
        related_name="product_detail"
    )


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)