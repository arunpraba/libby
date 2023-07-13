from rest_framework import viewsets, permissions
from rest_framework.response import Response
from catelog.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from catelog.filters import BookFilter


# Define viewsets as model viewsets
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    permission_classes = [permissions.IsAuthenticated]
