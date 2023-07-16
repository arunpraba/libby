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
        extra_kwargs = {"id": {"read_only": False, "required": False}}

    def create(self, validate_data):
        author_data = validate_data.pop("author")
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validate_data)
        return book

    def update(self, instance, validate_data):
        author_data = validate_data.pop("author")
        author, created = Author.objects.get_or_create(**author_data)
        instance.author = author
        for attr, value in validate_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
