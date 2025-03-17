from django.urls import path
from shop.views import first_view

urlpatterns = [
    path('hello/', first_view),
]