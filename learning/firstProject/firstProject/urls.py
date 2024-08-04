

from django.urls import path
#importrando a views da aplicacao
from app_learning import views

urlpatterns = [
    #rota, view responsavel e nome de referencia
    path('', views.home, name='home'),
    path('/users', views.users, name='user_list'),

]



