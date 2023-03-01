from django.shortcuts import render, get_object_or_404
from todos.models import TodoList
# Create your views here.


def todoList_list(request):
    todo = TodoList.objects.all()
    context = {
        "todo_object": todo,
    }
    return render(request, "todos/index.html", context)


def show_todo(request, id):
    todo = get_object_or_404(TodoList, id=id)
    context = {
        "todo_object": todo,
    }

    return render(request, "todos/detail.html", context)
