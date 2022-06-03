from django.shortcuts import render

def index(request):
    context = {
        'main_page': 'Programação em Django'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
