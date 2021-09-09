# from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'ToDoApp'
urlpatterns = [
    path('MyToDo', views.index, name='index'),
    path('MyToDo/cross_off/<task_id>', views.cross_off, name='cross_off'),
    path('MyToDo/uncross/<task_id>', views.uncross, name='uncross'),
    path('MyToDo/delete/<task_id>', views.delete, name='delete'),
    path('MyToDo/edit/<task_id>', views.edit, name='edit'),
    # path('login', LoginView.as_view(), name='login'),
]
