from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('createtodos')
            except IntegrityError:
               return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error_message':'Username has already been taken'}) 
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error_message':'Passwords did not match'})

def loginuser(request):
     if request.method == 'GET':
        return render(request, 'todo/loginuser.html',{'form': AuthenticationForm()})
     else:
        user =  authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',{'form': AuthenticationForm(), 'error_message': 'Username did not match'})
        else:
            login(request, user)
            return redirect('createtodos')

def createtodos(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodos.html', {'form': TodoForm()})
    else:
        form = TodoForm(request.POST)
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()
        return redirect('currenttodos')

def currenttodos(request):
    # todos = Todo.objects.all() for getting all todos
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/current-todos.html', {'todos': todos})

def viewtodo(request, pk_id):
    todo = get_object_or_404(Todo, pk=pk_id)
    if request.method == "GET":
        todoform = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form':todoform})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form':todoform, 'error':'Bad Info'})

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
