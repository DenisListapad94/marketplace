from django.shortcuts import render
from shop.models import Product

# users = [
#     {"user": "Ivan", "age": 24},
#     {"user": "david", "age": 29},
#     {"user": "peter", "age": 15},
#     {"user": "ann", "age": 34},
#     {"user": "Eva", "age": 31},
# ]
#
#
#
# def first_view(request, year):
#     return HttpResponse(f"<h1>Hello Django {year}</h1>")
#
#
# def second_view(request, year):
#     return HttpResponse(f"<h1>Hello Django {year}</h1>")
#
#
# def first_html(request):
#     context = {
#         "users": users,
#         "var_str": "hello_context"
#     }
#     return render(request, template_name='hello.html', context=context)

def home(request):
    return render(request, template_name="home.html")

def info(request):
    return render(request, template_name="info.html")


def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, template_name="products.html",context=context)