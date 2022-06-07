from django.db import models


# Create your models here.


class TodoList(models.Model):
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}'


class Todo(models.Model):
    title = models.CharField(max_length=30)
    list = models.ForeignKey(TodoList, null=True, blank=False, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] - {self.title}'