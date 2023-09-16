from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task


def addTask(request):
    # print(request.POST) return result
    # <QueryDict: {'csrfmiddlewaretoken': ['TSrgM27f8oH5MOuH75LlJfDA6giau8LAsFRH4x857t4kWdP8S2TlJHXWmPfLBZf3'], 'task': ['test']}>
    task = request.POST['task']
    Task.objects.create(task=task)
    # home is the name of urls
    return redirect('home')