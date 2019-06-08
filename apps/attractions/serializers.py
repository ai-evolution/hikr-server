from rest_framework import serializers
from .models import *
from drf_extra_fields.geo_fields import PointField

__all__ = [
    'AttractionSerializer',
    'TagSerializer',
]


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = (
            'created_date',
            'updated_date',
        )


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAttraction
        fields = ('liked', 'visited', )


class AttractionSerializer(serializers.ModelSerializer):

    like_count = serializers.IntegerField(
        read_only=True
    )

    visit_count = serializers.IntegerField(
        read_only=True
    )

    state = StateSerializer(
        read_only=True,
    )

    tags = TagSerializer(
        many=True,
        read_only=True,
    )

    point = PointField(
        required=False,
    )

    class Meta:
        model = Attraction
        exclude = (
            'user',
            'created_date',
            'updated_date',
        )


