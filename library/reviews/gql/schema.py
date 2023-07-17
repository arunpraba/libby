from graphene import ObjectType, Field, Schema, Int
from graphene_django.filter import DjangoFilterConnectionField
from reviews.models import Review
from .mutations import ReviewCreate, ReviewUpdate, ReviewDelete
from .types import ReviewType
from .queries import ReviewNode


class Query(ObjectType):
    reviews = DjangoFilterConnectionField(ReviewNode)
    review = Field(ReviewType, id=Int())

    def resolve_reviews(root, info):
        return Review.objects.all()

    def resolve_review(root, info, id):
        return Review.objects.get(id=id)


class Mutation(ObjectType):
    create_review = ReviewCreate.Field()
    update_review = ReviewUpdate.Field()
    delete_review = ReviewDelete.Field()


schema = Schema(query=Query, mutation=Mutation)
