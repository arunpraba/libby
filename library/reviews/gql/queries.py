from graphene import relay
from graphene_django import DjangoObjectType
from reviews.models import Review


class ReviewNode(DjangoObjectType):
    class Meta:
        model = Review
        interfaces = (relay.Node,)
        filter_fields = []
