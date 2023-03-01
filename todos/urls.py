from django.urls import path
from todos.views import todoList_list

urlpatterns = [
    path("", todoList_list, name='todoList_list')
]
