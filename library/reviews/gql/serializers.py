from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        meta = Review
        fields = (
            "user",
            "comment",
            "value",
            "book",
        )
