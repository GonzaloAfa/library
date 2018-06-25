from django.http import HttpResponse
from django.shortcuts import render
from feeds.views import getDataGoogleBook, parserToBook
from book.models import Book

# Create your views here.
def books(request):
    return HttpResponse('<h1>list books</h1>')

# Create your views here.
def search(request):

    data = {'result': ''}

    if 'isbn' in request.GET:
        # HTTP GET variables
        isbn = request.GET.get('isbn', "")
        query  = {'isbn': isbn}
        response = getDataGoogleBook(query)
        data['result'] = parserToBook(query, response['data'])

    return render(request, 'book/search.html', data )

def list(request):

    books = Book.objects.all()
    data = { 'books': books}

    return render(request, 'book/list.html', data )


def add(request):
    data = {'result': '', 'msg': ''}

    if 'isbn' in request.POST:
        # HTTP GET variables
        isbn = request.POST.get('isbn', "")
        query = {'isbn': isbn}
        response = getDataGoogleBook(query)
        book = parserToBook(query, response['data'])


        if book['ISBN'] != '':

            element = Book(
                title = book['title'] ,
                subtitle = book['subtitle'] ,
                description = book['description'] ,
                previewLink = book['previewLink'],
                imagen = book['imagen'],
                ISBN = book['ISBN']
            )

                # ref_author = book.ref_author ,
                # ref_category = book.ref_category ,

            element.save()

            data['result'] = "ok"
        else:
            data['result'] = "error"
            data['msg'] = "error"


    return render(request, 'book/search.html', data )
