from django.contrib import admin
from .models import Todo
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

admin.site.register(Todo, MarkdownxModelAdmin)