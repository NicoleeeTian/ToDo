from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task


def addTask(request):
    # print(request.POST) return result
    # <QueryDict: {'csrfmiddlewaretoken': ['TSrgM27f8oH5MOuH75LlJfDA6giau8LAsFRH4x857t4kWdP8S2TlJHXWmPfLBZf3'], 'task': ['test']}>
    task = request.POST['task']
    Task.objects.create(task=task)
    # home is the name of urls
    return redirect('home')

def mark_as_done(request,pk):
    selected_task = get_object_or_404(Task,pk=pk)
    selected_task.is_completed = True
    selected_task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    selected_task = get_object_or_404(Task,pk=pk)
    selected_task.is_completed = False
    selected_task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        get_task.task  = request.POST['task']
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request,'edit_task.html',context)
    
def delete_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')