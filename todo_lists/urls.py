from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:date>', views.Todolist.as_view(), name='list'),
    path('create', views.TodoCreate.as_view()),
    path('detail/<int:pk>', views.TodoDetail.as_view(), name='todo'),
]
