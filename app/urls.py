from django.urls import path
from .views import *
urlpatterns = [
    path('', hello,name = 'list'),
    path('update_task/<int:pk>/',updateTask,name = "update_tasks"),
    path('delete/<int:pk>/',delete,name = "delete_tasks")
]
