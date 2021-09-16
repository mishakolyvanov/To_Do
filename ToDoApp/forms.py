from django.forms import ModelForm, forms, CheckboxInput, TextInput, Select
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ["task_author"]
        fields = ["task_title", "task_complete"]
        widgets = {
            "task_title": TextInput(attrs={
            }),
            "task_complete": CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
