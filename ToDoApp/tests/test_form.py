from unittest import TestCase
from django.contrib.auth.models import User
from ToDoApp.forms import TaskForm
from ToDoApp.models import Task


class FormTest(TestCase):
    def test_valid_form(self):
        user = User.objects.create_user(username='test admin 2', email='', password='123')
        task = Task.objects.create(task_title='test to do', task_complete=False, task_author=user)
        data = {'task_title': task.task_title, 'task_complete': task.task_complete, 'task_author': task.task_author}
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_negative(self):
        user = User.objects.create_user(username='test admin 3', email='', password='123')
        task = Task.objects.create(task_title='', task_complete=False, task_author=user)
        data = {'task_title': task.task_title, 'task_complete': task.task_complete, 'task_author': task.task_author}
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())

