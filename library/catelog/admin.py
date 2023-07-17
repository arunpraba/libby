from django.contrib import admin
from .models import Author, Book, BookImage

# Register your models here.
classess = [Author, Book, BookImage]
for model in classess:
    admin.site.register(model)
