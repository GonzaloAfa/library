from django.http import HttpResponse
from django.shortcuts import render
from feeds.views import getDataGoogleBook, parserToBook
from book.models import Book,Category,Author

from django.contrib.auth.decorators import login_required

# Create your views here.
def books(request):
    return HttpResponse('<h1>list books</h1>')

# Create your views here.
@login_required(login_url='/')
def search(request):

    data = {'result': ''}
    if 'isbn' in request.GET:
        # HTTP GET variables
        isbn = request.GET.get('isbn', "")
        data['result'] = search_internal_book(isbn)

    return render(request, 'book/search.html', data )


def search_internal_book(isbn):

    book = Book.objects.filter(ISBN=isbn)

    if len(book) > 0 :
        return book.first()

    else:
        query  = {'isbn': isbn}
        response = getDataGoogleBook(query)
        data = parserToBook(query, response['data'])

        if data['ISBN'] != '':
            return save_book(data)
        else:
            return ''

def save_book(book):
    print("save_book")
    element = Book(
        title = book['title'] ,
        subtitle = book['subtitle'] ,
        description = book['description'] ,
        previewLink = book['previewLink'],
        imagen = book['imagen'],
        ISBN = book['ISBN']
    )
    element.save()

    for author in book['authors']:

        item = Author.objects.filter(name=author)
        print(len(item))

        if len(item) < 1 :
            item = Author(name=author)
            item.save()
        else:
            item = item.first()

        element.ref_author.add(item)


    for category in book['categories']:

        item = Category.objects.filter(name=category)
        if len(item) < 1 :
            item = Category(name=category)
            item.save()
        else:
            item = item.first()
        element.ref_category.add(item)


    return element


@login_required(login_url='/')
def list(request):

    books = Book.objects.all()
    data = {'books': books}

    return render(request, 'book/list.html', data )


@login_required(login_url='/')
def add(request):
    data = {'result': '', 'msg': ''}

    return render(request, 'book/search.html', data )
