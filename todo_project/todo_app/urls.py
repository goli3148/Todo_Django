from django.urls import path
from todo_app import views
app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('update/<int:id>', views.update, name='update'),
    path('deleteDB/<int:id>', views.deleteDB, name='deleteDB'),
]
