from django.contrib import admin
from todos.models import TodoList, TodoItem
# Register your models here.


@admin.register(TodoList, TodoItem)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )


class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "due_date",
    )
