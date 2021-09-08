from django.forms import ModelForm, forms, CheckboxInput, TextInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["task_title", "task_complete"]
        widgets = {
            "task_title": TextInput(attrs={
                # 'class': 'form-control'
            }),
            "task_complete": CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
