from django.urls import path
from . import views

urlpatterns = [
    path('<int:date>', views.Todolist.as_view()),
    path('<int:date>/<int:pk>', views.TodoDetail.as_view()),
]
