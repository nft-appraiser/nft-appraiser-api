from django import forms
from .models import TaskB_table


class TaskBForm(forms.ModelForm):
    class Meta:
        model = TaskB_table
        fields = ('img',)
