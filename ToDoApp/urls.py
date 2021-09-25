from django.urls import path
from . import views

app_name = 'ToDoApp'
urlpatterns = [
    path('MyToDo', views.index, name='index'),
    path('MyToDo/cross_off/<task_id>', views.cross_off, name='cross_off'),
    path('MyToDo/uncross/<task_id>', views.uncross, name='uncross'),
    path('MyToDo/delete/<task_id>', views.delete, name='delete'),
    path('MyToDo/edit/<task_id>', views.edit, name='edit'),
    path('ToDo/authors', views.users, name='users'),
    path('ToDo/<str:user>/', views.users_ToDo, name='users_ToDo'),
]
