from django.shortcuts import render, get_object_or_404
from todo_app.models import todo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    list = todo.objects.all().values()
    return render(request, 'index.html', {'todo_list':list})
    
def insert(request):
    return render(request, 'insert.html')
    
def insertDB(request):
    sub = request.POST['Subject']
    ext = request.POST['extra']
    todo(subject=sub, extra=ext).save()
    return HttpResponseRedirect(reverse('todo_app:index'))
# Create your views here.
