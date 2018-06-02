from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def books(request):
    return HttpResponse('<h1>list books</h1>')

# Create your views here.
def search(request):
    
    return render(request, 'book/search.html', {})
