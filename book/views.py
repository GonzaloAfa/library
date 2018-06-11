from django.http import HttpResponse
from django.shortcuts import render
from feeds.views import getDataGoogleBook, parserToBook

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

        print (data)

    return render(request, 'book/search.html', data )
