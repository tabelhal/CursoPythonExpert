from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks= Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todolist/index.html', context)