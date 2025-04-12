from django.contrib import admin

from shop.models import (
    Order,
    ProductDetail,
    Provider,
    ProductOrder,
    Feedback,
    Rating,
    ProductRating,
    ProviderRating
)
# Register your models here.
admin.site.register(Order)
admin.site.register(ProductDetail)
admin.site.register(Provider)
admin.site.register(ProductOrder)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(ProductRating)
admin.site.register(ProviderRating)
