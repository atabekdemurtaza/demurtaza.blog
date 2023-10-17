from rest_framework import serializers
from movies.models import Movie


# Model Serializer
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_len_name(self, object):
        return len(object.name)

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
