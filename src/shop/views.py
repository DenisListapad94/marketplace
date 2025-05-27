from django.shortcuts import render,redirect,reverse, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from authentication.models import CustomUser
from shop.forms import ProductModelForm
from shop.models import Product
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

class TemplateViewHome(TemplateView):
    template_name = "home.html"

#
# def home(request):
#     return render(request, template_name="home.html")

def info(request):
    return render(request, template_name="info.html")

# @permission_required("shop.view_product", raise_exception=True)
# @cache_page(60 * 5,cache="default")
# def products(request):
#     from time import sleep
#     sleep(10)
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, template_name="products.html",context=context)

class ProductView(ListView):
    template_name = "products.html"
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

class UserOrdersListViews(ListView):
    template_name = "user_order_products.html"
    queryset =  CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')
    #queryset = CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')
        return context

# def user_orders(request):
#     users = CustomUser.objects.all().prefetch_related('orders').prefetch_related('orders__product')
#
#     context = {
#         "users": users
#     }
#     return render(request, template_name="user_order_products.html",context=context)

# @login_required(login_url="/auth/login",redirect_field_name="product_form")
# @permission_required("shop.add_product", raise_exception=True)
# def product_form(request):
#
#     context = {}
#
#     if request.method == "POST":
#         form = ProductModelForm(request.POST, request.FILE)
#         if form.is_valid():
#             form.save()
#             caches["default"].clear()
#             return redirect(reverse("products"))
#         context["form"] = form
#
#     context["form"] = ProductModelForm()
#
#
#     return render(request, template_name="product_form.html",context=context)



class ProductCreateView(PermissionRequiredMixin,CreateView):
    template_name = "product_form.html"
    model = Product
    # form_class = ProductModelForm
    fields = ["name","price","count_items","description","photo"]
    success_url = reverse_lazy("products")
    permission_required = ["shop.add_product"]
    # redirect_field_name = "product"

