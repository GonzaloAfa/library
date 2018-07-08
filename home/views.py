from django.shortcuts import render

def index(request):
    data = {}
    return render(request, 'home/index.html', data )
