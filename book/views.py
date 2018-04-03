from django.shortcuts import HttpResponse

# Create your views here.
def books(request):
    return HttpResponse("<h1>list books</h1>")
    