from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('Hello there!')
    return render(request, 'generator/home.html', {'title':'This is Home page'})


def password(request):
    # return HttpResponse('Hello there!')
    return render(request, 'generator/password.html')

def eggs(request):
    return HttpResponse('Eggs are so tasty')