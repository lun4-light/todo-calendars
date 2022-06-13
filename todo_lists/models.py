from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    text = MarkdownxField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def date_to_integer(self):
        return self.date.year * 10000 + self.date.month * 100 + self.date.day

    def get_absolute_url(self):
        return f'/todolist/{self.pk}'

    def get_content_markdown(self):
        return markdown(self.text)

    def __str__(self):
        return f'{self.date_to_integer()} - {self.title} :: {self.author}'
