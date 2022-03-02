from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product
    }
    return render(request, 'store/product.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
