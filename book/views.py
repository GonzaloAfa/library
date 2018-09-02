from django.http import HttpResponse
from django.shortcuts import render
from feeds.views import getDataGoogleBook, parserToBook
from feeds.antartica import getDataAntartica, parserToBookAntartica

# Models
from book.models import Book,Category,Author
from record.models import Record
from system_auth.models import Workspace

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

    # do I have that book?
    if len(book) > 0 :
        return book.first()
    else:
        # First find in Google Book
        query  = {'isbn': isbn}
        response = getDataGoogleBook(query)
        data = parserToBook(query, response['data'])

        if data['ISBN'] != '':
            return save_book(data)
        else:
            # if dont exist in Google, then find in Artartica
            result  = getDataAntartica(query)

            if result['data'] != '':
                data    = parserToBookAntartica(query, result['data'])
                return save_book(data)

            return ''
                # Sorry, I dont have that book

def save_book(book):

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

    ref_workspace= Workspace.objects.filter(ref_profile=request.user.profile, active=True).first()

    records = Record.objects.filter(ref_workspace =ref_workspace )
    print({'records': records})

    return render(request, 'book/list.html', {'records': records} )


@login_required(login_url='/')
def add(request):
    data = {'result': ''}

    if 'isbn' in request.POST:
        isbn = request.POST.get('isbn', "")

        item = Record(
            status = "created",
            ref_owner = request.user.profile,
            ref_book = Book.objects.filter(ISBN=isbn).first(),
            ref_workspace = Workspace.objects.filter(ref_profile=request.user.profile, active=True).first()
        )
        item.save()
        print("Save record")
    else:
        print("else")

    return render(request, 'book/search.html', data )
