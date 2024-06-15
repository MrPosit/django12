from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Task
from django.urls import reverse_lazy

class ListTasks(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'tasks'

class CreateTask(CreateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status']
    success_url = reverse_lazy('list')
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = Task.Status.choices
        return context

class DetailTask(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class UpdateTask(UpdateView):
    model = Task
    fields = ['title', 'description', 'deadline', 'status']
    success_url = reverse_lazy('list')
    template_name = 'update.html'

class DeleteTask(DeleteView):
    model = Task
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')
