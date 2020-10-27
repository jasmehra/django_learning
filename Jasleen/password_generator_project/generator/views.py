from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return "Hii this is my first home page in django!"              #'str' object has no attribute 'get'
    #return HttpResponse('Hii this is my first home page in django!')
    # return render (request, 'generator/home.html', {'password': 'dkkdkd#djnd@$%jdhjdh'})
    return render (request, 'generator/home.html', {'password': 'dkkdkd#djnd@$%jdhjdh'})


# def eggs(request):
#     #return HttpResponse('Eggs are very tasty!!!')
#     return HttpResponse('<h1>Eggs are very tasty!!</h1>')       # we can also write html

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
   
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@#$%^&*()!'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
 
    length  = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render (request, 'generator/password.html', {'password' : thepassword})
