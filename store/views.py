from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def  all(request):
    products = Product.objects.all();
    context = {
        "products" :  products,
        "MediaUrl" : "http://localhost:8000/media/"
    }
    return render(request, "all.html", context)
