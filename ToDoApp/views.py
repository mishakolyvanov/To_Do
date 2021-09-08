from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()

# def create_task(request):
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
