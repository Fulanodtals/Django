from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')


def users(request):
    get_user = User()
    get_user.password = request.POST.get('idade')
    for names in get_user.name:
        if names == request.POST.get('nome'):
            print('nome ja usado')
            pass
        else:
            get_user.name = request.POST.get('nome')


    #exivir os usuarios na nova pagina
    '''    
    return_users = {
        'usuarios': User.objects.all()#retorna todas as informacoes
    }
    '''
    #retornar para a pagina
    return render(request, 'users/users.html')#, return_users