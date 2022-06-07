from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Todo, TodoList


# Create your views here.

class TodolistView(ListView):
    model = Todo
    ordering = '-pk'
    fields = ['date']

    template_name = "todo_lists/todo_list.html"

    def get_context_data(self, **kwargs):
        context = super(TodolistView, self).get_context_data()
        context['TodoLists'] = TodoList.objects.all()

        return context


class TodoView(DetailView):
    model = Todo
