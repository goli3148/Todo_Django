from django.urls import path
from todo_app import views
app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('insertDB', views.insertDB, name='insertDB'),
    path('update/<int:id>', views.update, name='update'),
    path('updateDB/<int:id>', views.updateDB, name='updateDB'),
    path('deleteDB/<int:id>', views.deleteDB, name='deleteDB'),
]
