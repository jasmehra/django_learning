from django.shortcuts import render
from django.http import HttpResponse

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
    return render (request, 'generator/password.html')
