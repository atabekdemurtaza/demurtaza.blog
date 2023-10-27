from rest_framework import serializers
from movies.models import MovieList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


# Model Serializer
class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    cast = serializers.StringRelatedField(many=True)
    platform = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = MovieList
        fields = '__all__'

    def get_len_name(self, object):
        return len(object.title)

    def validate(self, value):
        if 'name' in value and 'description' in value:
            if value['name'] == value['description']:
                raise serializers.ValidationError(
                    detail="Both fields should be different."
                )
        return value

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                detail='Name is too short.'
            )


class StreamPlatFormSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    """watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-list'
    )
"""
    class Meta:
        model = StreamPlatform
        fields = '__all__'


# Serializer 14.03.2023
    """
def name_of_length(value):
    if len(value) < 5:
        raise serializers.ValidationError(
            detail='Name is too short.'
        )


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_of_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get(
            'name',
            instance.name
        )
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.active = validated_data.get(
            'active',
            instance.active
        )
        instance.save()
        return instance

    def validate(self, value):
        if 'name' in value and 'description' in value:
            if value['name'] == value['description']:
                raise serializers.ValidationError(
                    detail="Both fields should be different."
                )
        return value
"""
