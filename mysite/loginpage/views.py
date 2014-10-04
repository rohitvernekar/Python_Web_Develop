from django.http import HttpResponseRedirect
from django.shortcuts import render
from login import LoginForm
from registration import RegistrationForm

def login(request):
    if request.method == 'POST':
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            cleandata=loginform.cleaned_data
            return HttpResponseRedirect('/index/')
    else:
       loginform=LoginForm()
    return render(request,'login_form.html', {'loginform': loginform})


def signup(request):
    return render(request,'signup_form.html')    

def index(request):
    return render(request,'index_form.html') 

def registration(request):
    if request.method=='POST':
        registrationform = RegistrationForm(request.POST)
        if registrationform.is_valid():
            cleandata = registrationform.cleaned_data
            return HttpResponseRedirect("/success/")
    else:
        registrationform=RegistrationForm()
    
    return render(request,"registration/registration_form.html",{"registrationform": registrationform})

def success(request):
    return render(request,'registration/success_form.html')
