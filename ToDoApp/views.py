from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.task_author = request.user
            new_task.save()
            return redirect('ToDoApp:index')
        else:
            error = f'Ошибка в форме: {form.errors}'

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


def edit(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id)
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('ToDoApp:index')
        else:
            error = 'Форма неверна'
    else:
        form = TaskForm(instance=tasks)

    return render(request, 'EditToDo.html', {'form': form})


def users(request):
    tasks = Task.objects.all()
    error = ''
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'tasks': tasks
    }
    return render(request, 'Users.html', context)


def users_ToDo(request, user):
    tasks = Task.objects.filter(task_author__username=user)
    error = ''
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'tasks': tasks
    }
    return render(request, 'MyToDo.html', context)
