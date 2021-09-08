from django.db import models


class Task(models.Model):
    task_title = models.TextField('Текст задачи')
    task_complete = models.BooleanField('Состояние')

    def __str__(self):
        return self.task_title
