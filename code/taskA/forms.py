from django import forms
from .models import TaskA_table


class TaskAForm(forms.ModelForm):
    class Meta:
        model = TaskA_table
        fields = ('asset_contract_address', 'token_id')
