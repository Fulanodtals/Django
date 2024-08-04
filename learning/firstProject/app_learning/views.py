from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    return render(request,'users/index.html')

def users(request):
    new_user = User()
    new_user.age = request.POST.get('idade')
    for names in new_user.name:
        if names == request.POST.get('nome'):
            print('nome ja usado')
            pass
        else:
            new_user.name = request.POST.get('nome')


    new_user.save()#salva na db

    #exivir os usuarios na nova pagina
    return_users = {
        'usuarios': User.objects.all()#retorna todas as informacoes
    }

    #retornar para a pagina
    return render(request, 'users/users.html', return_users)