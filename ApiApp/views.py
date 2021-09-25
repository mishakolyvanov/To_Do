from rest_framework import generics, permissions
from ToDoApp.models import Task
from . import serializers
from django.contrib.auth.models import User

from .permisisions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializerDetail


class PostList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(task_author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
