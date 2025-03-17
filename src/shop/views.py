from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return HttpResponse("<h1>Hello Django</h1>")
# Create your views here.
# MTV
# Model => table db
# Template => html
# Views => controller
