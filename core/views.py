from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_look(request):
    return HttpResponse("Hello Monica!")