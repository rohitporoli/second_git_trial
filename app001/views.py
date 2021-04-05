from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('first page')

def hello(request):
    return HttpResponse('Hello World')
