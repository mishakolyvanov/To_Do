from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ToDoApp:index')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'tasks': tasks
    }
    return render(request, 'MyToDo.html', context)


def cross_off(request, task_id):
    task_title = Task.objects.get(pk=task_id)
    task_title.task_complete = True
    task_title.save()
    return redirect('ToDoApp:index')


def uncross(request, task_id):
    task_title = Task.objects.get(pk=task_id)
    task_title.task_complete = False
    task_title.save()
    return redirect('ToDoApp:index')


def delete(request, task_id):
    task_title = Task.objects.get(pk=task_id)
    task_title.delete()
    return redirect('ToDoApp:index')