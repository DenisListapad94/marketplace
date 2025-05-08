from django.urls import path
from shop_api.views import ProductList,ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
]