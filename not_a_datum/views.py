from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>No Data To Be Found!</h1> None at all")

def hello(request):
    return HttpResponse("Hello world")
