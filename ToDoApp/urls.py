from django.urls import path
from . import views

app_name = 'ToDoApp'
urlpatterns = [
    path('MyToDo', views.index, name='index'),
]
