from django.http import HttpResponse

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.template.base import Template
from django.template.context import Context
from django.template.loader import get_template

def home(request):
    context = {}
    context['info'] = "banana"
    return render_to_response('home.html', context, RequestContext(request))

def submit(request):
    if request.POST:
        return HttpResponse("We got " + request.POST['item'])
    else:
        return HttpResponse("Nope :(")

def hello(request):
    return HttpResponse("Hello world")
