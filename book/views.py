from django.shortcuts import HttpResponse

# Create your views here.
def books(request):
    a = "/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas/bookaaaaaaaaaaaas"
    b = a
    return HttpResponse("<h1>list books</h1>")
    