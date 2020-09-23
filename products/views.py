from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products-list.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'products/product-details.html', context)

def say_hi(request, name):
    return render(request, 'say-hi.html', {'name': name})
    
def show_time(request):
    context = {'time': timezone.now()}
    return render(request, 'show-time.html', context)

