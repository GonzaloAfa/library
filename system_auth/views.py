from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

# autentification
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# for redirect
from django.urls import reverse

# Create your views here.
def login(request):

    if not request.user.is_anonymous:
        return redirect('home' )

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        access = authenticate(username=username, password=password)

        if access is not None:
            if access.is_active:
                auth_login(request, access)
                return redirect('home')
            else:
                return redirect('login')
        else:
            print( "Invalid login details: {0}, {1}".format(username, password))
            return redirect('login')
    else:
        return render(request, 'auth/login.html', {} )


def register(request):

    if request.method == 'POST':
        username        = request.POST['username']
        email           = request.POST['email']
        password        = request.POST['password']
        raw_password    = request.POST['raw_password']

        if password == raw_password:

            if authenticate(username=username, password=raw_password) is None:
                    user = create_user(username, email, password)
                    auth_login(request, user)
                    return redirect('home')
            else:
                print("you have a account")
        else:
            print("error in password")


    return render(request, 'auth/register.html',{} )


def create_user(username, email, password):
    user = User.objects.create_user(username, email, password)
    user.save()
    return user


@login_required(login_url='/')
def logout_session(request):
	logout(request)
	return redirect('login')
