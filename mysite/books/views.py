from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    import pdb;pdb.set_trace()
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        #if not q:
        #    error = True
        books=Book.objects.filter(title__icontains=q)
        return render(request,'search_results.html',{'books':books,'query':q})
    else:
        error=True
        return render(request,'search_form.html',{'error': error})
