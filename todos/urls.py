from django.urls import path
from todos.views import todoList_list, show_todo

urlpatterns = [
    path("", todoList_list, name='todoList_list'),
    path("<int:id>/", show_todo, name="show_todo"),
]
