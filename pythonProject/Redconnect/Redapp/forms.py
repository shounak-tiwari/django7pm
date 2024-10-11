from django import forms


from django.forms import ModelForm


from .models import Task

class TaskForm(forms.ModelForm):
    class meta():
        model=Task
        field = ['title','description','completed']