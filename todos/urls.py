from django.urls import path
from todos.views import todoList_list, show_todo, todo_list_create, edit_post,delete_todo, todo_item_create, todo_item_update

urlpatterns = [
    path("", todoList_list, name='todoList_list'),
    path("<int:id>/", show_todo, name="show_todo"),
    path("create/", todo_list_create, name='todo_list_create'),
    path("<int:id>/edit/", edit_post, name="edit_post"),
    path("<int:id>/delete/", delete_todo, name='delete_todo'),
    path('items/create/', todo_item_create, name='todo_item_create'),
    path('items/<int:id>/update/', todo_item_update, name='todo_item_update'),
]
