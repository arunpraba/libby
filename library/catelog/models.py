from django.db import models


class Book(models.Model):
    """Model definition for Book."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=100, help_text="Enter a brief description of the book"
    )

    class Meta:
        """Meta definition for Book."""

        ordering = ["-id"]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


class Author(models.Model):
    """Model definition for Author."""

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookImage(models.Model):
    """Model definition for BookImage"""

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    class Meta:
        """Meta definition for book image"""

        verbose_name = "Book Image"
        verbose_name_plural = "Book Images"

    def __str__(self) -> str:
        return self.book.title
