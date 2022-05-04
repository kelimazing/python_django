from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, AccessRecord, Webpage
from . import forms
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    my_dict = {'insert_me': "I am from views.py!"}
    return render(request, 'index.html', context=my_dict)

def guitar(request):
    return render(request, 'guitar.html')

def table(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'acc_rec': webpages_list}
    return render(request,'table.html', context=date_dict)

def form_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT AREA: "+form.cleaned_data['textarea']) 


    return render(request, 'forms.html', {'form':form})
