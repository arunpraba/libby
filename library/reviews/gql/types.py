from graphene_django import DjangoObjectType
from graphene import InputObjectType, String, ID, Int
from reviews.models import Review


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        convert_choices_to_enum = False
        fields = "__all__"


class ReviewInputType(InputObjectType):
    id = ID()
    user = ID()
    book = ID()
    comment = String()
    value = Int()
