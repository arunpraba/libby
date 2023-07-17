from graphene import Boolean, Field, ID, Mutation
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from reviews.models import Review
from .types import ReviewInputType, ReviewType
from .serializers import ReviewSerializer

User = get_user_model()


class ReviewCreate(Mutation):
    review = Field(ReviewType)

    class Arguments:
        input = ReviewInputType(required=True)

    @classmethod
    @login_required
    def mutate(cls, root, info, input):
        user = info.context.user
        review_data = dict(input)
        review_data["user"] = user.id

        serializer = ReviewSerializer(data=review_data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()
        return ReviewCreate(review=review)


class ReviewUpdate(Mutation):
    review = Field(ReviewType)

    class Arguments:
        input = ReviewInputType(required=True)

    @classmethod
    @login_required
    def mutate(cls, root, info, input):
        user = info.context.user
        review_data = dict(input)
        review_instance = Review.objects.get(id=review_data.get("id"), user=user.id)

        serializer = ReviewSerializer(review_instance, data=review_data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()
        return ReviewUpdate(review=review)


class ReviewDelete(Mutation):
    success = Boolean()

    class Arguments:
        id = ID(required=True)

    @classmethod
    @login_required
    def mutate(cls, root, info, id):
        user = info.context.user
        review = Review.objects.get(id=id, user=user)
        review.delete()
        return ReviewDelete(success=True)
