# Create your views here.
from django.template.loader import get_template
from django.template import Template,Context
from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address')
        if not errors:
            send_mail(
                request.POST('subject'),
                request.POST('message'),
                request.POST.get('email'),'grohit@zeomega.com'),
                ['rohitvernekar0072gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/') 
    return render(request,'contact_form.html'),{
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message',''),
        'email': request.POST.get('email',''),
    })

