from django.contrib import admin
from .models import Author, Book

# Register your models here.
classess = [Author, Book]
for model in classess:
    admin.site.register(model)
