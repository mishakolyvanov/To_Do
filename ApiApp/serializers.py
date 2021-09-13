from rest_framework import serializers
from django.contrib.auth.models import User

from ToDoApp.models import Task


class TaskSerializer(serializers.ModelSerializer):
    task_author = serializers.ReadOnlyField(source='task_author.username')

    class Meta:
        model = Task
        fields = ['id', 'task_title', 'task_complete', 'task_author']


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
