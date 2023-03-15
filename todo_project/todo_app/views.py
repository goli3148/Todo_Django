from django.shortcuts import render, get_object_or_404
from todo_app.models import todo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.views.decorators.http import require_http_methods

def index(request):
    list = todo.objects.all().values()
    return render(request, 'index.html', {'todo_list':list})
   
def insert(request):
    return render(request, 'insert.html')
    
def insertDB(request):
    sub = request.POST['Subject']
    ext = request.POST['extra']
    # request.POST['date'] => 03/09/2023 9:17 AM
    dat = datetime.strptime(request.POST['date'], "%m/%d/%Y %I:%M %p") 
    todo(subject=sub, extra=ext, date=dat).save()
    return HttpResponseRedirect(reverse('todo_app:index'))

def update(request,id):
    todo_up = get_object_or_404(todo, pk=id)
    # todo_up.date => March 9, 2023, 9:17 a.m.
    if (todo_up.date == None):
        return render(request, 'update.html', {'todo':todo_up, 'date':None})
    else:
        date = datetime.strftime(todo_up.date, '%m/%d/%Y %I:%M %p')
        return render(request, 'update.html', {'todo':todo_up, 'date':date})

@require_http_methods(['POST']) # updateDB view is working only if POST request is available
def updateDB(request, id):
    todo_up = get_object_or_404(todo, pk=id)
    todo_up.subject = request.POST['Subject']
    todo_up.extra = request.POST['extra']
    # request.POST['date'] => 03/09/2023 9:17 AM
    date = request.POST['date']
    if date is not None and not date == '':
        todo_up.date = datetime.strptime(date, "%m/%d/%Y %I:%M %p") 
    todo_up.save()
    return HttpResponseRedirect(reverse('todo_app:index'))

def deleteDB(request, id):
    todo_del = get_object_or_404(todo, pk=id)
    todo_del.delete()
    return HttpResponseRedirect(reverse('todo_app:index'))
# Create your views here.
