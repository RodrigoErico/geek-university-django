from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contato.html')

def product(request):
    return render(request, 'produto.html')
