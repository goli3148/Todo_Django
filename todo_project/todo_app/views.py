from django.shortcuts import render, get_object_or_404
from todo_app.models import todo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        # list = todo.objects.all().values()
        # list = get_object_or_404(todo, pk=request.user.id)
        list = todo.objects.filter(user=request.user.id).values()
        
        print(list)
        return render(request, 'index.html', {'todo_list':list})
    return HttpResponseRedirect(reverse('todo_app:login'))
   
def insert(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("todo_app:login"))
    if request.method == "GET":
        return render(request, 'insert.html')
    elif request.method == "POST":
        sub = request.POST['Subject']
        ext = request.POST['extra']
        # request.POST['date'] => 03/09/2023 9:17 AM
        dat = datetime.strptime(request.POST['date'], "%m/%d/%Y %I:%M %p") 
        todo(user=request.user ,subject=sub, extra=ext, date=dat).save()
        return HttpResponseRedirect(reverse('todo_app:index'))

def update(request,id):
    todo_up = get_object_or_404(todo, pk=id)
    if request.method == "GET":
        # todo_up.date => March 9, 2023, 9:17 a.m.
        if (todo_up.date == None):
            return render(request, 'update.html', {'todo':todo_up, 'date':None})
        else:
            date = datetime.strftime(todo_up.date, '%m/%d/%Y %I:%M %p')
            return render(request, 'update.html', {'todo':todo_up, 'date':date})
    elif request.method == "POST":
        todo_up.subject = request.POST['Subject']
        todo_up.extra = request.POST['extra']
        # request.POST['date'] => 03/09/2023 9:17 AM
        date = request.POST['date']
        if date is not None and not date == '':
            todo_up.date = datetime.strptime(date, "%m/%d/%Y %I:%M %p") 
        todo_up.save()
        return HttpResponseRedirect(reverse('todo_app:index'))

def delete(request, id):
    todo_del = get_object_or_404(todo, pk=id)
    todo_del.delete()
    return HttpResponseRedirect(reverse('todo_app:index'))

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todo_app:index'))
    mess = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('todo_app:index'))
        elif user is not None and not user.is_active:
            # to allow deactivated user authenticated I added :
            # AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
            # to settings.py
            mess = "account is suspended."
        else:
            mess = "Wrong user name or password."
    return render(request, 'login.html', {'message':mess})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todo_app:index'))
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        user = User.objects.create_user(username, password, email)
        if firstname is not None: user.first_name = firstname
        if lastname is not None: user.last_name = lastname
        user.save()
        return HttpResponseRedirect(reverse('todo_app:login'))
    if request.method == "GET":
        return render(request, "register.html", {})
    
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo_app:login'))
        
        
# Create your views here.
