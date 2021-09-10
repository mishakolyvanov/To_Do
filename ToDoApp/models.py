from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    task_title = models.TextField('Текст задачи')
    task_complete = models.BooleanField('Закончено', default=False)
    task_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
