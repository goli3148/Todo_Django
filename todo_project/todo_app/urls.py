from django.urls import path
from todo_app import views
app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login', views.auth_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.auth_logout, name='logout')
]
