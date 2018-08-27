from django.conf.urls import url
from book import views as book

urlpatterns = [
    url(r'^search', book.search, name='search_book'),
    url(r'^list', book.list, name='list_book'),
    url(r'^add', book.add, name='add_book'),
]
