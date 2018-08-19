from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def index(request):
    data = {}
    return render(request, 'home/index.html', data )
