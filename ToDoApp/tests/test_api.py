from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ApiApp.serializers import TaskSerializer
from ToDoApp.models import Task


class TaskApiTestCase(APITestCase):
    def test_get(self):
        user = User.objects.create_user(username='test admin', email='', password='123')
        task_1 = Task.objects.create(task_title='test to do', task_complete=False, task_author=user)
        task_2 = Task.objects.create(task_title='test 2 to do', task_complete=True, task_author=user)
        url = reverse('task-list')
        response = self.client.get(url)
        serializer_data = TaskSerializer([task_1, task_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
