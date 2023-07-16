from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from .api.serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter
from .models import Book, Author


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (relay.Node,)


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = []
        interfaces = (relay.Node,)


class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)

    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)


class Muation(ObjectType):
    book_muation = BookMutation.Field()