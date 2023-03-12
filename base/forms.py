from django import forms
from .models import Tasks

class TaskImageForm(forms.ModelForm):
    
    class Meta:
        model = Tasks
        fields = ['image','completed']