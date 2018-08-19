"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include

from system_auth import views as auth
from book import urls as book_urls
from home import views as home
from book import views as book_views

urlpatterns = [
    url(r'^$', auth.login, name='login'),
    url(r'^logout$', auth.logout_session, name='logout'),
    url(r'^register$', auth.register, name='register'),


    url(r'^home/$', home.index, name='home'),
    url(r'^book/', include(book_urls)),
    url(r'^admin/', admin.site.urls),

    url(r'^books', book_views.books),
]
