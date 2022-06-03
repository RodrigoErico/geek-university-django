from django.shortcuts import render

def index(request):
    print(f'Usuário é -> {request.user}')
    if str(request.user) == 'AnonymousUser':
        test = 'Usuário não está Logado!'
    else:
        test = 'Usuário está Logado!'
    
    context = {
        'main_page': 'Programação em Django',
        'login': test
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
