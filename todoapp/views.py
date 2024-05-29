from django.shortcuts import render, redirect
from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView






# Create your views here.

class   TaskListview(ListView):
    model = 'Task'
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = 'Task'
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
     model = Task
     template_name = 'update.html'
     context_object_name = 'task'
     fields =('name','priority','date')
