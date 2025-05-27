from django.contrib import admin
from django.db.models import F
from django.utils.safestring import mark_safe
from shop.models import (
    Product,
    ProductRating,
    Order,
)


class ProductOrderInline(admin.TabularInline):
    model = Order.product.through



class ProductRatingInline(admin.StackedInline):
    model = ProductRating
    extra = 1

@admin.action(description="Mark selected discount 5 persent")
def make_discount(modeladmin, request, queryset):
    queryset.update(price = F("price") * 0.95)


@admin.display(description='фото')
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')



class ProductAdmin(admin.ModelAdmin):
    # fields = ("name","description","photo",("price","count_items",))
    fieldsets = [
        (
            None,
            {
                "fields": ("name","provider",("price","count_items")),
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["photo", "description"],
            },
        ),
    ]
    readonly_fields = ("description",)
    list_display =  ("name","description","category","price","count_items",get_html_photo)
    list_display_links = ("name",)
    list_editable = ("price",)
    # list_per_page = 5
    list_filter  = ("category",)
    search_fields = ("name","price")
    ordering = ("-category","name")
    inlines = [
        ProductRatingInline,
        ProductOrderInline,
    ]
    actions = (make_discount,)

    # save_on_top = True

product_admin = admin.site.register(Product,ProductAdmin)





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