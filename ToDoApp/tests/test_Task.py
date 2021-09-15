from unittest import TestCase
from django.contrib.auth.models import User
from ToDoApp.models import Task


class TaskModelTest(TestCase):

    def test_string_representation(self):
        task = Task(task_title="My task title")
        self.assertEqual(str(task), task.task_title)

    def test_task_creation(self):
        user = User.objects.create_user(username='test admin', email='', password='123')
        task = Task.objects.create(task_title='test to do', task_complete=False, task_author=user)
        self.assertTrue(isinstance(task, Task))
