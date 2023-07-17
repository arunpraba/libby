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

    def create(self, validated_data):
        author_data = validated_data.pop("author", None)
        if author_data:
            author, created = Author.objects.get_or_create(**author_data)
            validated_data["author"] = author
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop("author", None)
        if author_data:
            author, created = Author.objects.get_or_create(**author_data)
            instance.author = author
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
