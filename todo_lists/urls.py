from django.urls import path
from . import views

urlpatterns = [
    path('',views.TodolistView.as_view()),
]