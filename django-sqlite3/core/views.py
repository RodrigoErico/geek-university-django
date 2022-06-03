from django.shortcuts import render
from .models import Product

def index(request):  
    products = Product.objects.all()
    
    context = {
        'main_page': 'Programação em Django',
        'products': products
    }
    return render(request, 'index.html', context)


def product(request, pk):
    prod = Product.objects.get(id=pk)
    
    context = {
        'product': prod
    }
    return render(request, 'produto.html', context)
