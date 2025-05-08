from django.urls import path,re_path
# from shop.views import first_view,second_view,first_html,index
from shop.views import  info
from shop.views import TemplateViewHome, ProductView, UserOrdersListViews, ProductCreateView
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path("hello/<path:year>/", first_view),
    # path("", index),
    # path("hello/first_html",first_html),
    # re_path(r"^reg/(?P<year>2[0-9]{3})/$", second_view),
    path("", TemplateViewHome.as_view(), name="home"),
    path("info", info, name="info"),
    path("products", ProductView.as_view(), name="products"),
    path("user_orders", UserOrdersListViews.as_view(), name="user_orders"),
    path("add_product",ProductCreateView.as_view(),name="product_form"),
]


