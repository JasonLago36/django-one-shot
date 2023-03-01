from django.contrib import admin
from todos.models import TodoList
# Register your models here.


@admin.register(TodoList)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
