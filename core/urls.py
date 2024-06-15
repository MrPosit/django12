from django.contrib import admin
from django.urls import path
from app.views import ListTasks, CreateTask, DetailTask, UpdateTask, DeleteTask

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', ListTasks.as_view(), name='list'),
    path('task/<int:pk>/', DetailTask.as_view(), name='detail'),
    path('task/create/', CreateTask.as_view(), name='create'),
    path('task/update/<int:pk>/', UpdateTask.as_view(), name='update'),
    path('task/delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
]
