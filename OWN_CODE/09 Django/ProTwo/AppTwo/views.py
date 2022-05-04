from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import forms
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    help = {'help_insert' : "HELP PAGE from views.py"}
    return render(request, 'help.html', context=help)

def user(request):
    users = User.objects.order_by('first_name')
    user_form = forms.User_Form()
    user_dict = {'user_db': users, 'form': user_form}

    if request.method == 'POST':
        user_form = forms.User_Form(request.POST)

        if user_form.is_valid():
            user_form.save(commit=True)



    return render(request, 'user.html', context=user_dict)
