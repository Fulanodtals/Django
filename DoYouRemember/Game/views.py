from django.shortcuts import render
from .models import UserInput
# Create your views here.
def home(request):
    return render(request,'users/index.html')

def userInput(request):
    user_input = UserInput()
    user_input.user_text = request.POST.get('...')
    user_input.new_text  = request.POST.get('...')