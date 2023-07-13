from rest_framework import serializers
from catelog.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)

    class Meta:
        model = Book
        fields = "__all__"
