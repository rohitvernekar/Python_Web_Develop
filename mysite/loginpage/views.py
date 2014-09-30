from django.http import HttpResponseRedirect
from django.shortcuts import render
from login import LoginForm

def login(request):
    import pdb;pdb.set_trace()
    if request.method == 'POST':
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            cleandata=loginform.cleaned_data
            return HttpResponseRedirect('/index/')
    else:
       loginform=LoginForm()
    return render(request,'login_form.html', {'loginform': loginform})

def index(request):
    return render(request,'index_form.html') 
