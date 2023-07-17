from graphene import relay, ObjectType, Mutation, ID, Boolean
from graphene_file_upload.scalars import Upload
import boto3
import uuid
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from .api.serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter
from .models import Book, Author, BookImage

S3_BASE_URL = "<s3-base-url>"
BUCKET = "<bucket-name>"


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        interfaces = (relay.Node,)


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = []
        interfaces = (relay.Node,)


class BookImageNode(DjangoObjectType):
    class Meta:
        model = BookImage


class BookMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer


class BookImageMutation(Mutation):
    success = Boolean()

    class Arguments:
        file = Upload(required=True)
        id = ID(required=True)

    def mutate(self, info, file, **data):
        photo_file = file
        book_id = data.get("id")
        if photo_file and book_id:
            s3 = boto3.client("s3")
            key = uuid.uuid4().hex[:6] + photo_file[photo_file.name.rfind(".") :]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f"htts://{BUCKET}.{S3_BASE_URL}/{key}"
                photo = BookImage(url=url, book_id=book_id)
                photo.save()
                return BookImageMutation(success=True)
            except Exception as err:
                print("Something went wrong")
                return BookImageMutation(success=False)
        else:
            return BookImageMutation(success=False)


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)

    author = relay.Node.Field(AuthorNode)
    authors = DjangoFilterConnectionField(AuthorNode)


class Mutation(ObjectType):
    book_mutation = BookMutation.Field()
