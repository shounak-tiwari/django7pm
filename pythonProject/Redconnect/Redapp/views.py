from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    temp = Task
    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on' 
        x = Task(title=title,description=description,completed = completed )
        x.save()

        return redirect('index')
    tasks = Task.objects.all()


    return render(request, 'index.html', {'dictdemo': tasks})




# from django.shortcuts import render, redirect
# from .models import Task

# def index(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
        
#         # Handle the 'completed' checkbox correctly
#         completed = request.POST.get('completed') == 'on'
        
#         # Create and save the Task instance
#         new_task = Task(title=title, description=description, completed=completed)
#         new_task.save()

#         return redirect('index')

#     # Retrieve all tasks
#     tasks = Task.objects.all()

#     return render(request, 'index.html', {'dictdemo': tasks})
