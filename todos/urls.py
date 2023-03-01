from django.urls import path
from todos.views import todoList_list, show_todo, todo_list_create, edit_post

urlpatterns = [
    path("", todoList_list, name='todoList_list'),
    path("<int:id>/", show_todo, name="show_todo"),
    path("create/", todo_list_create, name='todo_list_create'),
    path("<int:id>/edit/", edit_post, name="edit_post")
]
