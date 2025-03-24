from django.utils.translation import gettext_lazy as _

from django.db import models


class ProductCategory(models.TextChoices):
    TECHNIQUE = "TQ", _("Technique")
    BOOK = "BK", _("Book")
    FURNITURE = "FR", _("Furniture")
    SPORT = "SP", _("Sport")
    CHILDREN = "CN", _("Children")
    DEFAULT = "DF", _("Default")


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    category = models.CharField(
        choices=ProductCategory,
        default=ProductCategory.DEFAULT
    )
    rating = models.FloatField(null=True)
    photo = models.ImageField(null=True)
    count_items = models.IntegerField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.name} count: {self.count_items}"
