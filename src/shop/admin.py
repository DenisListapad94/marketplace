from django.contrib import admin

from shop.models import (
    Product,
    Order,
    ProductDetail,
    Provider,
    ProductOrder,
    Feedback
)
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)
admin.site.register(Feedback)