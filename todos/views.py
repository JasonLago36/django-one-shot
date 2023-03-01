from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import CreateForm
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


def todo_list_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('todoList_list')
    else:
        form = CreateForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)
