from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('Hello World!')

def hello(request):
    return HttpResponse('It works, Yay! :)')
