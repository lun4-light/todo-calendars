from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView
from .models import Todo


# Create your views here.

class TodoDetail(DetailView):
    model = Todo


class Todolist(LoginRequiredMixin, ListView):
    model = Todo
    ordering = '-pk'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(Todolist, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_datetime(self):
        year = int(self.kwargs['date'] / 10000)
        date = int(self.kwargs['date'] % 100)
        month = int((self.kwargs['date'] % 10000 - date) / 100)

        ret = datetime(year, month, date).date()

        return ret

    def get_context_data(self, **kwargs):
        context = super(Todolist, self).get_context_data()

        todo_date = self.get_datetime()
        current_user = self.request.user

        context['todo_list'] = Todo.objects.filter(date__contains=todo_date, author=current_user)
        context['date'] = todo_date

        return context
