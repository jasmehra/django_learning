Create Signup

1) in urls.py create new path
    - path('signup/', views.signupuser, name='signupuser')
    - from todo import views

2) goto  views.py in todo app and def signupuser method
    - def signupuser(request):
        return render(request, 'todo/signupuser.html')

3) Create new file in todo app
    - /todo/templates/todo/signupuser.html

4) using django forms to create signup page
    - goto views.py in todo
    - add from django.contrib.auth.forms import UserCreationForm
    - pass object to render
        -- render(request, 'todo/signupuser.html', {'form': UserCreationForm() })

5) goto template file signupuser.html
    - add {{ form }}
        -- or we can user {{ form.as_p }}  -> it shows paragraph 

6) Wrap {{ form.as_p }} inside form tag with method POST
    - add submit button with type submit
    - add {% csrf_token %}

