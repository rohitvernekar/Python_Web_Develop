from django.template.loader import get_template
from django.template import Template,Context
from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime
 
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    #t=Template("<html><body> It is now {{current_date}}.</body></html>")
    #html=t.render(Context({'current_date':now}))
    #t=get_template('current_datetime.html')
    #html=t.render(Context({'current_date':now}))
    html=render(request,'current_datetime.html',{'current_date':now})
    
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def ua_display_good1(request):
    try:
        ua=request.META['HTTP_USER_AGENT']
    except KeyError:
        ua='unknown'
    return HttpResponse("Your browser is %s" % ua)


def display_meta(request):
    values=request.META.items()
    values.sort()
    html=[]
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
